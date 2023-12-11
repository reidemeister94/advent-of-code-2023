"""
https://adventofcode.com/2023/day/8#part2

--- Part Two ---
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
"""


from math import gcd


def main():
    lines: list[str] = []
    for line in open("input.txt"):
        lines.append(line.strip())

    moves = lines[0]
    nodes = {}
    starts: list[str] = []

    for line in lines[2:]:
        node, succ = line.split(" = ")
        left, right = succ.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left.strip(), right.strip())
        if node.endswith("A"):
            starts.append(node)
    steps_on_z = []

    for current in starts:
        idx_move = 0
        n_steps = 0
        while current[-1] != "Z":
            if moves[idx_move] == "R":
                current = nodes[current][1]
            else:
                current = nodes[current][0]
            idx_move = (idx_move + 1) % len(moves)
            n_steps += 1
        steps_on_z.append(n_steps)

    lcm = steps_on_z[0]
    for i in steps_on_z[1:]:
        lcm = lcm * i // gcd(lcm, i)

    print(lcm)


if __name__ == "__main__":
    main()
