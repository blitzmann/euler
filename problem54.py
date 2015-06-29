"""
https://projecteuler.net/problem=54

This was a very fun problem. I broke it down into 2 parts, testing and comparing
 - Testing each group of cards for a playable hand. This returns a boolean value
   depending on if the cards meet the criteria for the hand. A set of cards may
   test positive for multiple hands. It is this reason we start with the highest
   ranked hand and go down. If player 1 tests positive and the other does not,
   then player 1 wins that play
 - If both players test positive for the same type of hand, then we must compare
   both hands. The compare functions test each hand to determine who wins based
   on highest value according to the rules of Poker.
 - If both players do not have a poker and at the end of the tests, do a simple
   high card comparison to determine winner

Per instructions, this solution does not attempt to verify validity of provided
data. The Card class is a recycled bit of code from an old project of mine that
proved to be a nice little container for card data, making the solution easier
"""

from itertools import groupby
from urllib2 import urlopen
file = 'https://projecteuler.net/project/resources/p054_poker.txt'
data = urlopen(file)

class Card():
    suitNames = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    faceNames = ('2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, str='AS'):
        # start conversion of human-readable string to proper indices
        n = len(str)
        face, suit = str[0], str[1]

        for i in range(0, 4):
            if self.suitNames[i][0] == suit:
                suit = i
                break

        if face.isdigit() is True:
            face = int(face) - 2 # index of given face value
        else:
            for i in range(8, 13):
                if self.faceNames[i][0] == face:
                    face = i
                    break

        self.suitIndex = suit
        self.faceIndex = face
        self.rank = face + 2

    def __int__(self):
        return self.rank

def testStraight(hand):
    # We test that all cards are unique in rank, and of proper sequence:
    # RankHigh - RankLow == #Cards - 1 (only works if list is uniquw)
    l = set([c.rank for c in hand])
    return len(l) is 5 and max(l) - min(l) is len(l) - 1

def testFlush(hand):
    # We test that all cards are of same suit
    return len(set(c.suitIndex for c in hand)) is 1

def testRoyal(hand):
    # We test that all cards are of same suit and
    # that lowest rank of card is ten
    return testFlush(hand) and min(hand, key=lambda x: x.rank).rank == 10

def testStraightFlush(hand):
    return testStraight(hand) and testFlush(hand)

def testFourKind(hand):
    # We group the list based on the rank of each card and test
    # if there is a 4 in the result
    l = [len(list(group)) for key, group in groupby(hand, key=lambda x: x.rank)]
    return 4 in l

def testFullHouse(hand):
    # We group the list based on the rank of each card and test
    # if there is a 3 and 2 in the result
    l = [len(list(group)) for key, group in groupby(hand, key=lambda x: x.rank)]
    return 3 in l and 2 in l

def testThreeKind(hand):
    # We group the list based on the rank of each card and test
    # if there is a 3 in the result
    l = [len(list(group)) for key, group in groupby(hand, key=lambda x: x.rank)]
    return 3 in l

def testTwoPairs(hand):
    # We group the list based on the rank of each card and test
    # if there are two groups of 2
    l = [len(list(group)) for key, group in groupby(hand, key=lambda x: x.rank)]
    return l.count(2) == 2

def testPair(hand):
    # We group the list based on the rank of each card and test
    # if there is a 2 in the result
    l = [len(list(group)) for key, group in groupby(hand, key=lambda x: x.rank)]
    return 2 in l

def compareSingleSets(hand1, hand2, n):
    # We do the same operations when comparing Pairs, Three of a Kind, and
    # Four of a Kind in that we compare the set values. 3/4 of a Kind do not
    # need additional processing as they will never tie but we include
    # additional steps for the Pair compare

    # get dict of value : number of occurrences
    l1 = {key:len(list(group)) for key, group in groupby(hand1, key=lambda x: x.rank)}
    l2 = {key:len(list(group)) for key, group in groupby(hand2, key=lambda x: x.rank)}

    # Get the value of the pairs to test
    t1 = l1.keys()[l1.values().index(n)]
    t2 = l2.keys()[l2.values().index(n)]

    if t1 > t2:
        return hand1
    elif t2 > t1:
        return hand2
    else:  # used to compare tied Pairs
        # store values of cards
        v1 = sorted(l1.keys(), reverse=True)
        v2 = sorted(l2.keys(), reverse=True)

        # remove the pair tested
        v1.remove(t1)
        v2.remove(t2)

        if v1 > v2:
            return hand1
        elif v2 > v1:
            return hand2

def compareThreeKind(hand1, hand2):
    return compareSingleSets(hand1, hand2, 3)

def comparePair(hand1, hand2):
    return compareSingleSets(hand1, hand2, 2)

def compareFourKind(hand1, hand2):
    return compareSingleSets(hand1, hand2, 4)

def compareTwoPairs(hand1, hand2):
    # Two pair is slightly different, so we cannot use the other method

    # get dict of value : number of occurrences
    l1 = {key:len(list(group)) for key, group in groupby(hand1, key=lambda x: x.rank)}
    l2 = {key:len(list(group)) for key, group in groupby(hand2, key=lambda x: x.rank)}

    # Get the value of the loner and remove it from dict
    t1 = l1.keys()[l1.values().index(1)]
    t2 = l2.keys()[l2.values().index(1)]
    l1.pop(t1)
    l2.pop(t2)
    k1 = sorted(l1.keys(), reverse=True)
    k2 = sorted(l2.keys(), reverse=True)
    if k1 > k2:
        return hand1
    elif k2 > k1:
        return hand2
    elif t1 > t2:
        return hand1
    return hand2

def compareStraight(hand1, hand2):
    # Dead simple, simply compare the highest card. Assumes hand is ordered
    if hand1[-1].rank > hand2[-1].rank:
        return hand1
    return hand2

def compareHighestCard(hand1, hand2):
    # Very simple. Make a list of all values and compare. This is also used to
    # compare Flushes
    l1 = sorted([c.rank for c in hand1], reverse=True)
    l2 = sorted([c.rank for c in hand2], reverse=True)

    if l1 > l2:
        return hand1
    return hand2

def compareFullHouse(hand1, hand2):
    # This takes a similar approach than the others, however we simply check the
    # set of 3 cards and don't check the remaining ones because there cannot be
    # two players with the same value in a regular deck without wildcards.

    #  get dict of value : number of occurrences
    l1 = {key:len(list(group)) for key, group in groupby(hand1, key=lambda x: x.rank)}
    l2 = {key:len(list(group)) for key, group in groupby(hand2, key=lambda x: x.rank)}

    # Get the value of the pairs to test
    t1 = l1.keys()[l1.values().index(3)]
    t2 = l2.keys()[l2.values().index(3)]

    if t1 > t2:
        return hand1
    return hand2

tests = [
    testPair,
    testTwoPairs,
    testThreeKind,
    testStraight,
    testFlush,
    testFullHouse,
    testFourKind,
    testStraightFlush,
    testRoyal
]

compares = [
    comparePair,
    compareTwoPairs,
    compareThreeKind,
    compareStraight,
    compareHighestCard,
    compareFullHouse,
    compareFourKind,
    compareStraight,  # compare straight flush is the same as straight
    None  # two Royals is not possible (IRL, players would split pot)
]

compareMapping = dict(zip(tests, compares))

p1_pts = 0
p2_pts = 0

for play in data:
    play = play.split(" ")
    p1_hand = sorted([Card(c) for c in play[:5]], key=lambda x: x.rank)
    p2_hand = sorted([Card(c) for c in play[5:]], key=lambda x: x.rank)

    for test in reversed(tests):
        t1 = test(p1_hand)
        t2 = test(p2_hand)
        if test(p1_hand) and not test(p2_hand):
            p1_pts += 1
            break
        elif test(p2_hand) and not test(p1_hand):
            p2_pts += 1
            break
        elif test(p1_hand) and test(p2_hand):
            # tie in rank, start comparing
            func = compareMapping[test]
            winner = func(p1_hand, p2_hand)
            if winner == p1_hand:
                p1_pts += 1
            else:
                p2_pts += 1
            break
    else:
        # if we reach here, neither player has an interesting hand. Use
        # basic compare
        winner = compareHighestCard(p1_hand, p2_hand)
        if winner == p1_hand:
            p1_pts += 1
        elif winner == p2_hand:
            p2_pts += 1

print "Player 1 pts:",p1_pts

