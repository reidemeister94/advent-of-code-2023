"""
https://adventofcode.com/2023/day/12#part2

--- Part Two ---
As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually folded up this whole time!

To unfold the records, on each row, replace the list of spring conditions with five copies of itself (separated by ?) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).

So, this row:

.# 1
Would become:

.#?.#?.#?.#?.# 1,1,1,1,1
The first line of the above example would become:

???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 16384 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 16 arrangements
????.######..#####. 1,6,5 - 2500 arrangements
?###???????? 3,2,1 - 506250 arrangements
After unfolding, adding all of the possible arrangement counts together produces 525152.

Unfold your condition records; what is the new sum of possible arrangement counts?

"""


memo = {}


def count_arrangements(conditions, nums):
    if not nums:
        return 0 if "#" in conditions else 1
    if not conditions:
        return 1 if not nums else 0

    if (conditions, nums) in memo:
        return memo[(conditions, nums)]

    result = 0

    if conditions[0] in ".?":
        result += count_arrangements(conditions[1:], nums)
    if conditions[0] in "#?":
        if (
            nums[0] <= len(conditions)
            and "." not in conditions[: nums[0]]
            and (nums[0] == len(conditions) or conditions[nums[0]] != "#")
        ):
            result += count_arrangements(conditions[nums[0] + 1 :], nums[1:])

    memo[(conditions, nums)] = result
    return result


def main():
    total = 0
    for line in open("input.txt"):
        conditions, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        conditions = "?".join([conditions] * 5)
        nums = nums * 5
        total += count_arrangements(conditions, nums)
    print(total)


if __name__ == "__main__":
    main()
