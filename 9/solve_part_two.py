"""
https://adventofcode.com/2023/day/9#part2

--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
"""


def compute_diffs(history: list[int]) -> list[list[int]]:
    diffs = []
    while not all([x == 0 for x in history]):
        diffs.append(history)
        history = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    return diffs


def main():
    next_vals = 0
    for line in open("input.txt"):
        line = line.strip()
        history = list(map(int, line.split(" ")))

        diffs = compute_diffs(history)
        diffs = [elem[::-1] for elem in diffs]
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] - diffs[i + 1][-1])
        next_vals += diffs[0][-1]

    print(next_vals)


if __name__ == "__main__":
    main()
