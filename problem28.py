"""
https://projecteuler.net/problem=28

The idea behind this solution is that with every layer of the spiral, there are
four numbers that we need to abtain. These four numbers are separated by a very
easy to predict width, which is the width of the layer minus two. The next layer
will be exactly 2 more added to width

The direction of the spiral does not matter, as it is only a graphical
representation of what we are dealing with
"""

width = 1001
goal = width**2

n = 1  # starting number
i = 2  # starting increment
diagonals = [n]

while n < goal:
    for x in xrange(4):  # collect the four diagonals for this layer
        n += i
        diagonals.append(n)
    i += 2  # increase increment for next layer
    
print sum(diagonals)
