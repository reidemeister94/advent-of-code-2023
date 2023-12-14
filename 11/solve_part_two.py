"""
https://adventofcode.com/2023/day/11#part2

--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

"""


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    empty_rows = []
    empty_cols = []
    for i, line in enumerate(lines):
        if "#" not in line:
            empty_rows.append(i)

    for i in range(len(lines[0])):
        if "#" not in [line[i] for line in lines]:
            empty_cols.append(i)

    points = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                points.append((i, j))

    expand_increment = 1000000
    distance_map = {}
    for i, (start_row, start_col) in enumerate(points):
        for j, (end_row, end_col) in enumerate(points[i + 1 :]):
            distance = 0
            for row in range(min(start_row, end_row), max(start_row, end_row)):
                distance += expand_increment if row in empty_rows else 1
            for col in range(min(start_col, end_col), max(start_col, end_col)):
                distance += expand_increment if col in empty_cols else 1

            distance_map[((start_row, start_col), (end_row, end_col))] = distance

    print(sum(distance_map.values()))


if __name__ == "__main__":
    main()
