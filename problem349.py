"""
https://projecteuler.net/problem=349

I solved this problem first by plotting out the moves as normal. I had a feeling that this would end up in some sort of 
infinite sequence due to the large number of moves that needed to be calculated (10^18, which would have taken too much
time and memory to calculate by only doing the move calculation).

After ~30,000 moves, I printed (-100, 100) on both x and y axis to see what it came up with, and quickly noticed this 
pattern (problem349.png)
 
Confirming that there is indeed a pattern, I set forth trying to identify that programatically (instead of monitoring 
the moves themselves to identify it)
  
Once the pattern (sequence) was known, along with how many black square the sequence produced, it was as simple as
extrapolating that out to 10^18 and including the blacks that has already been discovered.

After solving this puzzle, I explored the internet and found an entire Wikipedia page and YouTube videos on Lantons Ant,
with more information. Apparently this is a thing in the mathmetical / number theory crowd. This puzzle can be refined 
now that the values are known to make it more efficent (eg: we know the sequence length and when the sequence starts, 
which means we don't need to do the interim step of finding this programmatically), however I started this problem with 
only the information provided without looking up additional facts or constants. 
"""

import math

# Mapping to determine new ant direction
dir_mapping = {
    0: lambda point: [point[0], point[1] + 1],  # north
    1: lambda point: [point[0] + 1, point[1]],  # east
    2: lambda point: [point[0], point[1] - 1],  # south
    3: lambda point: [point[0] - 1, point[1]],  # west
}

targetNumber = 1e18
point = [0, 0]  # current point that the ant is on
blacks = set()  # a set of points that are black
direction = 0  # determines which direction we are heading, based on %4
directions = []  # a list of directions the ant takes, which is used to identify sequence programatically
blacks_list = []  # this goes hand in hand with directions, and stored weather or not the square was flipped to black (+1) or white (-1)

# Got this from Stack Overflow, forgot to reference.
# Returns a list of tuples indicating the indexes of longSeq in which shortSeq start and end
def getSeqOfSeq(shortSeq, longSeq):
   return [(i, i + len(shortSeq)) for i in range(len(longSeq)) if longSeq[i:i + len(shortSeq)] == shortSeq]

# Part 1: run the moves until the pattern shows itself.
move = 1
while True:
    t_point = tuple(point)
    if t_point in blacks:
        direction = (direction - 1) % 4  # move left
        blacks.remove(t_point)
        blacks_list.append(-1)
    else:
        direction = (direction + 1) % 4 # move right
        blacks.add(t_point)
        blacks_list.append(1)

    directions.append(direction)
    point = dir_mapping[direction](point)

    # every 10K moves, check the progress and break out if it looks like we have a repeating sequence starting
    if move % 10000 == 0:
        # do a check to find number of sequences of the last 200 directions; break once it gets to a high number of
        # repetition indicating high chance of repeating sequence
        if len(getSeqOfSeq(directions[-200:], directions)) > 200:
            break

    move += 1

# Part 2: find the actual sequence
# The previous sequence checker was a very rough check. We now need to refine it to get the actual sequence which is
# repeated. To do this, we start by finding the last two directions (needle) within the last 2000 directions (haystack).
# This will give us a list of tuples that determine where the sequence is found: [(startIdx, endIdx), ...].
# We keep prepending more directions to the needle until we have startIdx's equalling endIdx's, which means one found
# sequence has met up with another found sequence, which indicates the sequence starting to repeat

def thing(seq):
    for x in xrange(1, len(seq)):
        if seq[-x][0]-seq[-x-1][1] > 0:
            break
    else:
        return True
    return False

longSeq = directions[-2000:]  # get last 2K directions (some large subset of directions that we can test against)

i = -1
while True:
    # go backwards, getting more and more of our sequence until the different between them is 0
    shortSeq = directions[i:]
    test = getSeqOfSeq(shortSeq, longSeq)
    if thing(test):
        break
    i -= 1

# We now have the actual sequence. Calculate the remaining amount of moves needed, and get the blacks that are
# associated with that sequence
seqLen = len(shortSeq)
blacksForSequence = blacks_list[-seqLen:]

remaining_moves = long(targetNumber) - move
remaining_sequences = long(math.floor(remaining_moves / seqLen))
remaining_mod = remaining_moves % len(shortSeq)

# Add up the blacks that we found in the brute force + the remaining full sequence blacks + the remaining black to the target number
print(sum(blacks_list) + (sum(blacksForSequence) * remaining_sequences) + sum(blacksForSequence[:remaining_mod]))

# nifty thing to draw out the first bit of the grid
# for y in xrange(100, -100, -1):
#     row = []
#     for x in xrange(-100, 100):
#         row.append('#' if (x,y) in blacks else '.')
#     row.append(str(y))
#     print(''.join(row))
