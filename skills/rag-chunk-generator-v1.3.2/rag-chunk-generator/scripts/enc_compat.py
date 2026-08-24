"""
enc_compat.py — token 編碼相容層（v1.1 新增）

tiktoken 的 cl100k_base BPE 檔要現場從 openaipublic 下載，離線或網域
受限的環境會拿到 403，整支切片器連帶掛掉。這裡把它包成降級階梯：

  1. tiktoken cl100k_base（精確，優先）
  2. 離線近似編碼器（CJK 一字一 token、拉丁字母每 4 字一 token、
     數字每 3 字一 token，其餘字元各自成 token）

第 2 階與真實 cl100k 對中文長文的偏差約 10～20%，僅供切片邊界與
統計參考。切片邊界與 overlap 仍精確可逆（encode／decode 互為反函式），
不會切壞字。降級時會印出一行告知，絕不靜默假裝是精確值。

用法：
    import enc_compat
    ENC = enc_compat.get_encoding()
    ENC.encode(text) / ENC.decode(ids) / ENC.name
"""
import re

_SEG = re.compile(
    r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]"  # CJK 與全形標點，一字一 token
    r"|[A-Za-z]{1,4}"                             # 拉丁字母每 4 字一 token
    r"|\d{1,3}"                                   # 數字每 3 字一 token
    r"|\s+"
    r"|."
)

_ANNOUNCED = False


class OfflineEncoding:
    """離線近似編碼器。encode／decode 可逆，供 overlap 切片使用。"""

    name = "offline_approx"

    def __init__(self) -> None:
        self._table: list[str] = []
        self._index: dict[str, int] = {}

    def _id(self, piece: str) -> int:
        i = self._index.get(piece)
        if i is None:
            i = len(self._table)
            self._table.append(piece)
            self._index[piece] = i
        return i

    def encode(self, text: str) -> list[int]:
        return [self._id(p) for p in _SEG.findall(text)]

    def decode(self, ids: list[int]) -> str:
        return "".join(self._table[i] for i in ids)


def get_encoding():
    """取得可用的編碼器：優先 tiktoken，失敗則降級離線近似編碼器。"""
    global _ANNOUNCED
    try:
        import tiktoken

        enc = tiktoken.get_encoding("cl100k_base")
        enc.encode("測試 test")  # BPE 檔要真的載得到才算數
        return enc
    except Exception as e:
        if not _ANNOUNCED:
            print(
                f"[enc_compat] 降級：tiktoken 不可用（{type(e).__name__}），"
                f"改用離線近似編碼器，token_count 有約 10～20% 偏差。",
                flush=True,
            )
            _ANNOUNCED = True
        return OfflineEncoding()


def is_exact(enc) -> bool:
    """這個編碼器是不是精確的 tiktoken。"""
    return getattr(enc, "name", "") != "offline_approx"
