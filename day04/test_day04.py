from unittest import TestCase
from pathlib import Path

def read_input(file: str):
    p = Path(__file__).with_name(file)

    with open(p) as f:
        return f.read()
    
def grid(file: str) -> list[list[str]]:
    input_lines = read_input(file).splitlines()
    grid: list[list[str]] = []
    for line in input_lines:
        g = []
        for c in line:
            g.append(c)
        grid.append(g)

    return grid

directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

def part_1(file: str) -> int:
    input = grid(file)
    return remove_paper(input)

def part_2(file: str) -> int:
    new_grid = grid(file)
    num_removed = 1
    result = 0
    i = 0

    while num_removed > 0:
        num_removed, new_grid = remove_paper(new_grid)
        print(f"round: {i}, removed: {num_removed}")
        result += num_removed
        i+=1

    print(f"result: {result}")
    return result


def remove_paper(input: list[list[str]]):
    result = 0
    new_grid = []
    for r in range(len(input)):
        new_row = []
        for c in range(len(input[0])):
            spot = input[r][c]
            if spot == '.':
                new_row.append('.')
                continue

            num_adj = 0

            for d0, d1 in directions:
                r_new, c_new = r+d0, c+d1
                if r_new >= 0 and r_new < len(input) and c_new >= 0 and c_new < len(input[0]):
                    if input[r_new][c_new] == '@':
                        num_adj += 1

            if num_adj < 4:
                result += 1
                new_row.append('.')
            else:
                new_row.append('@')
        new_grid.append(new_row)

    return result, new_grid

class Test(TestCase):
    def test_part1(self):
        part_1("test.txt")
        part_1("input.txt")

    def test_part2(self):
        part_2("test.txt")
        part_2("input.txt")
