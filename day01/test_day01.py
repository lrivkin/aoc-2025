from unittest import TestCase
from pathlib import Path

def read_input(file: str):
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def part_2(file):
    input = read_input(file).splitlines()

    num_zeros = 0

    position = 50
    for line in input:
        line = line.strip()

        dir = line[0]
        num = int(line[1:])

        for _ in range(num):
            if dir == 'L':
                position -= 1

            elif dir == 'R':
                position += 1
            else:
                raise ValueError()
            
            if position % 100 == 0:
                num_zeros += 1

    return num_zeros

class Test(TestCase):
    def test_part1(self):
        pass

    def test_part2_real(self):
        # 6530 = correct answer
        print(part_2("input.txt"))

    def test_part2(self):
        self.assertEqual(6, part_2("test.txt"))