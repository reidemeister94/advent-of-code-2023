"""
https://adventofcode.com/2023/day/5#part2

--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

"""


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n\n")

    input_seeds = list(map(int, lines[0].split(":")[1].strip().split(" ")))
    seeds = [(seed, seed + length) for seed, length in zip(input_seeds[::2], input_seeds[1::2])]

    blocks = []
    for block in lines[1:]:
        block = block.split("\n")[1:]
        block = [list(map(int, line.strip().split(" "))) for line in block]
        blocks.append(block)

    for block in blocks:
        new = []
        while seeds:
            seed_start, seed_end = seeds.pop()
            for dest, source, length in block:
                block_seed_start = max(seed_start, source)
                block_seed_end = min(seed_end, source + length)

                if block_seed_start < block_seed_end:
                    new_seed_start = block_seed_start - source + dest
                    new_seed_end = block_seed_end - source + dest

                    new.append((new_seed_start, new_seed_end))
                    if block_seed_start > seed_start:
                        seeds.append((seed_start, block_seed_start))
                    if seed_end > block_seed_end:
                        seeds.append((block_seed_end, seed_end))
                    break
            else:
                new.append((seed_start, seed_end))
        seeds = new

    print(min(seeds)[0])


if __name__ == "__main__":
    main()
