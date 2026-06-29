# 標準片段（可直接複製到新 skill）

每段都是從 Joan（酒 Ann）五包抽出的、已驗證可用的範式。複製後依該 skill 調整命名即可。

---

## 1. 版號戳記（五包統一格式，放 SKILL.md H1 正下方）

```markdown
# <Skill 顯示名稱>

> **vX.Y｜YYYY-MM-DD**：<這一版做了什麼，一句話>。
```

升級規則：版型／引擎不動、只改驗證或文件 → 進 patch（如 v2.1 → v2.1.1）；新增功能 → 進 minor（v1.0 → v1.1）；動到凍結版面 → 另開新版本並更新 FROZEN.md。

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

## 3. bootstrap 授權式安裝（唯讀偵測、冪等、隔離環境優先）

```python
import importlib.util, subprocess, sys

def _pip(*pkgs, break_system=False):
    cmd = [sys.executable, "-m", "pip", "install", "-q", *pkgs]
    if break_system:
        cmd.insert(5, "--break-system-packages")
    subprocess.run(cmd, check=True)

def plan_tools(spec=None):
    """唯讀偵測缺少項目，只回傳計畫，不安裝。"""
    need = []
    if importlib.util.find_spec("playwright") is None:
        need.append("playwright")
    return need

def ensure_tools(spec=None, authorized=False, break_system=False):
    """取得授權後才安裝；未授權只回報缺少項目。"""
    need = plan_tools(spec)
    if need and not authorized:
        return {"ok": False, "missing": need, "needs_authorization": True}
    if need:
        _pip(*need, break_system=break_system)
    return {"ok": True, "missing": []}
```

shell 版（setup.sh）務必冪等：已備妥則秒過。會寫入環境或下載相依前，必須先列出影響範圍並取得使用者授權。

---

## 4. 生成前對焦閘門（開場模板）

依 skill 性質剪裁。教學文件型：

```text
（步驟 0，透明）靜默完成環境準備，不要求使用者手動跑指令。
（必問，最先）輸出語言：中文／英文／雙語。
（必問，次之）對象學齡或受眾層級。
（依主線追問）方向與深度、範圍、風格。能從語意判斷的就不問。
→ 把對焦結果用一句話複述，得到同意才動工。
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

降級階梯（缺料不留空洞）：

```python
def resolve_visual(card, subject):
    # 宣告型別優先；沒宣告就依學科預設；最終一律可降級到字形大字
    ...

def render_image(value):
    if not _exists(value):
        return _glyph_fallback("▣")   # 缺料降級，不留醜空洞
    ...
```

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

## 8. 授權式 bootstrap（ensure 在 import 之前）

每包一支 `scripts/bootstrap.py`，分顆粒 `ensure_*`。先唯讀偵測，取得授權後才安裝，裝過秒跳過：

```python
import importlib.util, os, subprocess, sys
def _have_py(m): return importlib.util.find_spec(m) is not None
def _have_npm(p): return os.path.isdir(os.path.join(os.getcwd(), "node_modules", p))
def _pip(*pkgs, break_system=False):
    cmd=[sys.executable,"-m","pip","install","-q",*pkgs]
    if break_system: cmd.insert(5,"--break-system-packages")
    subprocess.run(cmd, check=True)
def _npm(*pkgs): subprocess.run(["npm","install","--silent",*pkgs], check=True)

def ensure_export(log=print, authorized=False, break_system=False):
    missing=[]
    if not _have_py("playwright"): missing.append("playwright")
    if not _have_py("PIL"): missing.append("pillow")
    if missing and not authorized:
        return {"ok": False, "missing": missing, "needs_authorization": True}
    if "playwright" in missing:
        log("[bootstrap] 安裝 playwright…"); _pip("playwright", break_system=break_system)
        subprocess.run([sys.executable,"-m","playwright","install","chromium"], check=True)
    if "pillow" in missing: _pip("pillow", break_system=break_system)
    return {"ok": True, "missing": []}

def ensure_katex(log=print, authorized=False):
    if not _have_npm("katex") and not authorized:
        return {"ok": False, "missing": ["katex"], "needs_authorization": True}
    if not _have_npm("katex"): log("[bootstrap] 安裝 katex…"); _npm("katex")
    return {"ok": True, "missing": []}
```

**關鍵接線**：頂層 `from playwright import …` 在套件缺席時會直接 ImportError，所以 ensure 要在 import 之前：

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap; bootstrap.ensure_export(authorized=True)   # 已取得授權後才補齊，再 import
from playwright.sync_api import sync_playwright
```

node 腳本（如 build_katex.js）內不得未授權自我安裝。`require.resolve('katex')` 失敗時先回報缺少項目；取得授權後才 `npm install --silent katex`，並避免寫死絕對路徑。

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

解析順序：`spec["accent"]`（明確覆寫）＞ `SKINS[skin]["accent"]` ＞ 學科／預設色。擴充＝加一組 token；凍結項寫進 `FROZEN` 與 `FROZEN.md`，並用測試斷言守門（第 9 段）。kmap 則用 `scripts/preset_*.py` 每支一個 `render_*` 函式當凍結版型。
