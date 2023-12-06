"""
https://adventofcode.com/2023/day/6#part2

--- Part Two ---
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?
"""


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    times = [elem.strip() for elem in lines[0].split(":")[1].strip().split(" ") if elem != ""]
    distances = [elem.strip() for elem in lines[1].split(":")[1].strip().split(" ") if elem != ""]

    total_time = int("".join(times))
    total_distance = int("".join(distances))

    current_ways = 0

    for i in range(total_time):
        current_record = (total_time - i) * i
        if current_record > total_distance:
            current_ways += 1

    print(current_ways)


if __name__ == "__main__":
    main()
