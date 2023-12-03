"""
https://adventofcode.com/2023/day/3#part2

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from typing import List, Tuple
from collections import defaultdict


def fill_engine() -> List[List[str]]:
    engine = []
    for line in open("input.txt", "r"):
        line = line.strip()
        engine_line = []
        for char in line:
            engine_line.append(char)
        engine.append(engine_line)
    return engine


def check_symbols(
    engine: List[List[str]],
    n_rows: int,
    n_cols: int,
    coords_to_check: List[Tuple[int, int]],
    asterisk_map: defaultdict,
) -> bool:
    for row, col in coords_to_check:
        for row_diff in range(-1, 2):
            for col_diff in range(-1, 2):
                if row_diff == 0 and col_diff == 0:
                    continue
                if (
                    row + row_diff >= 0
                    and row + row_diff < n_rows
                    and col + col_diff >= 0
                    and col + col_diff < n_cols
                    and not (engine[row + row_diff][col + col_diff]).isdigit()
                    and not (engine[row + row_diff][col + col_diff]) == "."
                ):
                    if engine[row + row_diff][col + col_diff] == "*":
                        asterisk_map[(row + row_diff, col + col_diff)].append(coords_to_check[0])
                    return True
    return False


def main():
    engine = fill_engine()
    starts = []
    n_rows = len(engine)
    n_cols = len(engine[0])
    gear_ratios = 0
    starts_map = {}

    for row in range(n_rows):
        for col in range(n_cols):
            if (col == 0 and engine[row][col].isdigit()) or (
                col > 0 and engine[row][col].isdigit() and not (engine[row][col - 1].isdigit())
            ):
                starts.append((row, col))

    part_numbers = []
    asterisk_map = defaultdict(list)
    for row_start, col_start in starts:
        col = col_start
        number = ""
        coords_to_check = []
        while col < n_cols and engine[row_start][col].isdigit():
            number += engine[row_start][col]
            coords_to_check.append((row_start, col))
            col += 1
        starts_map[(row_start, col_start)] = int(number)
        if check_symbols(engine, n_rows, n_cols, coords_to_check, asterisk_map):
            part_numbers.append(int(number))

    print(sum(part_numbers))
    for _, coords in asterisk_map.items():
        if len(coords) == 2:
            gear_ratios += starts_map[coords[0]] * starts_map[coords[1]]
    print(gear_ratios)


if __name__ == "__main__":
    main()
