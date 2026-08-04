#!/usr/bin/env python3
"""Create the deterministic EAN-13 decoder control fixture used by image tests."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


VALUE = "5901234123457"
L_PATTERNS = {
    "0": "0001101", "1": "0011001", "2": "0010011", "3": "0111101", "4": "0100011",
    "5": "0110001", "6": "0101111", "7": "0111011", "8": "0110111", "9": "0001011",
}
G_PATTERNS = {
    "0": "0100111", "1": "0110011", "2": "0011011", "3": "0100001", "4": "0011101",
    "5": "0111001", "6": "0000101", "7": "0010001", "8": "0001001", "9": "0010111",
}
R_PATTERNS = {digit: "".join("1" if bit == "0" else "0" for bit in pattern) for digit, pattern in L_PATTERNS.items()}
FIRST_DIGIT_PARITY = {
    "0": "LLLLLL", "1": "LLGLGG", "2": "LLGGLG", "3": "LLGGGL", "4": "LGLLGG",
    "5": "LGGLLG", "6": "LGGGLL", "7": "LGLGLG", "8": "LGLGGL", "9": "LGGLGL",
}


def encoded_bits(value: str) -> str:
    if len(value) != 13 or not value.isdigit():
        raise ValueError("ean13_value_must_have_13_digits")
    left = "".join(
        (L_PATTERNS if parity == "L" else G_PATTERNS)[digit]
        for digit, parity in zip(value[1:7], FIRST_DIGIT_PARITY[value[0]])
    )
    right = "".join(R_PATTERNS[digit] for digit in value[7:])
    return f"101{left}01010{right}101"


def create_fixture(path: Path) -> None:
    scale = 2
    quiet_zone = 12
    height = 280
    bits = encoded_bits(VALUE)
    image = Image.new("RGB", ((len(bits) + quiet_zone * 2) * scale, height), "white")
    draw = ImageDraw.Draw(image)
    guard_indexes = set(range(3)) | set(range(45, 50)) | set(range(92, 95))
    for index, bit in enumerate(bits):
        if bit == "1":
            bottom = 215 if index in guard_indexes else 190
            draw.rectangle(
                ((quiet_zone + index) * scale, 25, (quiet_zone + index + 1) * scale - 1, bottom),
                fill="black",
            )
    draw.text((quiet_zone * scale, 222), VALUE, fill="black", font=ImageFont.truetype("arial.ttf", 28))
    image.save(path)


if __name__ == "__main__":
    create_fixture(Path(__file__).with_name("barcode-ean13.png"))
