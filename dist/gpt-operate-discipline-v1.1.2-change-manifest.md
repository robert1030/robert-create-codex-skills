# gpt-operate-discipline v1.1.2 Change Manifest

## Artifact identity

- Baseline ZIP SHA-256：`e7f74c8394d9717e435d0ea64a7c9a25f89e743cea092cefb433ad9f4985ff78`
- Release ZIP SHA-256：`9e56a311c21ae4ac2db2187a0588f96bb28163914015d90a8afd3efe477f6301`
- 所有正式文字檔：UTF-8 without BOM、LF。
- v1.0 八節與五題／路由 hash：未變。

## File changes

| Relative path | Purpose | Frozen impact | Before SHA-256 | After SHA-256 | Encoding／newline | Test coverage |
| --- | --- | --- | --- | --- | --- | --- |
| `SKILL.md` | 加入 v1.1.2 入口、兩個 direct references 與能力邊界 | Frozen block 未改；八節／五題 hash PASS | `3b65f0205cf7ab647f62ddda6eb5e1d36423e60253cd4c2cfee803dced3b227f` | `e0e827be7c37da555af59e530caad3543f4622f457af80e2346e2c6f931cfcbc` | UTF-8 no BOM／LF | Freeze、v1.1、trigger、reference reachability、version |
| `FROZEN.md` | 追加 v1.1.2 增量與 hash 紀錄 | Append-only；既有 frozen text 未改 | `8c2e6c5d01a3de26d986d1351306918985528a0697b42d725d45d837d4678d87` | `a31ac1855b916b7615556d3ccbbc5e4f17f321f39155727b09426d3f22b1a61a` | UTF-8 no BOM／LF | Frozen hash、version record |
| `REBUILD.md` | 記錄重建、Runtime、encoding 與驗證要求 | 無 frozen text 影響 | `d1699b2216a5ae9135dc79a6d72f882e9524b3f342409b6fd8e06792507b5472` | `ddb48a55d489dbf89c0a838f52c02b7f121dba648217d3e6e1d010f304f0bf0b` | UTF-8 no BOM／LF | Encoding、package whitelist、reference reachability |
| `agents/openai.yaml` | 對齊官方 optional metadata，只保留必要 UI／policy 欄位 | 無 frozen text 影響 | `8dd7b3e99cce83503d742eb84d9680a6792a897ff6314b3e2c7b3eeca528f42b` | `a6aa4cc6adf5ba36193afa3340aecdd3c14058dca3595cb00e16dca956a9d00f` | UTF-8 no BOM／LF | Exact allowlist、description 25 至 64 chars、no dependencies |
| `references/critical-review.md` | 六核心、Conditional 7／8／9、分級、反表演式規則 | 新增層，不取代 frozen／v1.1 | N/A | `fa45232e943b1fd862277263b81c200488e0095337fcaf2191f3d68d2e8afd5e` | UTF-8 no BOM／LF | Exact six questions、C01 至 C10、N01 至 N10、conditional-only |
| `references/runtime-adaptation.md` | Capability-first inventory、fallback 與 R01 至 R04 行為契約 | 無 frozen text 影響 | N/A | `44f63f04407fd55e36b795405df0f026eaed32858a504f9e0da2c4411f9dd1e1` | UTF-8 no BOM／LF | Exact behavior assertions、四個 mutation、platform boundary |
| `scripts/validate_punct.py` | Strict UTF-8／BOM／CP950 reader、explicit override、ambiguous rejection | Validator 增強，未弱化 frozen expectations | `9751d2a6e7c0762c4c995cf0e42712a3527b7e4d3964fe3ec2aebaf103785cc2` | `8512aa31813c9a838e740aeca496c1a78532727bf8c37c1012bfebdc3d4d5af4` | UTF-8 no BOM／LF | UTF8、BOM、CP950、CRLF、invalid、ambiguous、Windows／WSL |
| `tests/acceptance_cases.md` | 保留 A01 至 A08，加入 C01 至 C10、N01 至 N10、R01 至 R04 | 原案例未刪除或弱化 | `44219c8ea6165301b198438855a968da172d190f709e4ca25943bd10e23f6138` | `1b8c9df1d9db83471835dbce0e1db05420c31db38b1d6cd0668b43be9cfb54d0` | UTF-8 no BOM／LF | Acceptance marker exact assertions |
| `tests/test_discipline.py` | 完整 freeze、critical、Runtime、encoding、metadata、security、package regression | 既有 hash expectations 未改；新增 gates | `8de3cadd5b9a00ac81779ba61e79bfbf490227c9413f258f59d7187c222ec328` | `bb0ac444f79e49d256f182b05836f69d26e2b6001f2a40021e02099c97ff9ed2` | UTF-8 no BOM／LF | Windows、CP950 outer、WSL2、mutation、negative、package whitelist |

## Scope summary

- Modified：7 files。
- Added：2 files。
- Removed：0 files。
- Formal ZIP 不含 work harness、logs、temporary fixtures、`__pycache__`、`.pyc`、nested archives、virtual environments 或 OS metadata junk。
- 正式 ZIP 9 個檔案均與最後驗證過的 staging 逐位元一致。

