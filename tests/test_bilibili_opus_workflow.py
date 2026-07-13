import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "99-System" / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


BASE = """---
title: "{title}"
tags: [ai_agent, video_transcript, bilibili]
created: 2026-07-13
source: "https://www.bilibili.com/opus/{opus}"
description: "测试专栏"
source_type: bilibili_opus
source_url: "https://www.bilibili.com/opus/{opus}"
opus_id: "{opus}"
column_id: "{column}"
video_url: "https://www.bilibili.com/video/{bv}/"
bv: "{bv}"
uploader: "Easonlee的AI笔记"
source_tier: {source_tier}
primary_source: column
material_tier: S
content_form: {form}
dialogue_fidelity: {fidelity}
question_source: {question_source}
factual_status: {factual_status}
factual_reviewed: 2026-07-13
verification_basis:
  - column
{extra}---
# {title}

## 核心判断

机制和案例。

## 相关阅读

- [[相关笔记]]
"""


class OpusWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script("bilibili-opus-validate.py")

    def note(self, **overrides):
        values = dict(
            title="专栏测试", opus="1224198797632995337", column="cv51417405",
            bv="BV1U4Tz6CEzu", source_tier="C1", form="lecture", fidelity="none",
            question_source="none", factual_status="verified", extra="",
        )
        values.update(overrides)
        return BASE.format(**values)

    def test_complete_opus_is_c1(self):
        self.assertEqual(self.module.classify_source(True, True, True, True), "C1")

    def test_incomplete_opus_is_c2(self):
        self.assertEqual(self.module.classify_source(True, True, False, True), "C2")

    def test_lecture_with_qa_remains_lecture(self):
        body = "## 主题演讲\n机制说明\n## 现场问答\n观众提问：如何落地？"
        self.assertEqual(self.module.classify_form(body), "lecture")

    def test_dialogue_and_roundtable_classification(self):
        self.assertEqual(self.module.classify_form("主持人：为什么？\n嘉宾：因为机制。\n主持人：限制呢？\n嘉宾：边界。"), "dialogue")
        self.assertEqual(self.module.classify_form("甲：观点一\n乙：回应\n丙：另一种限制\n乙：补充"), "roundtable")

    def test_unknown_question_is_normalized(self):
        self.assertNotIn("unknown：", self.module.normalize_column_text("unknown：如何评估？"))
        self.assertIn("现场提问：", self.module.normalize_column_text("unknown：如何评估？"))

    def test_noise_and_images_are_removed(self):
        text = "摘要\n核心结论\n重点速览\n核心结论\n关注UP主\n![图](x.png)\n机制"
        cleaned = self.module.normalize_column_text(text)
        self.assertEqual(cleaned.count("核心结论"), 1)
        self.assertNotIn("关注UP主", cleaned)
        self.assertNotIn("![图]", cleaned)

    def test_column_note_needs_no_transcript_or_spot_check(self):
        result = self.module.validate_note_text(self.note())
        self.assertEqual(result["status"], "complete")
        self.assertFalse(any("transcript" in e.lower() or "spot_check" in e for e in result["errors"]))

    def test_lecture_contract(self):
        result = self.module.validate_note_text(self.note(fidelity="source", question_source="transcript"))
        self.assertIn("lecture must use dialogue_fidelity/question_source: none", result["errors"])

    def test_dialogue_requires_source_transcript(self):
        result = self.module.validate_note_text(self.note(form="dialogue", fidelity="none", question_source="none"))
        self.assertIn("dialogue/roundtable must use source/transcript", result["errors"])

    def test_verified_rejects_unresolved(self):
        result = self.module.validate_note_text(self.note(extra="unresolved_facts:\n  - 人名待核\n"))
        self.assertIn("verified notes cannot contain unresolved_facts", result["errors"])

    def test_basis_is_limited_to_sources_read(self):
        text = self.note().replace("  - column", "  - column\n  - transcript")
        result = self.module.validate_note_text(text, sources_read={"column"})
        self.assertIn("verification_basis contains unread source: transcript", result["errors"])

    def test_requires_link_or_orphan(self):
        result = self.module.validate_note_text(self.note().replace("- [[相关笔记]]", ""))
        self.assertIn("note requires a wikilink or status: orphan", result["errors"])

    def test_rejects_moderator_and_unknown_labels(self):
        result = self.module.validate_note_text(self.note() + "\nModerator：问题\nunknown：追问\n")
        self.assertIn("column notes must not contain Moderator or unknown speaker labels", result["errors"])

    def test_duplicate_bv_opus_or_column_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            area = root / "02-Resources"
            area.mkdir()
            first = area / "first.md"
            second = area / "second.md"
            first.write_text(self.note(), encoding="utf-8")
            second.write_text(self.note(title="重复"), encoding="utf-8")
            result = self.module.validate_note_file(second, root)
            self.assertTrue(any("duplicate" in e for e in result["errors"]))

    def test_system_and_fixture_files_do_not_create_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            area = root / "02-Resources"
            fixtures = root / "tests" / "fixtures"
            area.mkdir()
            fixtures.mkdir(parents=True)
            note = area / "note.md"
            note.write_text(self.note(), encoding="utf-8")
            (fixtures / "sample.md").write_text(self.note(), encoding="utf-8")
            result = self.module.validate_note_file(note, root)
            self.assertFalse(any("duplicate" in e for e in result["errors"]))

    def test_report_declares_images_and_transcript_skipped(self):
        result = self.module.validate_note_text(self.note())
        self.assertEqual(result["workflow"], "bilibili_opus_ingest_v1")
        self.assertEqual(result["sources_skipped"], ["images", "transcript"])

    def test_real_shape_fixtures_validate(self):
        fixture_root = ROOT / "tests" / "fixtures" / "bilibili_opus"
        for path in fixture_root.glob("*.fixture"):
            with self.subTest(path=path.name):
                result = self.module.validate_note_text(path.read_text(encoding="utf-8"), sources_read={"column"})
                self.assertEqual(result["status"], "complete", result["errors"])


if __name__ == "__main__":
    unittest.main()
