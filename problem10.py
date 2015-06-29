"""
https://projecteuler.net/problem=10

Modified from #7 solution. This is fairly straightforward, albeit take quite a
while. Haven't really looked into optimizations.
"""

import math
def is_prime(n):  # does not handle 0 or 1
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

g = 2000000  # goal
n = 1  # what our test number is
sum = 0
while n < g:
    n += 1
    if is_prime(n):
        sum += n

print sum
