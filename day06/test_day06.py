from unittest import TestCase
from dataclasses import dataclass
from pathlib import Path
import numpy as np


def part_1(filename):
    p = Path(__file__).with_name(filename)

    res = np.loadtxt(p, dtype=str)
    arr = np.transpose(res)
    operations = arr[:, -1]
    numbers = arr[:, :-1].astype(int)

    overall_ans = 0
    for idx, operation in enumerate(operations):
        if operation == "*":

            ans = 1
            for n in numbers[idx]:
                ans *= n
        elif operation == "+":

            ans = 0
            for n in numbers[idx]:
                ans += n
        else:
            pass
        overall_ans += ans

    print(overall_ans)
    return overall_ans


def part_2(filename):
    p = Path(__file__).with_name(filename)
    with open(p) as f:
        input_raw = f.read()
        lines = input_raw.splitlines()

        num_cols = len(lines[0])
        num_rows = len(lines)

        col = num_cols-1

        nums = []
        numbers = []
        operations = []
        while col >= 0:
            num = ""
            for row in range(num_rows-1):
                if lines[row][col] != " ":
                    num += lines[row][col]

            if num.strip() == "" or col == 0:
                if col == 0:
                    col = -1
                operations.append(lines[row+1][col+1])
                numbers.append(nums)
                nums = []

            else:
                nums.append(int(num))

            col -= 1

        overall_ans = 0
        for idx, operation in enumerate(operations):
            if operation == "*":

                ans = 1
                for n in numbers[idx]:
                    ans *= n

            elif operation == "+":
                ans = 0
                for n in numbers[idx]:
                    ans += n
            else:
                pass

            overall_ans += ans

        print(overall_ans)



class Test(TestCase):
    def test_part1(self):
        part_1("test.txt")

    def test_part1_real(self):
        part_1("input.txt")

    def test_part2(self):
        part_2("test.txt")

    def test_part2_real(self):
        part_2("input.txt")
