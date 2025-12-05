from unittest import TestCase
from pathlib import Path
from dataclasses import dataclass

def read_input(file: str) -> str:
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def part_1(file: str):
    input = read_input(file)
    ranges_in, ingredients_in = input.split("\n\n")
    fresh_ranges = set()

    ranges: list[tuple[int, int]] = []

    for r in ranges_in.splitlines():
        low, high = r.split("-")
        ranges.append((int(low), int(high)))

    ranges = sorted(ranges, key=lambda x: x[0])

    ans = 0
    for i in ingredients_in.splitlines():
        i = int(i)
        for low, high in ranges:
            if i >= low and i <= high:
                ans += 1
                break

    return ans

class TestDay5(TestCase):
    def test_part_1(self):
        self.assertEqual(3, part_1("test.txt"))

    def test_part_1_real(self):
        ans = part_1("input.txt")
        self.assertEqual(-1, ans)