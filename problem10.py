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

"""
After looking into primes and trying to optimize it, found the concept of 
prime number sieves. Basically, we start with a list of all true values. 
This like represents the prime status of it's index. We start looping through 
and check if the flag is True for that number. If so, that means this number is 
the next prime, and then we turn off all the multiples of that number. Very 
efficient, and dropped the computations from ~14s to ~1 sec
"""
import math

g = 2000000  # goal
sieve = [True] * g
sieve[0] = False
sieve[1] = False

for n in xrange(2, g):
    if not sieve[n]:
        continue
    else:
        for x in xrange(n+n, g, n):
            sieve[x] = False

sum = 0
for i, x in enumerate(sieve):
    if x:
        sum += i

print sum

