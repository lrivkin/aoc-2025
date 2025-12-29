from unittest import TestCase
from pathlib import Path

def read_input(file: str):
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def part_2(input: list[str]) -> int:
    num_zeros = 0

    position = 50
    for line in input:
        line = line.strip()
        dir = line[0]
        num = int(line[1:])


        if dir == 'L':
            position = 100 - position
            position -= num

        elif dir == 'R':
            position += num

        if position == 0:
            num_zeros += 1

        elif position >= 100:
            while position >= 100:
                position -= 100
                num_zeros += 1

        elif position < 0:
            while position < 0:
                position += 100
                num_zeros += 1            
        else:
            pass


    return num_zeros

class Test(TestCase):
    def test_part1(self):
        pass

    def test_part2_real(self):
        input = read_input("input.txt").splitlines()
        # 6530 = correct answer
        self.assertEqual(6530, part_2(input))

    def test_part2(self):
        input = read_input("test.txt").splitlines()

        self.assertEqual(6, part_2(input))

    def test_part2_debug(self):
        want_one = [
            ["L50", "R50"],
            ["L50", "L50"],
            ["R50", "L50"],
            ["R50", "R50"]
        ]
        for test_case in want_one:
            with self.subTest(case=test_case) as t:
                self.assertEqual(1, part_2(test_case))