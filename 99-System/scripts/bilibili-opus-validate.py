#!/usr/bin/env python3
"""Validate Bilibili opus notes against the column-first ingest contract."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


VALID_SOURCE_TIERS = {"C1", "C2"}
VALID_MATERIAL_TIERS = {"S", "A", "B"}
VALID_FORMS = {"lecture", "dialogue", "roundtable"}
VALID_FACTUAL = {"verified", "partial", "unverified"}
NOISE_LINES = (
    "关注UP主", "关注 UP 主", "点赞", "投币", "收藏", "评论区", "展位",
    "没有更多评论", "分享至", "投诉或建议",
)


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    result: dict[str, object] = {}
    active_list: str | None = None
    for line in parts[1].splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if active_list and stripped.startswith("- "):
            cast = result.setdefault(active_list, [])
            if isinstance(cast, list):
                cast.append(stripped[2:].strip().strip('"\''))
            continue
        active_list = None
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        raw = value.strip().strip('"\'')
        if not raw:
            result[key] = []
            active_list = key
        elif raw.startswith("[") and raw.endswith("]"):
            result[key] = [item.strip().strip('"\'') for item in raw[1:-1].split(",") if item.strip()]
        else:
            result[key] = raw
    return result


def classify_source(has_body: bool, has_sections: bool, has_identity: bool, has_anchor: bool) -> str:
    return "C1" if all((has_body, has_sections, has_identity, has_anchor)) else "C2"


def classify_form(text: str) -> str:
    if re.search(r"^##\s*(主题演讲|核心判断|关键机制|演讲)", text, re.MULTILINE):
        return "lecture"
    labels = re.findall(r"^([^\n：:]{1,24})[：:]", text, re.MULTILINE)
    unique = {label.strip() for label in labels if label.strip() not in {"现场提问", "观众提问"}}
    if len(unique) >= 3:
        return "roundtable"
    if len(unique) >= 2:
        return "dialogue"
    return "lecture"


def normalize_column_text(text: str) -> str:
    text = re.sub(r"^unknown[：:]", "现场提问：", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"!\[[^]]*\]\([^)]*\)", "", text)
    output: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if any(noise in stripped for noise in NOISE_LINES):
            continue
        if stripped and stripped in seen and not stripped.startswith("#"):
            continue
        if stripped:
            seen.add(stripped)
        output.append(line.rstrip())
    return "\n".join(output).strip()


def _body(text: str) -> str:
    parts = text.split("---", 2)
    return parts[2] if len(parts) == 3 else text


def _ids(text: str) -> dict[str, str]:
    fm = parse_frontmatter(text)
    return {key: str(fm.get(key, "")).strip().rstrip("/") for key in ("bv", "opus_id", "column_id")}


def _is_knowledge_note(path: Path, vault_root: Path) -> bool:
    relative = path.relative_to(vault_root)
    return bool(relative.parts) and relative.parts[0] in {"00-Inbox", "01-Areas", "02-Resources", "03-Archive"}


def validate_note_text(text: str, sources_read: set[str] | None = None) -> dict[str, object]:
    fm = parse_frontmatter(text)
    errors: list[str] = []
    warnings: list[str] = []
    for key in ("title", "tags", "created", "source", "description"):
        if key not in fm:
            errors.append(f"missing frontmatter field: {key}")
    if fm.get("source_type") != "bilibili_opus":
        errors.append("source_type must be bilibili_opus")
    if fm.get("primary_source") != "column":
        errors.append("primary_source must be column")
    if fm.get("source_tier") not in VALID_SOURCE_TIERS:
        errors.append("source_tier must be C1 or C2")
    if fm.get("material_tier") not in VALID_MATERIAL_TIERS:
        errors.append("material_tier must be S, A, or B")
    if fm.get("content_form") not in VALID_FORMS:
        errors.append("content_form must be lecture, dialogue, or roundtable")
    opus = str(fm.get("opus_id", ""))
    column = str(fm.get("column_id", ""))
    bv = str(fm.get("bv", ""))
    if not re.fullmatch(r"\d{10,}", opus):
        errors.append("opus_id must be a numeric Bilibili opus id")
    if column and not re.fullmatch(r"cv\d+", column):
        errors.append("column_id must match cv<digits>")
    if not re.fullmatch(r"BV[0-9A-Za-z]+", bv):
        errors.append("bv must match BV<id>")
    if not opus and not column:
        errors.append("primary_source column requires opus_id or column_id")

    form = fm.get("content_form")
    fidelity = fm.get("dialogue_fidelity")
    question = fm.get("question_source")
    if form == "lecture" and (fidelity != "none" or question != "none"):
        errors.append("lecture must use dialogue_fidelity/question_source: none")
    if form in {"dialogue", "roundtable"} and (fidelity != "source" or question != "transcript"):
        errors.append("dialogue/roundtable must use source/transcript")

    factual = fm.get("factual_status")
    if factual not in VALID_FACTUAL:
        errors.append("factual_status must be verified, partial, or unverified")
    basis = fm.get("verification_basis", [])
    unresolved = fm.get("unresolved_facts", [])
    if factual == "verified":
        if not fm.get("factual_reviewed"):
            errors.append("verified notes require factual_reviewed")
        if not isinstance(basis, list) or not basis:
            errors.append("verified notes require verification_basis")
        if isinstance(unresolved, list) and unresolved:
            errors.append("verified notes cannot contain unresolved_facts")
    if isinstance(basis, list) and sources_read is not None:
        for item in basis:
            if item not in sources_read:
                errors.append(f"verification_basis contains unread source: {item}")

    body = _body(text)
    if re.search(r"^(?:Moderator|unknown)[：:]", body, re.MULTILINE | re.IGNORECASE):
        errors.append("column notes must not contain Moderator or unknown speaker labels")
    if re.search(r"!\[[^]]*\]\([^)]*\)", body):
        errors.append("column notes must not embed downloaded or recognized images")
    if not re.search(r"\[\[[^]]+\]\]", body) and fm.get("status") != "orphan":
        errors.append("note requires a wikilink or status: orphan")
    if " - 对谈稿" in str(fm.get("title", "")):
        errors.append("canonical title must not use - 对谈稿")
    if factual == "unverified":
        warnings.append("unverified note is a discovery lead, not a citable fact source")

    return {
        "workflow": "bilibili_opus_ingest_v1",
        "source_id": {"opus": opus, "column": column, "bv": bv},
        "route": {"source_tier": fm.get("source_tier"), "material_tier": fm.get("material_tier"), "content_form": form},
        "sources_read": sorted(sources_read or set(basis if isinstance(basis, list) else [])),
        "sources_skipped": ["images", "transcript"],
        "checks": {},
        "errors": errors,
        "warnings": warnings,
        "unresolved": errors.copy(),
        "status": "complete" if not errors else "incomplete",
    }


def validate_note_file(note_path: Path, vault_root: Path, sources_read: set[str] | None = None) -> dict[str, object]:
    text = note_path.read_text(encoding="utf-8")
    result = validate_note_text(text, sources_read)
    errors = list(result["errors"])
    own = _ids(text)
    for other in vault_root.rglob("*.md"):
        if other.resolve() == note_path.resolve():
            continue
        if not _is_knowledge_note(other, vault_root):
            continue
        candidate = _ids(other.read_text(encoding="utf-8", errors="replace"))
        for key in ("bv", "opus_id", "column_id"):
            if own[key] and own[key] == candidate[key]:
                errors.append(f"duplicate {key} found in {other.relative_to(vault_root).as_posix()}")
    sibling = note_path.with_name(f"{note_path.stem} - 对谈稿.md")
    if sibling.exists():
        errors.append("canonical note has a - 对谈稿 sibling")
    result["errors"] = errors
    result["unresolved"] = errors.copy()
    result["status"] = "complete" if not errors else "incomplete"
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path)
    parser.add_argument("--vault-root", type=Path, default=Path.cwd())
    parser.add_argument("--sources-read", nargs="*", default=["column"])
    args = parser.parse_args()
    result = validate_note_file(args.note, args.vault_root, set(args.sources_read))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["status"] == "complete" else 1)


if __name__ == "__main__":
    main()
