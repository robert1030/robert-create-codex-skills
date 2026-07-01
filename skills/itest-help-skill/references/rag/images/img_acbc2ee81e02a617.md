---
{
  "image_chunk_id": "img_acbc2ee81e02a617",
  "image_path": "topics/images/tc_steps_rightClickMenuOption-EditCommand.png",
  "category": "screenshot",
  "dimensions": [
    594,
    564
  ],
  "ocr_status": "ok",
  "has_ocr_text": true,
  "referenced_by": [
    "topics/test_case_editor_editing_steps.htm"
  ],
  "usage_count": 1
}
---

# Image: topics/images/tc_steps_rightClickMenuOption-EditCommand.png

- category: screenshot
- dimensions: (594, 564)
- ocr_status: ok
- referenced_by: topics/test_case_editor_editing_steps.htm

此圖片分類為畫面截圖（screenshot），已使用 Tesseract OCR（英文語言包）擷取圖片內文字，內容如下（OCR 結果，非人工校對，可能含辨識誤差，尤其是低解析度或特殊字元）：

```
S Edit Command

Command: [F This Python script demonstrates how to generate alist of prime numbers within a given

+ Define the range of numbers to check for primality
start=1
end = 100

+ Initialize an empty list to store prime numbers,
prime_numbers = []

+ Loop through each number in the specified range.
for num in range(start, end + 1)
+ Skip numbers less than 2, since 1 is not a prime number
if num <2:
continue
+# Assume the number is prime until proven otherwise
is prime = True

+ Check divisibility by all numbers from 2 to num-1
for iin range(2, num):
if num %i == 0:
# If divisible it's not a prime number
is prime = False
break # No need to check further

# If the number is still marked as prime, add itto the list
ifis_prime:
prime_numbers.append(num)

+ Display the result
print(’Prime numbers from 1 to 100 a.
```
