"""
https://projecteuler.net/problem=36
"""

sum = 0
for x in range(0, 1000000):
    binNum = bin(x)[2:]
    if str(x) == str(x)[::-1] and binNum == binNum[::-1]:
        sum += x

print sum
