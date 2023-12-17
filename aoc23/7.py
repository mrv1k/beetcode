# Problem
input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

better_input_from_reddit ="""\
2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41
"""
# JJJJJ 111

# get: a list of hands
# goal: order based on strength
# hand consists of 5 cards

CARDS_DESC = ['A', 'K', 'Q', 'J', 'T', '9', '8',
              '7', '6', '5', '4', '3', '2', '1', '0']
CARDS_ASC = CARDS_DESC[::-1]

CARDS_ASC_JOKER_WEAK = CARDS_ASC.copy()
CARDS_ASC_JOKER_WEAK.remove('J')
CARDS_ASC_JOKER_WEAK[1] = 'J'
print(CARDS_ASC_JOKER_WEAK)


def day7part1():
    # file = "JJJ34 666".splitlines()
    # file = better_input_from_reddit.splitlines()
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
            items = sorted(analysis.items(), key=lambda x: x[1], reverse=True)

            # J cards can pretend to be whatever card is best for the purpose
            # of determining hand type;
            jocker_count = 0
            for card, count in items:
                if card == 'J':
                    jocker_count = count
                    break

            # handle what happens if combination is made out of jockers?
            start = 1 if (items[0][0] == 'J' and len(items) > 1) else 0
            aCard = items[start][1]
            # print(items)

            # logic should be
            # 5 > 4 > 32 > 3 > 22 > 1 > 0
            if aCard == 5:  # five of a kind # is impossible without a jocker
                hands_buckets[5].append((hand, bet))
            elif aCard == 4:  # four of a kind
                # QJJJJ 8888J
                if jocker_count >= 1:  # 4 + J = 5
                    hands_buckets[5].append((hand, bet))
                else:
                    hands_buckets[4].append((hand, bet))
            else:
                start2 = -1
                if len(items) > start + 1:
                    start2 = start + 2 if items[start + 1][0] == 'J' else start + 1

                try:
                    bCard = items[start2][1] if start2 != -1 else 0
                except:
                    print('broke, whateves. just swallow and move on', items)
                # print(items[start], items[start2], '|', start, start2)
                # print()

                if aCard == 3:  # three
                    if jocker_count == 2:  # 3 + JJ = 5
                        hands_buckets[5].append((hand, bet))
                    elif jocker_count == 1:  # 3 + J = 4
                        hands_buckets[4].append((hand, bet))
                    elif bCard == 2:  # full house
                        hands_buckets[32].append((hand, bet))
                    else:  # three of a kind
                        hands_buckets[3].append((hand, bet))
                elif aCard == 2:  # pair
                    # print('h2', analysis, hand, values, jocker_count)

                    # up until the point, jocker_count and card count would differ
                    # thus, we knew that highest card wasn't Jocker
                    # now we have to make sure it isn't
                    # an edge case could be: higest card is JJ, plus we count JJ
                    # for jocker_count, thus we get 4 out of 2 J's

                    if bCard == 2:
                        # JJQQA
                        if jocker_count == 2:
                            hands_buckets[4].append((hand, bet))
                        # AAQQJ
                        elif jocker_count == 1:  # 2 + 2 + J = 32
                            hands_buckets[32].append((hand, bet))
                        else:
                            hands_buckets[22].append((hand, bet))
                    else:  # one pair
                        # AAJ23 / 1 + J = 3; 0 + JJ = 3
                        if jocker_count == 2:
                            hands_buckets[4].append((hand, bet))
                        elif jocker_count == 1:
                            hands_buckets[3].append((hand, bet))
                        else:
                            hands_buckets[1].append((hand, bet))
                else:  # highest card
                    if jocker_count == 1:  # 0 + J = 2
                        hands_buckets[1].append((hand, bet))
                    elif jocker_count == 2:
                        hands_buckets[3].append((hand, bet))
                    elif jocker_count == 3:
                        hands_buckets[4].append((hand, bet))
                    elif jocker_count == 4:
                        hands_buckets[5].append((hand, bet))
                    else:
                        hands_buckets[0].append((hand, bet))

    # for bucket in hands_buckets.items():
    #     print('bucket', bucket)
    #     print()

    # now sort the buckets based on second ordering rule
    # compare 1st card in each hand, if different highest card combo wins
    # and so on so forth

    sorted_buckets = {}

    # J cards are now the weakest individual cards, weaker even than 2
    # J cards can pretend to be whatever card is best for the purpose of
    # determining hand type;
    for (combo, hands_with_bets) in hands_buckets.items():
        # print(combo, hands_with_bets)
        powers = []
        for hand, bet in hands_with_bets:
            power = []
            cards = list(hand)
            for card in cards:
                power.append(CARDS_ASC_JOKER_WEAK.index(card))
            else:
                powers.append((power, bet, hand))
        sorted_powers = sorted(powers, key=lambda x: x[0])
        sorted_buckets[combo] = sorted_powers

    store_served = 0
    order_number = 1

    for combo, buckets in sorted_buckets.items():
        # print(combo, buckets)
        for kfc in buckets:
            chicken, wings, _ = kfc
            fullfilled_order = wings * order_number
            store_served += fullfilled_order
            order_number += 1

    return store_served


print(day7part1())
