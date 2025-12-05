from unittest import TestCase
import unittest
from pathlib import Path
from dataclasses import dataclass

def read_input(file: str) -> str:
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

@dataclass
class Range:
    low: int = 0
    high: int = 0


def parse_input(input: str) -> list[Range]:
    ranges: list[Range] = []
    for line in input.split(","):
        low, high = line.split("-")
        ranges.append(Range(low=int(low), high=int(high)))

    return ranges

def part_1(file) -> int:
    input_raw = read_input(file)
    input = parse_input(input_raw)
    return -1

class TestDay2(TestCase):
    def test_part1(self):
        self.assertEqual(1227775554, part_1("test.txt"))

    def test_part1_real(self):
        part_1("input.txt")