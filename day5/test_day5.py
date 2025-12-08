from unittest import TestCase
from pathlib import Path
from dataclasses import dataclass

def read_input(file: str) -> str:
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def parse_input(file):
    input = read_input(file)
    ranges_in, ingredients_in = input.split("\n\n")

    ranges: list[list[int, int]] = []

    for r in ranges_in.splitlines():
        low, high = r.split("-")
        ranges.append([int(low), int(high)])

    ingredients: list[int] = []
    for i in ingredients_in.splitlines():
        ingredients.append(int(i))

    ranges = sorted(ranges, key=lambda x: x[0])
    return ranges, ingredients

def part_1(file: str):
    ranges, ingredients = parse_input(file)

    ans = 0
    for i in ingredients:
        for low, high in ranges:
            if i >= low and i <= high:
                ans += 1
                break

    return ans

def part_2(file: str):
    ranges, _ = parse_input(file)
    ans = 0
    max_seen = 0
    for low, high in ranges:
        if max_seen > high:
            # this whole range has already been covered
            continue
        if max_seen > low:
            low = max_seen + 1

        ans += high-low+1
        max_seen = max(max_seen, high)



    return ans

class TestDay5(TestCase):
    def test_part_1(self):
        self.assertEqual(3, part_1("test.txt"))

    def test_part_1_real(self):
        print(part_1("input.txt"))

    def test_part_2(self):
        self.assertEqual(14, part_2("test.txt"))

    def test_part_2_real(self):
        # 348115621205555 - too high
        print(part_2("input.txt"))
