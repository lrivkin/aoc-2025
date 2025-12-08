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



class Test(TestCase):
    def test_part1(self):
        part_1("test.txt")


    def test_part2(self):
        part_1("input.txt")