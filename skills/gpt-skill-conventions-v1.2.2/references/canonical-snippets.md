# 標準片段（可直接複製到新 skill）

每段都是從 Joan（酒 Ann）五包抽出的、已驗證可用的範式。複製後依該 skill 調整命名即可。

---

## 1. 版號戳記（五包統一格式，放 SKILL.md H1 正下方）

```markdown
# <Skill 顯示名稱>

> **vX.Y｜YYYY-MM-DD**：<這一版做了什麼，一句話>。
```

升級規則（三級明確定義，低階模型照做即可）：
- **patch**（v2.1 → v2.1.1）：版型／引擎不動，只改驗證器、文件、錯字。
- **minor**（v1.1 → v1.2）：新增功能、往 registry 加新皮膚／新版型、擴充驗證層。凍結項一律不動。
- **major**（v1.2 → v2.0）：**唯一觸發條件是動到凍結版面**。做法不是修改凍結項，而是：舊凍結項原封保留在 registry、新視覺以新具名項加入並凍結、版號進 major、`FROZEN.md` 記兩者。既有產出永遠可用舊名重現。

---

## 2. 凍結契約（程式內標記＋帳本）

程式內用集合或常數標記凍結項，並附註解：

```python
SKINS = {
    "joan-coral": dict(  # 凍結 FROZEN，改色即破壞，不可隨意動
        bg="#E8856E", accent="#C75A41", qbg="#C75A41", barbg="#3a302d", ...),
    "joan-yellow": dict(...),   # 可調
}
FROZEN = {"joan-coral"}
```

每包放一份 `FROZEN.md` 帳本：

```markdown
# 凍結紀錄
## vX.Y ｜ YYYY-MM-DD ｜ 已鎖定
- 鎖了什麼（座標／色票／皮膚 token）。
- 定版檔：assets/example_*.html（皆通過驗證器）。
要調整 → 另開新版本，不動本版。
```

並在回歸測試裡把凍結值寫成斷言守門（見第 6 段）。

---

## 3. bootstrap 自動安裝

**本段已併入第 8 段，bootstrap 只有一種正本範式，不再維護兩個版本**（雙範式本身就是漂移源）。正本檔在 `assets/bootstrap.py`，複製後依該 skill 相依裁剪 `ensure_*` 顆粒。shell 版（setup.sh）務必冪等：已備妥則秒過，可被一鍵腳本自動觸發。

---

## 4. 生成前對焦閘門（開場模板）

依 skill 性質剪裁。「問不問」不憑感覺，照三欄決策表操課：

| 項目 | 歸類 | 規則 |
| --- | --- | --- |
| 輸出語言（中／英／雙語） | 必問 | 除非使用者本輪明講，否則一定問 |
| 對象學齡／受眾層級 | 必問 | 除非使用者本輪明講，否則一定問 |
| 方向與深度、範圍 | 可推斷 | 對話中有明確線索（如「國三會考複習」）就直接採用，複述時講明推斷依據；無線索則問 |
| 風格／皮膚 | 預設值 | 不問，用該 skill 預設或凍結版型，複述時講明；使用者可在滿意度迴圈改 |
| 交付格式 | 預設值 | 用該 skill 標準組合，不問 |

三欄的判準：**必問**＝答錯整份重做的項目；**可推斷**＝答錯要局部返工、但語意常帶線索的項目；**預設值**＝事後可低成本調整的項目。低階模型只需回答一件事：這個項目答錯的返工成本是哪一級。

流程：

```text
（步驟 0，透明）靜默完成環境準備，不要求使用者手動跑指令，安裝留 log。
（步驟 1）按決策表收集「必問」項；「可推斷」有線索則採用。
（步驟 2）把對焦結果（含推斷項與預設項）用一句話複述，得到同意才動工。
```

卡片／知識牆型：先講好「欄位與視覺型別」或先做「結構盤點（分區清單＋每區卡型）」，停下確認後才生。**嚴禁拿到主題就直接生。**

---

## 5. 能力邊界＋降級階梯（文件模板＋程式範式）

SKILL.md 段落：

```markdown
## 能力邊界（先講清楚，別硬做）
做得到：<結構化、可驗證、向量／可內嵌的產出>。
做不到（界外）：AI 生成插畫／照片（來源無法驗證、授權問題）、水彩手繪、bespoke 插畫。
要圖請放使用者自備或公眾領域素材。
```

