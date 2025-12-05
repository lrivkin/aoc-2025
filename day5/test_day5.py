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

    for r in ranges_in.splitlines():
        low, high = r.split("-")
        fresh_ranges.update(range(int(low), int(high)+1))

    ans = 0
    for i in ingredients_in.splitlines():
        if int(i) in fresh_ranges:
            ans += 1
    return ans

class TestDay5(TestCase):
    def test_part_1(self):
        self.assertEqual(3, part_1("test.txt"))
