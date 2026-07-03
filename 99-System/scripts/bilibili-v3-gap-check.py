#!/usr/bin/env python3
"""Quick gap check for Bilibili v3 rollout."""
import json
import re
from pathlib import Path

VAULT = Path(r"d:\workSpace\obsidian_repository\02-Resources\AI and Agents\B站视频知识库")
WS = Path(r"D:\workSpace\git_clone_test\hoye-git\Recastory\workspace")
MANIFEST = WS / "bilibili/manifest.json"


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


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    orphan_dialogue: list[str] = []
    s_not_canonical: list[str] = []
    dead_links: list[str] = []
    s_no_tier: list[str] = []
    no_ingest: list[str] = []
    long_no_spot: list[tuple[str, str]] = []
    concept_dash_en: list[tuple[str, int]] = []
    dlg_count = len(list(VAULT.rglob("* - 对谈稿.md")))
    vault_md = len(list(VAULT.rglob("*.md")))

    for entry in manifest["entries"]:
        name = Path(entry["vault_path"]).name
        note = next(VAULT.rglob(name), None)
        if not note:
            print("MISSING_VAULT", entry["bv"], name)
            continue
        text = note.read_text(encoding="utf-8")
        fm = parse_fm(text)
        is_s = has_s_column(entry)

        if is_s:
            if fm.get("material_tier") != "S":
                s_no_tier.append(name)
            if fm.get("dialogue_version") != "v3.2" or "canonical-dialogue" not in text:
                s_not_canonical.append(name)

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
    print("S_NOT_CANONICAL", len(s_not_canonical))
    for x in s_not_canonical:
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


if __name__ == "__main__":
    main()