降級階梯（缺料不留空洞，完整可複製實作，dex 五階：smiles→katex→icon→image→glyph）：

```python
LADDER = ["smiles", "katex", "icon", "image", "glyph"]   # 由高到低
SUBJECT_DEFAULT = {"chemistry": "smiles", "math": "katex", "biology": "icon"}

def _available(kind, value):
    """該階的料到不到位：套件裝得起來、檔案存在、字串非空。"""
    if kind == "smiles":
        try:
            import bootstrap; bootstrap.ensure_chem()
            import rdkit  # noqa: F401
            return bool(value)
        except Exception:
            return False
    if kind == "image":
        import os
        return bool(value) and os.path.exists(value)
    if kind == "glyph":
        return True                      # 最終階永遠可用
    return bool(value)

def resolve_visual(card, subject):
    """宣告型別優先；沒宣告依學科預設；逐階降級，最終一律到字形大字。"""
    declared = card.get("visual_type")
    start = declared or SUBJECT_DEFAULT.get(subject, "icon")
    idx = LADDER.index(start) if start in LADDER else 2
    for kind in LADDER[idx:]:
        value = card.get(kind) or card.get("visual_value")
        if _available(kind, value):
            if declared and kind != declared:
                print(f"[degrade] {declared} 缺料，降級為 {kind}")   # 誠實留痕
            return kind, (value if kind != "glyph" else card.get("glyph", "▣"))
    return "glyph", "▣"                  # 理論上到不了這行，保險
```

原則：每次降級**留 log**（房規五的誠實延伸到程式行為）；`glyph` 是無條件保底，所以流程永遠有輸出、永遠不留空洞、永遠不硬造。

數值真實度：不確定一律標「（需查證）」，絕不編造。

---

## 6. 回歸測試骨架（tests/test_*.py，cornell 風格）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：<skill>。執行：python tests/test_xxx.py
不需重相依（純邏輯與凍結契約即可測；重相依只測缺料降級分支）。"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

PASS = 0; FAIL = 0
def check(name, cond):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  [PASS] {name}")
    else:    FAIL += 1; print(f"  [FAIL] {name}")

# 1) 凍結契約守門
import kcg
check("joan-coral bg 凍結值", kcg.SKINS["joan-coral"]["bg"] == "#E8856E")
# 2) 引擎可獨立算繪（煙霧測試）
# 3) 缺料降級分支
# 4) 驗證守則（subprocess 跑 validate_punct，乾淨過、髒的擋）

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
```

原則：能在沒裝 rdkit／playwright／chromium 下跑的部分，全部寫成測試；重相依只測「缺料降級」分支。凍結契約一定寫成斷言。

---

## 7. 三種模式（每支 SKILL.md 收尾段，沿用 course-handout 心法）

```markdown
## 三種模式
- 套用：指名既有版型／皮膚，穩定批量。
- 探索：換配色／版型／密度，給不同調性，重做到滿意。
- 模仿：上傳一份喜歡的參考，抽色票與版面凍結成新版型（插畫不模仿）。
每次交付後問是否滿意，不滿意給方向重生。
```

---

## 8. 自動安裝 bootstrap（ensure 在 import 之前）

**正本檔：本包 `assets/bootstrap.py`（列於 manifest，可由 sync 同步）**。每包一支 `scripts/bootstrap.py`，分顆粒 `ensure_*`，偵測缺哪個裝哪個、裝過秒跳過、**每次實際安裝必留 log**：

```python
import importlib.util, os, subprocess, sys
def _have_py(m): return importlib.util.find_spec(m) is not None
def _have_npm(p): return os.path.isdir(os.path.join(os.getcwd(), "node_modules", p))
def _pip(*pkgs): subprocess.run([sys.executable,"-m","pip","install","--break-system-packages","-q",*pkgs], check=True)
def _npm(*pkgs): subprocess.run(["npm","install","--silent",*pkgs], check=True)

def ensure_export(log=print):
    if not _have_py("playwright"):
        log("[bootstrap] 安裝 playwright…"); _pip("playwright")
        subprocess.run([sys.executable,"-m","playwright","install","chromium"], check=True)
    if not _have_py("PIL"): _pip("pillow")

