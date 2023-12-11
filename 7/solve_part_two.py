"""
https://adventofcode.com/2023/day/7#part2

--- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
"""


from collections import defaultdict

hand_results = defaultdict(list)
cards_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}
result_types = [
    "high_card",
    "one_pair",
    "two_pair",
    "three_of_a_kind",
    "full_house",
    "four_of_a_kind",
    "five_of_a_kind",
]


def hand_strength(hand):
    return tuple(cards_strength[card] for card in hand)


def get_hand_result(hand: str):
    count_occurrences = defaultdict(int)
    for card in hand:
        count_occurrences[card] += 1

    jolly_count = count_occurrences.get("J", 0)

    if 0 < jolly_count < 5:
        # Remove jokers from the count
        del count_occurrences["J"]
        # Find the card with the maximum occurrence and highest strength
        max_card = max(
            count_occurrences, key=lambda card: (count_occurrences[card], cards_strength[card])
        )
        # Use jokers to increase the count of the selected card
        count_occurrences[max_card] += jolly_count

    if len(count_occurrences) == 5:
        hand_results["high_card"].append(hand)
    elif len(count_occurrences) == 4:
        hand_results["one_pair"].append(hand)
    elif len(count_occurrences) == 3:
        if 3 in count_occurrences.values():
            hand_results["three_of_a_kind"].append(hand)
        else:
            hand_results["two_pair"].append(hand)
    elif len(count_occurrences) == 2:
        if 4 in count_occurrences.values():
            hand_results["four_of_a_kind"].append(hand)
        else:
            hand_results["full_house"].append(hand)
    elif len(count_occurrences) == 1:
        hand_results["five_of_a_kind"].append(hand)


def main():
    hands_map = {}
    for line in open("input.txt"):
        line = line.strip()
        hand, bid = line.split(" ")
        hands_map[hand] = int(bid)
        get_hand_result(hand)

    ordered_hands = []
    for result_type in result_types:
        if result_type not in hand_results:
            continue
        sorted_hands_result_type = sorted(
            hand_results[result_type], key=lambda hand: hand_strength(hand)
        )
        ordered_hands.extend(sorted_hands_result_type)

    total_winnings = 0
    for index, hand in enumerate(ordered_hands):
        total_winnings += hands_map[hand] * (index + 1)

    print(total_winnings)


if __name__ == "__main__":
    main()
