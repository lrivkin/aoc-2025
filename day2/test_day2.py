from unittest import TestCase
from pathlib import Path
from dataclasses import dataclass

def read_input(file: str) -> str:
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

@dataclass
class Range:
    low: str = ''
    high: str = ''

    @staticmethod
    def is_invalid(num: str) -> bool:
        if len(num) % 2 != 0:
            return False
        mid = int(len(num)/2)
        return num[0:mid] == num[mid:]
    
    def find_invalid_ids(self) -> list[int]:
        results = []
        for i in range(int(self.low), int(self.high)+1):
            if self.is_invalid(str(i)):
                results.append(i)

        return results



def parse_input(input: str) -> list[Range]:
    ranges: list[Range] = []
    for line in input.split(","):
        low, high = line.split("-")
        ranges.append(Range(low=low, high=high))

    return ranges

def part_1(file) -> int:
    input_raw = read_input(file)
    input = parse_input(input_raw)
    ans = 0
    for r in input:
        for i in r.find_invalid_ids():
            ans += i

    return ans

class TestDay2(TestCase):
    def test_is_invalid(self):
        self.assertFalse(Range.is_invalid('101'))
        self.assertTrue(Range.is_invalid('11'))
        self.assertTrue(Range.is_invalid('22'))
        self.assertTrue(Range.is_invalid('1188511885'))
        self.assertTrue(Range.is_invalid('38593859'))

    def test_part1(self):
        self.assertEqual(1227775554, part_1("test.txt"))

    def test_part1_real(self):
        print(part_1("input.txt"))