def ensure_katex(log=print):
    if not _have_npm("katex"): log("[bootstrap] 安裝 katex…"); _npm("katex")
```

**關鍵接線**：頂層 `from playwright import …` 在套件缺席時會直接 ImportError，所以 ensure 要在 import 之前：

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap; bootstrap.ensure_export()   # 先補齊，再 import
from playwright.sync_api import sync_playwright
```

node 腳本（如 build_katex.js）內也可自我補：`require.resolve('katex')` 失敗就 `execSync('npm install --silent katex')` 再解析，並避免寫死絕對路徑。

---

## 9. 自動驗證（回歸自測，不觸發真實安裝）

`tests/test_*.py`，cornell 風格的 `check()` 計數，重點測三類：① 純邏輯 ② 凍結契約斷言 ③ 自動安裝邏輯（攔截 `_pip`／subprocess，只驗分支，不真的裝）：

```python
import types
import bootstrap
calls = []
bootstrap._pip = lambda *p: calls.append(p)                       # 攔截，不真的 pip
bootstrap.subprocess = types.SimpleNamespace(run=lambda *a, **k: None)  # 攔截 chromium 安裝

bootstrap._have_py = lambda m: True
calls.clear(); bootstrap.ensure_export(log=lambda *a: None)
check("相依已在 → 不重裝", calls == [])

bootstrap._have_py = lambda m: False
calls.clear(); bootstrap.ensure_export(log=lambda *a: None)
check("相依缺少 → 嘗試安裝", len(calls) >= 1)

# 凍結契約守門
check("joan-coral bg 凍結值", SKINS["joan-coral"]["bg"] == "#E8856E")
```

驗證守則本身也測（subprocess 跑 validate_punct：乾淨過、髒的擋、破折號擋）。

---

## 10. 凍結可擴充版型庫（registry ＋ FROZEN ＋ 向後相容）

把版型／皮膚做成具名 registry，預設不破壞既有產出：

```python
DEFAULTS = dict(paper="#ffffff", ink="#222222", muted="#8a877e")  # ＝舊視覺，沒指定皮膚就維持原樣
SKINS = {
    "joan-ink": dict(accent="#B5462F", paper="#ffffff", ink="#2a2320"),  # 凍結 FROZEN
    "slate":    dict(accent="#3A5A78"),                                   # 可調
}
FROZEN = {"joan-ink"}

def resolve(skin_name):
    tok = dict(DEFAULTS)
    sk = SKINS.get(skin_name or "")
    if sk:
        tok.update({k: v for k, v in sk.items() if k != "accent"})
        tok["accent"] = sk.get("accent")
    return tok
```

解析順序：`spec["accent"]`（明確覆寫）＞ `SKINS[skin]["accent"]` ＞ 學科／預設色。擴充＝加一組 token；凍結項寫進 `FROZEN` 與 `FROZEN.md`，並用測試斷言守門（第 9 段）。kmap 則用 `scripts/preset_*.py` 每支一個 `render_*` 函式當凍結版型。凍結不能只靠「記得寫斷言」，程式級守門見第 11 段。

---

## 11. 凍結雜湊守門（不依賴人工記得寫斷言）

FROZEN 若只是慣例標記，忘了寫測試斷言就形同虛設。做法：把凍結項序列化後取雜湊，存進 `FROZEN.md`，啟動或測試時自動比對：

```python
import hashlib, json

def frozen_digest(skins, frozen):
    """對 FROZEN 集合內的 token 算穩定雜湊。"""
    payload = {k: skins[k] for k in sorted(frozen)}
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]

EXPECTED = "放進 FROZEN.md 記錄的定版雜湊"

def assert_frozen(skins, frozen):
    got = frozen_digest(skins, frozen)
    if got != EXPECTED:
        raise RuntimeError(
            f"凍結契約被動到（雜湊 {got} ≠ 定版 {EXPECTED}）。"
            "要改視覺請另開新具名項並進 major，不動凍結項。")
```

接線：`tests/test_*.py` 第一條測試就呼叫 `assert_frozen`；引擎主流程啟動時也呼叫一次（成本近零）。這樣就算沒人寫個別色票斷言，任何對凍結項的改動都會在第一時間紅燈。`FROZEN.md` 每版記一行定版雜湊。
