# 標準片段（可直接複製到新 skill）

每段都是從 `joan-skill-conventions` 移植過來、依 Codex 平台調整過的範式。前七段和 Claude 版邏輯相同，第三、第六、第八、第九段是 Codex 改寫版；第十一段是 Codex 新增的外殼模板。複製後依該 skill 調整命名即可。

---

## 一、版號戳記（放 SKILL.md H1 正下方）

```markdown
# <Skill 顯示名稱>

> **vX.Y｜YYYY-MM-DD**：<這一版做了什麼，一句話>。
```

升級規則：版型／引擎不動、只改驗證或文件 → 進 patch（如 v2.1 → v2.1.1）；新增功能 → 進 minor（v1.0 → v1.1）；動到凍結版面 → 另開新版本並更新 `FROZEN.md`。

---

## 二、凍結契約（程式內標記＋帳本）

```python
SKINS = {
    "joan-coral": dict(  # 凍結 FROZEN，改色即破壞，不可隨意動
        bg="#E8856E", accent="#C75A41", qbg="#C75A41", barbg="#3a302d"),
    "joan-yellow": dict(),   # 可調
}
FROZEN = {"joan-coral"}
```

每包放一份 `FROZEN.md` 帳本，並在回歸測試裡把凍結值寫成斷言守門（見第九段）。

---

## 三、Codex 版 bootstrap 自動安裝（環境偵測，不寫死旗標）

```python
import importlib.util, os, subprocess, sys, sysconfig

def _is_externally_managed():
    return os.path.exists(os.path.join(sysconfig.get_path("stdlib"), "EXTERNALLY-MANAGED"))

def _in_virtualenv():
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)

def _pip_install(*pkgs, log=print):
    cmd = [sys.executable, "-m", "pip", "install", "-q", *pkgs]
    if _is_externally_managed() and not _in_virtualenv():
        cmd.insert(cmd.index("install") + 1, "--break-system-packages")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as exc:
        log(f"[bootstrap] 安裝失敗：{pkgs}（{exc}），請手動處理。")
        return False

def ensure(*modules, pip_names=None, log=print):
    pip_names = pip_names or {}
    missing = [m for m in modules if importlib.util.find_spec(m) is None]
    if not missing:
        return True
    log(f"[bootstrap] 偵測到缺少：{', '.join(missing)}，準備安裝…")
    return _pip_install(*(pip_names.get(m, m) for m in missing), log=log)
```

和 Claude 版的差異只有一件事：**先偵測環境是不是外部管理、有沒有在虛擬環境裡，再決定要不要加 `--break-system-packages`**，不是每次都無條件加。完整版見 `scripts/bootstrap.py`。

---

## 四、生成前對焦閘門（開場模板）

依 skill 性質剪裁。教學文件型：

```text
（步驟零，透明）靜默完成環境準備，不要求使用者手動跑指令。
（必問，最先）輸出語言：中文／英文／雙語。
（必問，次之）對象學齡或受眾層級。
（依主線追問）方向與深度、範圍、風格。能從語意判斷的就不問。
→ 把對焦結果用一句話複述，得到同意才動工。
```

卡片／知識牆型：先講好「欄位與視覺型別」或先做「結構盤點」，停下確認後才生。**嚴禁拿到主題就直接生。**

---

## 五、能力邊界＋降級階梯（文件模板＋程式範式）

```markdown
## 能力邊界（先講清楚，別硬做）
做得到：<結構化、可驗證、向量／可內嵌的產出>。
做不到（界外）：AI 生成插畫／照片（來源無法驗證、授權問題）、水彩手繪、bespoke 插畫。
要圖請放使用者自備或公眾領域素材。
```

```python
def render_image(value):
    if not _exists(value):
        return _glyph_fallback("▣")   # 缺料降級，不留醜空洞
    ...
```

數值真實度：不確定一律標「（需查證）」，絕不編造。

---

## 六、回歸測試骨架（tests/test_*.py）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：<skill>。執行：python tests/test_xxx.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

PASS = 0; FAIL = 0
def check(name, cond):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  [PASS] {name}")
    else:    FAIL += 1; print(f"  [FAIL] {name}")

# 一）凍結契約守門
import kcg
check("joan-coral bg 凍結值", kcg.SKINS["joan-coral"]["bg"] == "#E8856E")
# 二）引擎可獨立算繪（煙霧測試）
# 三）缺料降級分支
# 四）驗證守則（subprocess 跑 validate_punct，乾淨過、髒的擋）

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
```

原則：能在沒裝重相依下跑的部分，全部寫成測試；重相依只測「缺料降級」分支。凍結契約一定寫成斷言。

---

## 七、三種模式（每支 SKILL.md 收尾段）

```markdown
## 三種模式
- 套用：指名既有版型／皮膚，穩定批量。
- 探索：換配色／版型／密度，給不同調性，重做到滿意。
- 模仿：上傳一份喜歡的參考，抽色票與版面凍結成新版型（插畫不模仿）。
每次交付後問是否滿意，不滿意給方向重生。
```

---

## 八、Codex 版分顆粒 bootstrap（ensure 在 import 之前）

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap

if not bootstrap.ensure("playwright"):
    raise SystemExit("playwright 安裝失敗，請手動處理後再試一次。")
from playwright.sync_api import sync_playwright
```

**關鍵接線不變**：頂層 `from playwright import …` 在套件缺席時會直接 `ImportError`，所以 `ensure` 一定要在對應 `import` 之前呼叫。和 Claude 版唯一的差異是 `bootstrap.py` 內部多了環境偵測（見第三段），不是每次都無條件帶 `--break-system-packages`。

---

## 九、自動驗證（回歸自測，不觸發真實安裝）

```python
import types
import bootstrap
calls = []
bootstrap._pip_install = lambda *p, **k: calls.append(p) or True   # 攔截，不真的 pip
bootstrap.subprocess = types.SimpleNamespace(run=lambda *a, **k: None)

bootstrap._have_py = lambda m: True
calls.clear(); bootstrap.ensure("playwright")
check("相依已在 → 不重裝", calls == [])

bootstrap._have_py = lambda m: False
calls.clear(); bootstrap.ensure("playwright")
check("相依缺少 → 嘗試安裝", len(calls) >= 1)
```

驗證守則本身也測（subprocess 跑 `validate_punct.py`：乾淨過、髒的擋、破折號擋）。

---

## 十、凍結可擴充版型庫（registry ＋ FROZEN ＋ 向後相容）

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

解析順序：`spec["accent"]`（明確覆寫）＞ `SKINS[skin]["accent"]` ＞ 學科／預設色。擴充＝加一組 token；凍結項寫進 `FROZEN` 與 `FROZEN.md`，並用測試斷言守門（第九段）。

---

## 十一、Codex 外殼模板（`agents/openai.yaml`，Codex 新增）

```yaml
interface:
  display_name: "<人看的標題>"
  short_description: "<二十五至六十四字的一句話>"
  default_prompt: "使用 $<skill-name> <做什麼的一句話範例>"

policy:
  allow_implicit_invocation: true
```

`SKILL.md` frontmatter 只保留：

```yaml
---
name: <小寫字母數字連字號，六十四字以內，等同資料夾名>
description: "<一千零二十四字以內，含所有觸發情境，因為 body 只在觸發後才載入>"
---
```

`display_name`／版本號／icon 這類 UI 中繼資料一律不進 `SKILL.md` frontmatter，只進 `agents/openai.yaml`。
