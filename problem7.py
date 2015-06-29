"""
https://projecteuler.net/problem=7

This is fairly straightforward, no explanation is needed.
"""
import math
def is_prime(n):  # does not handle 0 or 1
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

g = 10001  # goal
i = 0  # how many primes we have
n = 1  # what our test number is
while i < g:
    n += 1
    if is_prime(n):  # if number is prime, increment number of primes
        i += 1
# when loop finishes, we are at our prime number threshold. print n
print n
