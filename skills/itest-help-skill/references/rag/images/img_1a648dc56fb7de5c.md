---
{
  "image_chunk_id": "img_1a648dc56fb7de5c",
  "image_path": "topics/images/fr_tcl_query_json_without_rm.png",
  "category": "screenshot",
  "dimensions": [
    1138,
    122
  ],
  "ocr_status": "ok",
  "has_ocr_text": true,
  "referenced_by": [
    "topics/field_replacements.6.htm"
  ],
  "usage_count": 1
}
---

# Image: topics/images/fr_tcl_query_json_without_rm.png

- category: screenshot
- dimensions: (1138, 122)
- ocr_status: ok
- referenced_by: topics/field_replacements.6.htm

此圖片分類為畫面截圖（screenshot），已使用 Tesseract OCR（英文語言包）擷取圖片內文字，內容如下（OCR 結果，非人工校對，可能含辨識誤差，尤其是低解析度或特殊字元）：

```
|) comment XPATH with substitution

@ eval set zone_query [format "mapped/Json/L3_Domains/item\[name=%s\]/domain/zones/item/name" $d]
( comment Query on stored response using substitution

@ eval set zones [query json_data $zone_query]
```
