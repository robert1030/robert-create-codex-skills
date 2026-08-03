# itest-help dist 清單

產生日期：2026-08-03

## v1.3.1（現行版）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.1-runtime.zip` | 49 | 2.18 MB | `7BB8065D1D08858EF0923F2CA24A78E3F6F026515C6365241D88B468AB6DE6BC` |
| `itest-help-v1.3.1-chatweb.zip` | 48 | 1.15 MB | `FC319E44E042ED02949399F13B05E2CB9DF510F4A8271373B2E65350DC10521E` |
| `itest-help-v1.3.1-full.zip` | 9,378 | 18.79 MB | `8F434CAE21A208C001295767CBCDB94A984D9C1A61113370E4029B45E09B13A1` |

## v1.3.0

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.0-runtime.zip` | 49 | 2.18 MB | `72648C81BCA5CC992D6A80C0EBF4591BB859ED30DD976C3DBE3603E6F9C09836` |
| `itest-help-v1.3.0-chatweb.zip` | 48 | 1.15 MB | `352396B0D4686ABB05CBF9F86E35D3D69252A3364D343B9F2D05499C1C5FEBB9` |
| `itest-help-v1.3.0-full.zip` | 9,378 | 18.79 MB | `CD2746CF9E03314267E315194079C9F72C8A2B289E0347FFFC254614B8E714ED` |

## v1.1.0

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.1.0-runtime.zip` | 48 | 2.17 MB | `3ACE95FF4B4229F559557BAD33B1574BB1846F2CA4F9B319FF2CA4088B743C8D` |
| `itest-help-v1.1.0-chatweb.zip` | 47 | 1.14 MB | `1364EE88AF8D5AAE0DF59C51A097FA547AEA8581AD168F717B9DB4D060D5C278` |
| `itest-help-v1.1.0-full.zip` | 9,377 | 18.78 MB | `BC59EACFEDE31612EF47152A72D884DC2AC72CB87C71B7002DC6648883411DE6` |

## v1.0.0（原始封裝，不可刪除）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v26.2.0.zip` | 9,370 | 18.89 MB | `6EEB3CAD7DDC63B6F89BE7B434312141375EFEBA24D0E5CB2F257F4FAAC6A344` |

安裝請用 v1.3.1。

v1.2.0 的 dist 已由擁有者移除，來源樹保留於 `skills/itest-help-v1.2.0/`，需要時可重建。dist zip 不是權威副本，來源樹才是。

**`itest-help-v26.2.0.zip` 不可刪除**：v1.1.0 之後的來源樹都不含 `knowledge/rag/`，`full` profile 的 9,329 個 RAG 檔案是打包時自該檔串流產生。刪除後將無法再產生任何 `full` profile，完整 provenance 鏈驗證永久失效。

用途：`runtime` 供 Claude Code、Claude CLI、Codex CLI 與 Codex Desktop 安裝；`chatweb` 供 claude.ai 與 ChatGPT 的 Skills 上傳；`full` 供存證與完整 provenance 鏈驗證，請解壓到短路徑，不得放進 skill 目錄。
