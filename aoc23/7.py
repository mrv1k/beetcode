# Problem
input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
# AKQJT 111
# 98765 111
# 69696 666
# JJJJJ 111
# 66669 111

# get: a list of hands
# goal: order based on strength
# hand consists of 5 cards

CARDS_DESC = ['A', 'K', 'Q', 'J', 'T', '9', '8',
              '7', '6', '5', '4', '3', '2', '1', '0']
CARSD_ASC = CARDS_DESC[::-1]


def is_five_of_a_kind(cards):
    cards


def day7part1():
    # file = input.splitlines()
    # with  as file:
    f = open('./input/7.txt', 'r')
    file = f.read().splitlines()
    f.close()

    hands_with_bets = []
    for line in file:
        hands, bet = line.split()
        hands_with_bets.append((hands, int(bet)))

    hands_buckets = {
        0: [],  # highest card
        1: [],  # '1_pair': [],
        22: [],  # '2+2_pairs': [],
        3: [],  # '3_of_a_kind': [],
        32: [],  # '3+2_full_house': [],
        4: [],  # '4_of_a_kind': [],
        5: [],  # '5_of_a_kind': [],
    }

    # sort into 6 buckets of available hands
    for hand, bet in hands_with_bets:
        cards = list(hand)
        analysis = {}
        for card in cards:
            if card not in analysis:
                analysis[card] = 1
            else:
                analysis[card] += 1
        else:
            values = sorted(analysis.values(), reverse=True)

            highest = values[0]

            if highest == 5:  # five of a kind
                hands_buckets[5].append((hand, bet))
            elif highest == 4:  # four of a kind
                hands_buckets[4].append((hand, bet))
            else:
                highest2 = values[1]
                if highest == 3:  # three
                    if highest2 == 2:  # full house
                        hands_buckets[32].append((hand, bet))
                    else:  # three of a kind
                        hands_buckets[3].append((hand, bet))
                elif highest == 2:  # pair
                    if highest2 == 2:
                        hands_buckets[22].append((hand, bet))
                    else:  # one pair
                        hands_buckets[1].append((hand, bet))
                else:  # highest card
                    hands_buckets[0].append((hand, bet))

    # TODO: now sort the buckets based on second ordering rule
    # compare 1st card in each hand, if different highest card combo wins
    # and so on so forth
    sorted_buckets = {}

    for (combo, hands_with_bets) in hands_buckets.items():
        # print(combo, hands_with_bets)
        powers = []
        for hand, bet in hands_with_bets:
            power = []
            cards = list(hand)
            for card in cards:
                power.append(CARSD_ASC.index(card))
            else:
                powers.append((power, bet))
        sorted_powers = sorted(powers, key=lambda x: x[0])
        sorted_buckets[combo] = sorted_powers
        # print('raw', powers)
        # print('sorted', sorted_power)
        # print()

    store_served = 0
    order_number = 1

    for combo, buckets in sorted_buckets.items():
        for kfc in buckets:
            chicken, wings = kfc
            fullfilled_order = wings * order_number
            store_served += fullfilled_order
            order_number += 1

    return store_served


print(day7part1())
