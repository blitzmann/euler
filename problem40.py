"""
https://projecteuler.net/problem=40

Brute force the answer by iterating over all integers <= 1000000.
We keep track of our current count with c, and then we convert to 
a string and iterate through the elements to get digits.

There is probably a better way that ustilized python generators and 
the like. Meh
"""

import math

c = 0
digit = 0
found = []

while digit <= 1000000:
    c += 1
    for x in str(c):
        digit += 1

        # mod 1 will allow us to know if it's a whole number
        if math.log10(digit) % 1 == 0.0:
            found.append(int(x))

print reduce(lambda x, y: x*y, found)


