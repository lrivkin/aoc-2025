from unittest import TestCase
from pathlib import Path

def joltage(input: str) -> int:
    max_val = input[0]
    second_max = input[len(input)-1]
    for i in range(1, len(input)-1):
        if input[i] > max_val:
            max_val = input[i]
            second_max = input[i+1]
        elif input[i] > second_max:
            second_max = input[i]
    return int(max_val + second_max)

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
        # Result: 17324
        # too low. Curiously, it's the right answer for someone else; you might be logged in to the wrong account or just unlucky
        print(part_1("input.txt"))

    def test_part2(self):
        pass