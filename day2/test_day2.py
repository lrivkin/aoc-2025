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
    def is_invalid_p1(num: str) -> bool:
        if len(num) % 2 != 0:
            return False
        mid = int(len(num)/2)
        return num[0:mid] == num[mid:]
    
    @staticmethod
    def is_invalid_p2(num: str) -> bool:
        if len(num) % 2 != 0:
            return False
        mid = int(len(num)/2)
        return num[0:mid] == num[mid:]

    def find_invalid_ids(self, part: int=1) -> list[int]:
        is_invalid = self.is_invalid_p1 if part == 1 else self.is_invalid_p2
        results = []
        for i in range(int(self.low), int(self.high)+1):
            if is_invalid(str(i)):
                results.append(i)
        return results



def parse_input(input: str) -> list[Range]:
    ranges: list[Range] = []
    for line in input.split(","):
        low, high = line.split("-")
        ranges.append(Range(low=low, high=high))

    return ranges

def solve_problem(file, part=1) -> int:
    input_raw = read_input(file)
    input = parse_input(input_raw)
    ans = 0
    for r in input:
        for i in r.find_invalid_ids(part):
            ans += i

    return ans


class TestDay2(TestCase):
    def test_is_invalid(self):
        self.assertFalse(Range.is_invalid_p1('101'))
        self.assertTrue(Range.is_invalid_p1('11'))
        self.assertTrue(Range.is_invalid_p1('22'))
        self.assertTrue(Range.is_invalid_p1('1188511885'))
        self.assertTrue(Range.is_invalid_p1('38593859'))

    def test_part1(self):
        self.assertEqual(1227775554, solve_problem("test.txt", 1))

    def test_part1_real(self):
        print(solve_problem("input.txt", 1))

    def test_is_invalid_p2(self):
        for case in [12341234, 123123123, 1212121212, 1111111]:
            self.assertTrue(Range.is_invalid_p2(str(case)), f"Expected {case} to be a bad id")
        self.assertFalse(Range.is_invalid_p2('101'))
        self.assertTrue(Range.is_invalid_p2('11'))
        self.assertTrue(Range.is_invalid_p2('22'))
        self.assertTrue(Range.is_invalid_p2('1188511885'))
        self.assertTrue(Range.is_invalid_p2('38593859'))

    def test_part2(self):
        self.assertEqual(4174379265, solve_problem("test.txt", 2))

    def test_part2_real(self):
        print(solve_problem("input.txt", 2))