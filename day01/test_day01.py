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
        if dir == 'L':
            position -= num
        elif dir == 'R':
            position += num
        else:
            raise ValueError()
        
        if 0 <= position < 99:
            continue

        if position < 0:
            while position < 0:
                position += 100
                num_zeros += 1

        elif position >= 100:
            while position >= 100:
                position -= 100
                num_zeros += 1

    return num_zeros

class Test(TestCase):
    def test_part1(self):
        pass

    def test_part2_real(self):
        # 6536: not right? 
        print(part_2("input.txt"))

    def test_part2(self):
        self.assertEqual(6, part_2("test.txt"))