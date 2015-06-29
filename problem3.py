"""
https://projecteuler.net/problem=3

The solution to this problem is fairly straightforward. We continue looping
through an iteration, checking if goal is evenly divisible by i. If it is, i
is a prime factor - store it (it will automatically be the largest as we only
increase i). From here, continue by setting goal = goal / i
"""

goal = 600851475143
i = 2
r = 0
while True:
    if goal % i == 0:
        r = i
        goal /= i
        if goal == 1:
            break
    i += 1

print r
