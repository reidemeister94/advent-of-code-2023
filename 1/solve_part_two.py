"""
https://adventofcode.com/2023/day/1#part2

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


def find_words(input_line: str):
    result = ""
    i = 0
    while i < len(input_line):
        if input_line[i].isdigit() or input_line[i] not in {
            "o",
            "t",
            "f",
            "s",
            "e",
            "n",
        }:
            result += input_line[i]
            i += 1
        else:
            found = False
            for word in digits_words:
                if input_line[i : i + len(word)] == word:
                    result += str(digits_words.index(word) + 1)
                    i += len(word) - 1
                    found = True
                    break
            if not found:
                result += input_line[i]
                i += 1
    return result


def calculate_sum(processed_lines: list[str]):
    total_sum = 0
    for line in processed_lines:
        digits = [char for char in line if char.isdigit()]
        total_sum += int(digits[0] + digits[-1])
    return total_sum


digits_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
lines = []
for line in open("input.txt", "r"):
    lines.append(find_words(line.strip()))

print(calculate_sum(lines))
