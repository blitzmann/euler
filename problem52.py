"""
https://projecteuler.net/problem=52

We calculate 2x and store the digits in a set. Then we calculate through 3x-6x
and compare those sets to our 2x. Pretty straightforward
"""
n=1
while True:
    n += 1

    s2 = set(str(n*2))
    for x in xrange(3, 7):
        if s2 != set(str(n*x)):
            break
    else:
        break
print n
