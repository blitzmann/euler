"""
https://projecteuler.net/problem=6

This is fairly straightforward, no explanation is needed.
"""
sum = 0  # this holds the sum, which is squared latter
sqr = 0  # this holds the sum of the squares
for x in xrange(100):
    sum += (x+1)
    sqr += (x+1)**2
print abs(sqr - sum**2)
