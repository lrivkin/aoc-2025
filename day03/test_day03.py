from unittest import TestCase
from pathlib import Path

def joltage(input: str) -> int:
    biggest = max(input[:len(input)-1])
    biggest_idx = input.index(biggest)

    next_biggest = max(input[biggest_idx+1:])
    return int(biggest+next_biggest)

def part_1(file):
    p = Path(__file__).with_name(file)
    with open(p) as f:
        ans = 0
        for line in f.readlines():
            ans += joltage(line.strip())

        return ans
    return 0

def part_2(file):
    return 0


class Test(TestCase):
    def test_joltage(self):
        test_cases = [("987654321111111", 98),
                      ("811111111111119", 89),
                      ("234234234234278", 78),
                      ("818181911112111", 92)]

        for input, result in test_cases:
            with self.subTest(f"{input}"):
                self.assertEqual(joltage(input), result)

    def test_part1(self):
        self.assertEqual(357, part_1("test.txt"))

    def test_run_part1(self):
        # Result: 17332
        print(part_1("input.txt"))

    def test_part2(self):
        pass