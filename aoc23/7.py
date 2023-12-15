# Problem
input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
# 69999 111
# J9999 111
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


def day7part1():
    file = input.splitlines()
    # with  as file:
    # f = open('./input/7.txt', 'r')
    # file = f.read().splitlines()
    # f.close()

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
            items = sorted(analysis.items(), key=lambda x: x[1], reverse=True)

            # J cards can pretend to be whatever card is best for the purpose of
            # determining hand type;
            jocker_count = 0
            for card, count in items:
                if card == 'J':
                    jocker_count = count
                    break

            print(jocker_count)
            print(items)
            values = sorted(analysis.values(), reverse=True)

            highest = values[0]
            # FIXME: what happens if combination is made out of jockers?

            # logic should be
            # 5 > 4 > 32 > 3 > 22 > 1 > 0
            if highest == 5:  # five of a kind # is impossible without a jocker
                hands_buckets[5].append((hand, bet))
            elif highest == 4:  # four of a kind
                if jocker_count == 1:  # 4 + J = 5
                    hands_buckets[5].append((hand, bet))
                else:
                    hands_buckets[4].append((hand, bet))
            else:
                highest2 = values[1]
                if highest == 3:  # three
                    if jocker_count == 2:  # 3 + JJ = 5
                        hands_buckets[5].append((hand, bet))
                    elif jocker_count == 1:  # 3 + J = 4
                        hands_buckets[4].append((hand, bet))
                    elif highest2 == 2:  # full house
                        hands_buckets[32].append((hand, bet))
                    else:  # three of a kind
                        hands_buckets[3].append((hand, bet))
                elif highest == 2:  # pair
                    if jocker_count == 3:  # 2 + JJJ = 5
                        hands_buckets[5].append((hand, bet))
                    if jocker_count == 2:  # 2 + JJ = 4
                        hands_buckets[4].append((hand, bet))
                    if jocker_count == 1:  # 2 + J = 3
                        hands_buckets[3].append((hand, bet))
                    if highest2 == 2:
                        if jocker_count == 1:  # 2 + 2 + J = 32
                            hands_buckets[32].append((hand, bet))
                        else:
                            hands_buckets[22].append((hand, bet))
                    else:  # one pair
                        if jocker_count == 4:  # 0 + JJJJ = 5
                            hands_buckets[5].append((hand, bet))
                        if jocker_count == 3:  # 0 + JJJ = 4
                            hands_buckets[5].append((hand, bet))
                        if jocker_count == 2:  # 0 + JJ = 3
                            hands_buckets[4].append((hand, bet))
                        if jocker_count == 1:  # 0 + J = 2
                            hands_buckets[3].append((hand, bet))

                        hands_buckets[1].append((hand, bet))
                else:  # highest card
                    hands_buckets[0].append((hand, bet))

    print(hands_buckets)
    # now sort the buckets based on second ordering rule
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
        # print('sorted', sorted_buckets)
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
