from unittest import TestCase
from pathlib import Path

def read_input(file: str):
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()

def part_1(file):
    grid = []
    for line in read_input(file).splitlines():
        g_line = []
        for c in line:
            g_line.append(c)

        grid.append(g_line)

    row = 0
    col = 0
    for val in grid[row]:
        if val == 'S':
            row += 1
            break
        col += 1

    running = [col]

    splits = 0

    while row < len(grid):
        new_running = set()
        for idx in running:
            if grid[row][idx] == '.':
                new_running.add(idx)
            elif grid[row][idx] == '^':
                splits += 1
                if idx - 1 >= 0:
                    new_running.add(idx-1)
                if idx + 1 < len(grid[row]):
                    new_running.add(idx+1)

        running = new_running
        row += 1

    print(splits)
    return splits


class Test(TestCase):
    def test_part1(self):
        part_1("test.txt")
        part_1("input.txt")

    def test_part2(self):
        pass