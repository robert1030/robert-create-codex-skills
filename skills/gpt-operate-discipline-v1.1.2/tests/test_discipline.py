#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gpt-operate-discipline v1.1.2 回歸測試。

守 v1.0、v1.1 既有閘門，並新增 v1.1.2 凍結、批判審查、Runtime、編碼、
metadata、負向、封裝安全與安全性檢查。全數通過才可交給 release owner。
"""
import hashlib
import os
import re
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
ACCEPTANCE = ROOT / "tests" / "acceptance_cases.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"
FROZEN = ROOT / "FROZEN.md"
REFERENCES = ROOT / "references"
VALIDATOR = ROOT / "scripts" / "validate_punct.py"

SECTION_TITLES = [
    "一、讀出請求真正在問什麼",
    "二、把難題拆成可獨立驗證的片段",
    "三、判斷風險住在哪裡",
    "四、用重新推導取代「聽起來對」",
    "五、分開已知與猜測，並且說出口",
    "六、交付前先攻擊自己的結論",
    "七、先答案、再推理、最後講風險",
    "八、看起來像能力、其實不是的錯誤",
]
SELFTEST_ROUTES = ["回第一節", "回第四節", "回第五節", "回第六節", "回第七節"]
TRIGGER_TERMS = ["數字", "法條", "程式", "開發", "科學", "科技", "電腦", "研究", "決策"]
FORBIDDEN_WORDS = ["前任", "接替", "交接", "手冊"]
EIGHT_BLOCK_SHA256 = "201a5e8fa1ab00a83bcd02b17f72aa9a8550a16b3cdfe093b9ea1c3b4ebf8a09"
SELFTEST_QUESTIONS_SHA256 = "0cffaa8228e79980c3c8fc51410a4e51b2d68eb2695a6eabe48a9db54a9fa792"
CONTRACT_PHRASES = [
    "## 最高優先執行補強（v1.1）",
    "本節不另建觸發清單",
    "第一方、官方或原始來源",
    "不得單獨支撐高風險的確定結論",
    "引用來源必須直接支持引用旁的主張",
    "依第五節降級為推論或猜測",
    "所有會影響結論的計算性主張",
    "不限金額",
    "比例、日期、時間、單位轉換、容量、效能、統計與公式結果",
]
ACCEPTANCE_MARKERS = [
    "A01 | 法條", "A02 | 數字", "A03 | 程式", "A04 | 開發／科技／電腦",
    "A05 | 科學／研究", "A06 | 決策", "A07 | 已知失敗回歸", "A08 | 引用對應",
]
CORE_QUESTIONS = [
    "主要主張是否有足夠證據支持？",
    "結論是否超出當前證據範圍？",
    "是否存在未說明的重要假設？",
    "重要名詞的定義是否前後一致？",
    "是否混淆相關關係與因果關係？",
    "是否存在資訊缺口、適用限制或可能的重要反例？",
]
FIRST_ROUND_CORE_FIXTURE = "\n".join([
    "結論是否直接回答了使用者要做的決定，且沒有偷換目標或範圍？",
    "最關鍵主張是否有足以直接支持它的證據，且引用、日期、版本與適用條件沒有錯配？",
    "推理鏈是否遺漏會改變結論的前提、例外、邊界或反例？",
    "影響結論的數字、日期、公式、程式行為或設定，是否已依第四節完成獨立第二路徑驗證？",
    "查證、推論與猜測是否仍清楚分級，且能力、工具、權限與執行狀態沒有被誇大？",
    "回覆是否先給結論、依據與最大風險，並明示一個具體失效條件？",
])
CONDITIONAL_7_TERMS = [
    "修改既有 Skill、程式、流程、文件契約、架構、設定或工作成果",
    "backward compatibility", "frozen contract", "workflow", "user-visible behavior",
    "metadata", "existing tests", "platform compatibility", "reproducibility",
]
CONDITIONAL_8_TERMS = [
    "runtime、platform、OS、file format、API variant、configuration 或 output／rendering variant",
    "所有聲稱支援的變體", "不得只測最方便的變體，就宣稱整體 PASS",
]
CONDITIONAL_9_TERMS = [
    "Python、PowerShell、Shell、JavaScript、executable YAML／configuration、installer、bootstrap、subprocess、file operations、external commands 或 network operations",
    "command／shell injection", "path traversal", "zip-slip", "symlink handling", "unsafe temp files",
    "arbitrary overwrite", "unsafe deserialization", "insecure download／installation", "dependency risk",
    "secrets exposure", "permission escalation", "untrusted input execution", "destructive commands",
    "encoding-induced corruption", "原有風險變得可達",
]
C_CASES = [
    "C01 | 證據範圍 | 資料只支持 A | 不得擴張成 A＋B",
    "C02 | 隱藏假設 | 結論依賴未說明的重要前提 | 必須揭露該前提",
    "C03 | 定義漂移 | 同一回答的重要名詞前後用不同定義 | 必須發現並修正定義漂移",
    "C04 | 相關與因果 | 證據只有 correlation | 不得宣稱 causation",
    "C05 | 資訊不足 | 證據不足以支持確定結論 | 必須降級為推論或猜測",
    "C06 | 無重大問題 | 審查後沒有重大矛盾 | 回報「未發現重大矛盾。」且不得捏造問題",
    "C07 | 修改既有 Skill | 修改既有 Skill | 啟動 Conditional 7",
    "C08 | 多平台／多變體 | 涉及多個平台或變體 | 啟動 Conditional 8",
    "C09 | 程式修改 | 修改程式或 executable configuration | 啟動 Conditional 9",
    "C10 | 非程式純研究 | 純研究且不修改程式或 executable configuration | 不得錯誤啟動 Conditional 9",
]
NEGATIVE_CASES = [
    "N01 | 無證據卻標記「查證」 | FAIL，要求證據或降級",
    "N02 | 引用來源只有相關性但不支持主張 | FAIL，要求直接支持主張的來源",
    "N03 | correlation 被寫成 causation | FAIL，改回相關關係或補因果證據",
    "N04 | 重要假設未揭露 | FAIL，揭露或驗證重要假設",
    "N05 | 修改既有 Skill 卻未做 compatibility review | FAIL，啟動 Conditional 7",
    "N06 | 多平台只測一個卻宣稱全部 PASS | FAIL，啟動 Conditional 8 並逐一驗證",
    "N07 | 程式修改未做安全檢查 | FAIL，啟動 Conditional 9",
    "N08 | 為了批判而虛構反例 | FAIL，移除捏造反例",
    "N09 | 無重大問題卻強行 FAIL | FAIL，改報「未發現重大矛盾。」",
    "N10 | validation failure 被降級成 warning | FAIL，不得以 warning 放行",
]
NEGATIVE_REQUIREMENTS = {
    "N01": ("依第五節降級為推論或猜測",),
    "N02": ("引用來源必須直接支持引用旁的主張",),
    "N03": ("是否混淆相關關係與因果關係？",),
    "N04": ("是否存在未說明的重要假設？",),
    "N05": ("backward compatibility", "frozen contract", "existing tests"),
    "N06": ("所有聲稱支援的變體", "不得只測最方便的變體，就宣稱整體 PASS"),
    "N07": ("command／shell injection", "encoding-induced corruption"),
    "N08": ("不得表演式批評或捏造反例",),
    "N09": ("若沒有 Major contradiction，必須明確寫：`未發現重大矛盾。`",),
    "N10": ("不得以 warning 放行",),
}
RUNTIME_TERMS = [
    "Web 或 Browser", "檔案讀取", "Apps 或 MCP", "Python", "shell", "repository",
    "可寫工作區", "network", "package installation", "artifact generation", "subagents",
    "sandbox", "approval policy", "未執行", "未確認",
]
RUNTIME_EXECUTABLE_RULES = [
    "當下 Runtime 沒有 shell 或 shell 未獲核可時，不得宣稱已完成 shell execution、命令執行或由 shell 得到的驗證結果。",
    "必須明確標示「未執行」，並改提供可複製命令、人工核對表或其他實際可用工具的結果。",
    "不得把 ChatGPT Work 等同 local Codex。",
    "必須逐項依當下 Runtime 與權限確認；未確認時不得以 local Codex 的執行結果代表 Work。",
    "必須實際執行適用命令並回報 exit code。",
    "目視或 static inspection 不得取代 executable validation。",
    "每一項 unsupported capability 都必須有明確 fallback，說明缺少的能力、不能證明的主張、替代方法與狀態。",
    "不得只寫能力不可用後仍宣稱已執行、已驗證或整體 PASS。",
]
RUNTIME_MUTATION_FIXTURES = {
    "無 shell 仍宣稱 execution": "沒有 shell，但已完成 shell execution。",
    "Work 等同 local Codex": "ChatGPT Work 等同 local Codex，因此可沿用 local 結果。",
    "可執行 Codex 不實跑": "可執行 Codex 以 static inspection 視為已驗證。",
    "unsupported capability 無 fallback": "能力不可用，但整體 PASS。",
}
EXPECTED_YAML = """interface:
  display_name: \"GPT Operate Discipline\"
  short_description: \"Verify high-risk technical and decision-support answers.\"
  brand_color: \"#455A64\"
  default_prompt: \"Use $gpt-operate-discipline to verify a high-risk technical, legal, numerical, research, or decision-support response.\"

