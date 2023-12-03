"""
https://adventofcode.com/2023/day/3

--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

from typing import List, Tuple


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
    engine: List[List[str]], n_rows: int, n_cols: int, coords_to_check: List[Tuple[int, int]]
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
                    return True
    return False


def main():
    engine = fill_engine()
    starts = []
    n_rows = len(engine)
    n_cols = len(engine[0])

    for row in range(n_rows):
        for col in range(n_cols):
            if (col == 0 and engine[row][col].isdigit()) or (
                col > 0 and engine[row][col].isdigit() and not (engine[row][col - 1].isdigit())
            ):
                starts.append((row, col))

    part_numbers = []
    for row_start, col_start in starts:
        col = col_start
        number = ""
        coords_to_check = []
        while col < n_cols and engine[row_start][col].isdigit():
            number += engine[row_start][col]
            coords_to_check.append((row_start, col))
            col += 1
        if check_symbols(engine, n_rows, n_cols, coords_to_check):
            part_numbers.append(int(number))

    print(sum(part_numbers))


if __name__ == "__main__":
    main()
