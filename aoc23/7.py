# Problem
input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
AKQJT 322
69696 666
JJJJJ 111
66669 111
"""

# get: a list of hands
# goal: order based on strength
# hand consists of 5 cards

CARDS_DESC = ['A', 'K', 'Q', 'J', 'T', '9', '8',
              '7', '6', '5', '4', '3', '2', '1', '0']
CARSD_ASC = CARDS_DESC[::-1]


def is_five_of_a_kind(cards):
    cards


def day7part1():
    # with open('./input/example.txt', 'r') as file:
    file = input.splitlines()
    hands_with_bets = []
    for line in file:
        hands, bet = line.split()
        hands_with_bets.append((hands, int(bet)))

    combination_buckets = {
        5: [],  # '5_of_a_kind': [],
        4: [],  # '4_of_a_kind': [],
        32: [],  # '3+2_full_house': [],
        3: [],  # '3_of_a_kind': [],
        2: [],  # '2_pair': [],
        1: [],  # '1_high_card': [],
    }
    # print(CARSD_ASC)
    # power = CARSD_ASC.index(card)
    # sort into 6 buckets of available combinations
    for hand, bet in hands_with_bets:
        cards = list(hand)
        analysis = {}
        # print(cards)
        for card in cards:
            # exists = analysis.get(card)
            # print(card, exists)
            if card not in analysis:
                analysis[card] = 1
            else:
                analysis[card] += 1
        else:
            values = sorted(analysis.values(), reverse=True)

            highest = values[0]
            if highest == 5:  # five of a kind
                combination_buckets[5].append(hand)
                continue

            highest2 = values[1]
            if highest == 4:  # four of a kind
                combination_buckets[4].append(hand)
            elif highest == 3:  # three
                if highest2 == 2:  # full house
                    combination_buckets[32].append(hand)
                else:  # three of a kind
                    combination_buckets[3].append(hand)
            elif highest == 2:  # two pair
                combination_buckets[2].append(hand)
            else:
                combination_buckets[1].append(hand)

            # combination_buckets[combo].append(combo)
            # print(analysis, 'max', values, highest, highest2)
        # break

    print(combination_buckets)
    return 'mek'


print(day7part1())
