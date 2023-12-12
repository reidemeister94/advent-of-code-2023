"""
https://adventofcode.com/2023/day/10#part2

--- Part Two ---
You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?
"""


def fill_adj_matrix(grid: list[list[str]]):
    adj_matrix = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "-":
                adj_matrix[(i, j)] = [(i, j - 1), (i, j + 1)]
            elif grid[i][j] == "|":
                adj_matrix[(i, j)] = [(i - 1, j), (i + 1, j)]
            elif grid[i][j] == "L":
                adj_matrix[(i, j)] = [(i - 1, j), (i, j + 1)]
            elif grid[i][j] == "J":
                adj_matrix[(i, j)] = [(i - 1, j), (i, j - 1)]
            elif grid[i][j] == "7":
                adj_matrix[(i, j)] = [(i + 1, j), (i, j - 1)]
            elif grid[i][j] == "F":
                adj_matrix[(i, j)] = [(i + 1, j), (i, j + 1)]
    return adj_matrix


def main():
    grid = []
    for line in open("input.txt"):
        grid.append(list(line.strip()))

    adj_matrix = fill_adj_matrix(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
                break

    possible_start_value = {"-", "|", "L", "J", "7", "F"}
    max_steps = 0
    visited = set()
    visited.add((start[0], start[1]))
    queue = []
    for i in [-1, 1]:
        if (start[0] + i, start[1]) in adj_matrix:
            queue.append((start[0] + i, start[1], 1))
        if (start[0], start[1] + i) in adj_matrix:
            queue.append((start[0], start[1] + i, 1))

    while queue:
        curr_row, curr_col, curr_steps = queue.pop()
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        for row, col in adj_matrix[(curr_row, curr_col)]:
            if (row, col) == start:
                # understand the current direction
                if row == curr_row and col == curr_col - 1:
                    possible_start_value &= {"-", "L", "F"}
                elif row == curr_row and col == curr_col + 1:
                    possible_start_value &= {"-", "J", "7"}
                elif row == curr_row - 1 and col == curr_col:
                    possible_start_value &= {"|", "7", "F"}
                elif row == curr_row + 1 and col == curr_col:
                    possible_start_value &= {"|", "L", "J"}
                max_steps = max(max_steps, curr_steps + 1)
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited:
                queue.append((row, col, curr_steps + 1))

    new_grid = []
    for i in range(len(grid)):
        row_grid = []
        for j in range(len(grid[0])):
            if (i, j) == start:
                row_grid.append(possible_start_value.pop())
            elif (i, j) in visited:
                row_grid.append(grid[i][j])
            else:
                row_grid.append(".")
        new_grid.append(row_grid)

    # print("\n".join(["".join(row) for row in new_grid]))

    inside_points = set()

    for r, row in enumerate(new_grid):
        inside = False
        on_line_up = False
        on_line_down = False
        for c, col in enumerate(row):
            if col == "|":
                inside = not inside
            elif col == "L":
                on_line_up = True
            elif col == "F":
                on_line_down = True
            elif col == "J":
                if on_line_down:
                    inside = not inside
                on_line_down = False
                on_line_up = False
            elif col == "7":
                if on_line_up:
                    inside = not inside
                on_line_down = False
                on_line_up = False
            if inside:
                inside_points.add((r, c))

    inside_points = inside_points - visited

    # print new grid with main loop and O for outside points and I for inside points
    final_grid = []
    for i in range(len(new_grid)):
        row_grid = []
        for j in range(len(new_grid[0])):
            if new_grid[i][j] == ".":
                if (i, j) in inside_points:
                    row_grid.append("I")
                else:
                    row_grid.append("O")
            else:
                row_grid.append(new_grid[i][j])
        final_grid.append(row_grid)

    # print("\n".join(["".join(row) for row in final_grid]))

    print(len(inside_points))


if __name__ == "__main__":
    main()