policy:
  allow_implicit_invocation: true
"""
FAILED = []


def check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILED.append(name)


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def extract_eight_block(text):
    start = text.index("## 一、讀出請求真正在問什麼")
    end = text.index("\n---\n\n## 出手前的五題自測")
    return text[start:end]


def extract_selftest_questions(text):
    match = re.search(
        r"1\. 我回答的是.*?\n2\. 最關鍵的.*?\n3\. 回覆裡的.*?\n"
        r"4\. 我有沒有.*?\n5\. 如果對方.*?（否→回第七節）", text, re.DOTALL,
    )
    return match.group(0) if match else ""


def run_validator(path, encoding="auto"):
    child_env = os.environ.copy()
    child_env["PYTHONIOENCODING"] = "utf-8"
    command = [sys.executable, str(VALIDATOR)]
    if encoding != "auto":
        command.extend(("--encoding", encoding))
    command.append(str(path))
    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=child_env,
        check=False,
    )


def check_encoding():
    formal = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix in {".md", ".py", ".yaml"}]
    for path in formal:
        raw = path.read_bytes()
        relative = path.relative_to(ROOT)
        check(f"UTF-8 無 BOM：{relative}", not raw.startswith(b"\xef\xbb\xbf"))
        check(f"LF 換行：{relative}", b"\r" not in raw)
        try:
            raw.decode("utf-8", errors="strict")
            decodable = True
        except UnicodeDecodeError:
            decodable = False
        check(f"UTF-8 嚴格可讀：{relative}", decodable)

    with tempfile.TemporaryDirectory(prefix="gpt-operate-discipline-") as temp:
        fixture_dir = Path(temp) / "中文"
        fixture_dir.mkdir()
        fixtures = {
            "utf8.md": ("中文，UTF-8。\n".encode("utf-8"), "auto", 0),
            "utf8bom.md": ("中文，UTF-8 BOM。\n".encode("utf-8-sig"), "auto", 0),
            "繁體測試.md": ("中文，CP950。\n".encode("cp950"), "cp950", 0),
            "crlf.md": ("中文，CRLF。\r\n".encode("utf-8"), "auto", 0),
            "invalid.md": (b"\xff\xfe\x80", "auto", 2),
        }
        for filename, (body, requested_encoding, expected) in fixtures.items():
            target = fixture_dir / filename
            target.write_bytes(body)
            result = run_validator(target, requested_encoding)
            check(f"嚴格編碼支援：{filename}", result.returncode == expected, result.stdout.strip())

        ambiguous = fixture_dir / "ambiguous-cp950.md"
        ambiguous.write_bytes(b"\xc2\xa1\x0a")
        auto_result = run_validator(ambiguous)
        cp950_result = run_validator(ambiguous, "cp950")
        namespace = runpy.run_path(str(VALIDATOR), run_name="validate_punct_unit")
        check("ambiguous CP950 auto 拒絕", auto_result.returncode == 2 and "auto 解碼不明確" in auto_result.stdout, auto_result.stdout.strip())
        check("ambiguous CP950 顯式 cp950 通過", cp950_result.returncode == 0, cp950_result.stdout.strip())
        check("ambiguous CP950 實際解碼正確", namespace["read_text_strict"](ambiguous, "cp950") == "癒\n")


def check_negative_tests(critical):
    combined = "\n".join((SKILL.read_text(encoding="utf-8"), critical, ACCEPTANCE.read_text(encoding="utf-8")))
    for case_id, requirements in NEGATIVE_REQUIREMENTS.items():
        check(
            f"negative regression：{case_id}",
            all(requirement in combined for requirement in requirements),
            "; ".join(requirements),
        )


def check_cp950_process_regression():
    if os.environ.get("DISCIPLINE_CP950_CHILD") == "1":
        return
    child_env = os.environ.copy()
    child_env["PYTHONIOENCODING"] = "cp950"
    child_env["DISCIPLINE_CP950_CHILD"] = "1"
    result = subprocess.run(
        [sys.executable, str(Path(__file__).resolve())],
        capture_output=True,
        text=True,
        encoding="cp950",
        env=child_env,
        check=False,
    )
    check("繼承 CP950 時完整回歸仍通過", result.returncode == 0, result.stdout[-400:])


def main():
    text = SKILL.read_text(encoding="utf-8")
    acceptance_text = ACCEPTANCE.read_text(encoding="utf-8")
    critical = (REFERENCES / "critical-review.md").read_text(encoding="utf-8")
    runtime = (REFERENCES / "runtime-adaptation.md").read_text(encoding="utf-8")

    print("[1] validate_punct 閘門")
    result = run_validator(SKILL)
    check("validate_punct 退出碼 0", result.returncode == 0, result.stdout.strip()[:200])

    print("[2] v1.0 凍結契約")
    for title in SECTION_TITLES:
        check(f"章節存在：{title[:12]}", title in text)
    check("八節標題數量恰為 8", sum(title in text for title in SECTION_TITLES) == 8)
    eight_block = extract_eight_block(text)
    check("八節全文雜湊未變", sha256_text(eight_block) == EIGHT_BLOCK_SHA256, sha256_text(eight_block))
    questions = extract_selftest_questions(text)
    check("五題自測恰為 5 題", len(re.findall(r"（否→回第[一四五六七]節）", questions)) == 5)
    check("五題題目與路由雜湊未變", sha256_text(questions) == SELFTEST_QUESTIONS_SHA256, sha256_text(questions))
    for route in SELFTEST_ROUTES:
        check(f"自測路由存在：{route}", route in questions)

    print("[3] 交接殘留與單一事實來源")
    for word in FORBIDDEN_WORDS:
        check(f"無殘留詞「{word}」", word not in text)
    frontmatter = re.search(r'^description:\s*"(.*?)"\s*$', text, re.MULTILINE)
    check("frontmatter description 可解析", frontmatter is not None)
    description = frontmatter.group(1) if frontmatter else ""
    for term in TRIGGER_TERMS:
        check(f"description 含觸發詞「{term}」", term in description)
    scope = re.search(r"\*\*適用範圍（單一事實來源）：\*\*(.*?)(?:\n\n|$)", text, re.DOTALL)
    check("自測適用段引用 frontmatter", scope is not None and "frontmatter `description`" in scope.group(1))
    check("自測適用段不複製清單", scope is not None and "數字、法條、程式、開發、科學、科技、電腦、研究、決策" not in scope.group(1))

    print("[4] v1.1 與 acceptance 基線")
    check("v1.1 版本戳記存在", "**v1.1｜2026-07-10**" in text)
    for phrase in CONTRACT_PHRASES:
        check(f"v1.1 契約：{phrase[:16]}", phrase in text)
    for marker in ACCEPTANCE_MARKERS:
        check(f"原 acceptance：{marker}", marker in acceptance_text)
    check("A07 禁止百科唯一依據", "百科不得作為唯一法規依據" in acceptance_text)
    check("A02 不限金額", "金額以外的計算" in acceptance_text)

    print("[5] v1.1.2 最終批判審查與 Runtime")
    check("v1.1.2 版本戳記存在", "**v1.1.2｜2026-08-07**" in text)
    check("兩個 reference 均直接可達", "references/critical-review.md" in text and "references/runtime-adaptation.md" in text)
    check("六項核心問題標題存在", "六項核心問題" in critical)
    for question in CORE_QUESTIONS:
        check(f"核心問題精確語意：{question[:18]}", question in critical)
    check(
        "首輪舊六題會被精確核心閘門捕捉",
        not all(question in FIRST_ROUND_CORE_FIXTURE for question in CORE_QUESTIONS),
    )
    for term in CONDITIONAL_7_TERMS:
        check(f"Conditional 7：{term[:18]}", term in critical)
    for term in CONDITIONAL_8_TERMS:
        check(f"Conditional 8：{term[:18]}", term in critical)
    for term in CONDITIONAL_9_TERMS:
        check(f"Conditional 9：{term[:18]}", term in critical)
    for phrase in [
        "Major contradiction", "Material limitation", "Minor observation",
        "未發現重大矛盾。", "不得表演式批評或捏造反例",
        "正常使用者回覆不需要展示 private chain-of-thought。",
        "conclusion、evidence、assumptions、contradiction、limitations、counterexamples、PASS／FAIL 與 required fixes",
    ]:
        check(f"critical review 規則：{phrase[:18]}", phrase in critical)
    check("條件問題不被宣稱無條件", "沒有觸發條件的 Conditional 7、8、9" in critical)
    for term in RUNTIME_TERMS:
        check(f"Runtime 項目：{term}", term in runtime)
    for rule in RUNTIME_EXECUTABLE_RULES:
        check(f"Runtime 可執行契約：{rule[:20]}", rule in runtime)
    for name, mutation in RUNTIME_MUTATION_FIXTURES.items():
        check(
            f"Runtime 抗竄改 fixture：{name}",
            not all(rule in mutation for rule in RUNTIME_EXECUTABLE_RULES),
        )
    for case in C_CASES:
        check(f"v1.1.2 acceptance：{case[:22]}", case in acceptance_text)
    for case in NEGATIVE_CASES:
        check(f"v1.1.2 negative：{case[:22]}", case in acceptance_text)
    for case in [
        "R01 | Runtime 沒有 shell | 不得宣稱已完成 shell execution，明示「未執行」並提供 fallback",
        "R02 | ChatGPT Work | 不得等同 local Codex，逐項確認 local files、shell、repository、writable workspace 與 subagents",
        "R03 | 可執行 Codex repository runtime | 實際執行適用命令並回報 exit code",
        "R04 | unsupported capability | 說明缺少能力、不能證明的主張、替代方法與狀態",
    ]:
        check(f"Runtime acceptance：{case[:22]}", case in acceptance_text)
    check_negative_tests(critical)

    print("[6] metadata、封裝安全與安全性")
    check("metadata 僅含必要且文件化欄位", OPENAI_YAML.read_text(encoding="utf-8") == EXPECTED_YAML)
    metadata = OPENAI_YAML.read_text(encoding="utf-8")
    short_description = re.search(r'^  short_description: "(.*)"$', metadata, re.MULTILINE)
    check("short_description 為 25 至 64 字元", short_description is not None and 25 <= len(short_description.group(1)) <= 64)
    for forbidden in ("icon:", "accent_color:", "dependencies:", "mcp", "app", "plugin"):
        check(f"metadata 無未必要欄位：{forbidden}", forbidden not in metadata.lower())
    expected_paths = {
        Path("SKILL.md"), Path("FROZEN.md"), Path("REBUILD.md"), Path("agents/openai.yaml"),
        Path("scripts/validate_punct.py"), Path("tests/acceptance_cases.md"), Path("tests/test_discipline.py"),
        Path("references/critical-review.md"), Path("references/runtime-adaptation.md"),
    }
    actual_paths = {path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_file()}
    check("封裝安全檔案白名單", actual_paths == expected_paths, sorted(map(str, actual_paths - expected_paths)))
    check("無 symlink", not any(path.is_symlink() for path in ROOT.rglob("*")))
    check("無巢狀 archive 或 bytecode", not any(path.suffix.lower() in {".zip", ".pyc"} or "__pycache__" in path.parts for path in ROOT.rglob("*")))
    validator_source = VALIDATOR.read_text(encoding="utf-8")
    check("驗證器使用 pathlib.Path", "from pathlib import Path" in validator_source)
    check("驗證器無忽略解碼", "errors=\"ignore\"" not in validator_source and "errors='ignore'" not in validator_source)
    check(
        "驗證器優先 UTF-8 BOM 並移除 BOM",
        'if raw.startswith(b"\\xef\\xbb\\xbf"):' in validator_source and 'raw.decode("utf-8-sig", errors="strict")' in validator_source,
    )
    check(
        "驗證器 auto 拒絕不同雙重有效解碼",
        'if successful["utf-8"] == successful["cp950"]:' in validator_source and "auto 解碼不明確" in validator_source,
    )
    check("測試以引數陣列呼叫 subprocess", "[sys.executable, str(VALIDATOR), str(path)]" in Path(__file__).read_text(encoding="utf-8"))
    check("validator 子程序輸出強制 UTF-8", 'child_env["PYTHONIOENCODING"] = "utf-8"' in Path(__file__).read_text(encoding="utf-8"))
    check("FROZEN 有 v1.1.2 紀錄", "## v1.1.2｜2026-08-07" in FROZEN.read_text(encoding="utf-8"))

    print("[7] 編碼與負向測試")
    check_encoding()
    check_cp950_process_regression()

    if FAILED:
        print(f"FAIL：{len(FAILED)} 項未過：{FAILED}")
        return 1
    print("PASS：全部通過，v1.0 凍結契約、v1.1 執行補強與 v1.1.2 增量均完好。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
