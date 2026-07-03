#!/usr/bin/env python3
"""Quick gap check for Bilibili v3 rollout (single-file canonical model)."""
import json
import re
import sys
from pathlib import Path

VAULT = Path(r"d:\workSpace\obsidian_repository\02-Resources\AI and Agents\B站视频知识库")
WS = Path(r"D:\workSpace\git_clone_test\hoye-git\Recastory\workspace")
MANIFEST = WS / "bilibili/manifest.json"

# A-lecture: tutorial/solo — nine-section 讲义 v3 (not Host-Guest asr)
A_LECTURE_STEMS = {
    "Karpathy爆火项目-AutoResearch解读与启发",
    "Agent实战-打造一个AI Agent的完整教程",
    "OpenAI官方-Codex新手教程",
    "Claude Code实战-构建一个AI数据分析师",
    "30分钟精通OpenClaw",
}


def has_s_column(entry: dict) -> bool:
    ing = entry.get("ingest_dir", "").replace("workspace/", "")
    col = WS / ing / "column_article.md"
    if not col.exists():
        return False
    text = col.read_text(encoding="utf-8")
    return len(text) >= 3000 and ("主持人" in text or "嘉宾" in text)


def parse_fm(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm


def is_s_canonical(text: str, fm: dict) -> bool:
    return (
        fm.get("material_tier") == "S"
        and fm.get("dialogue_version") == "v3.2"
        and "canonical-dialogue" in text
        and "v3.2-asr" not in text
    )


def is_a_dialogue_asr(text: str, fm: dict) -> bool:
    return (
        fm.get("material_tier") == "A"
        and ("canonical-dialogue v3.2-asr" in text or "canonical (ASR primary)" in text)
        and fm.get("dialogue_version") == "v3.2"
    )


def is_a_lecture(text: str, fm: dict) -> bool:
    return (
        fm.get("material_tier") == "A"
        and "讲义 v3" in text
        and "canonical-dialogue v3.2-asr" not in text
        and "## 先搞懂这一期" in text
    )


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    s_not_canonical: list[str] = []
    a_dialogue_bad: list[str] = []
    a_lecture_bad: list[str] = []
    tier_mismatch: list[str] = []
    dead_links: list[str] = []
    s_no_tier: list[str] = []
    no_ingest: list[str] = []
    long_no_spot: list[tuple[str, str]] = []
    concept_dash_en: list[tuple[str, int]] = []

    dlg_count = len(list(VAULT.rglob("* - 对谈稿.md")))
    vault_md = len(list(VAULT.rglob("*.md")))

    s_ok = a_dialogue_ok = a_lecture_ok = 0

    for entry in manifest["entries"]:
        name = Path(entry["vault_path"]).name
        stem = Path(name).stem
        note = next(VAULT.rglob(name), None)
        if not note:
            print("MISSING_VAULT", entry["bv"], name)
            continue
        text = note.read_text(encoding="utf-8")
        fm = parse_fm(text)
        is_s = has_s_column(entry)
        expect_lecture = stem in A_LECTURE_STEMS

        if is_s:
            if fm.get("material_tier") != "S":
                s_no_tier.append(name)
            if not is_s_canonical(text, fm):
                s_not_canonical.append(name)
            else:
                s_ok += 1
        elif expect_lecture:
            if not is_a_lecture(text, fm):
                a_lecture_bad.append(name)
            else:
                a_lecture_ok += 1
            if fm.get("material_tier") != "A":
                tier_mismatch.append(f"{name} (expect A lecture)")
        else:
            if not is_a_dialogue_asr(text, fm):
                a_dialogue_bad.append(name)
            else:
                a_dialogue_ok += 1
            if fm.get("material_tier") != "A":
                tier_mismatch.append(f"{name} (expect A dialogue)")

        if "ingest_dir" not in text:
            no_ingest.append(name)

        dur = fm.get("duration", "")
        m = re.match(r"(\d+):(\d+)", dur)
        if m:
            secs = int(m.group(1)) * 60 + int(m.group(2))
            if secs >= 45 * 60 and "spot_check" not in text:
                long_no_spot.append((name, dur))

        for link in re.findall(r"\[\[([^\]|]+ - 对谈稿)", text):
            dead_links.append(f"{name} -> {link}")

        if "## 关键概念" in text:
            block = text.split("## 关键概念", 1)[1].split("\n## ", 1)[0]
            if "| 英文 |" not in block:
                concept_dash_en.append((name, -1))
            else:
                rows = [
                    r
                    for r in block.splitlines()
                    if r.startswith("|") and "---" not in r and "英文" not in r
                ]
                dash = sum(1 for r in rows if re.search(r"\|\s*—\s*\|", r))
                if dash:
                    concept_dash_en.append((name, dash))

    print("VAULT_MD", vault_md, "(expect 32)")
    print("ORPHAN_DIALOGUE_FILES", dlg_count, "(expect 0)")
    print("S_CANONICAL", s_ok, "(expect 15)")
    print("A_DIALOGUE_ASR", a_dialogue_ok, "(expect 12)")
    print("A_LECTURE", a_lecture_ok, "(expect 5)")
    print("S_NOT_CANONICAL", len(s_not_canonical))
    for x in s_not_canonical:
        print(" ", x)
    print("A_DIALOGUE_BAD", len(a_dialogue_bad))
    for x in a_dialogue_bad:
        print(" ", x)
    print("A_LECTURE_BAD", len(a_lecture_bad))
    for x in a_lecture_bad:
        print(" ", x)
    print("TIER_MISMATCH", len(tier_mismatch))
    for x in tier_mismatch:
        print(" ", x)
    print("DEAD_WIKILINKS", len(dead_links))
    for x in dead_links:
        print(" ", x)
    print("S_NO_material_tier", len(s_no_tier))
    for x in s_no_tier:
        print(" ", x)
    print("NO_ingest_dir", len(no_ingest))
    for x in no_ingest:
        print(" ", x)
    print("LONG_NO_spot_check", len(long_no_spot))
    for x in long_no_spot:
        print(" ", x[0], x[1])
    print("CONCEPT_EN_DASH", len(concept_dash_en), "files")
    total_dash = sum(c for _, c in concept_dash_en if c > 0)
    print("CONCEPT_EN_DASH_ROWS", total_dash)

    failed = (
        vault_md != 32
        or dlg_count
        or s_not_canonical
        or a_dialogue_bad
        or a_lecture_bad
        or tier_mismatch
        or dead_links
    )
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
