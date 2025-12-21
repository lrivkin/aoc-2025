from unittest import TestCase
from pathlib import Path

def read_input(file: str):
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def part_2(file):
    input = read_input(file).splitlines()

    start_pos = 50
    for line in input:
        if line[0] == 'L':
            pass
        elif[0] == 'R':
            pass
        else:
            raise ValueError()

    return -1

class Test(TestCase):
    def test_part1(self):
        self.assertEqual(6, part_2("test.txt"))

    def test_part2(self):
        pass