'''
https://projecteuler.net/problem=5

There's a trick to this one. We already know that 2520 is the lowest number
evenly divided by 1-10. We use this fact for two purposes:
- Since our result must be evenly divided by 1-10 (and 11-20), the result must
    be a multiple of 2520 (otherwise it would not satisfy 1-10 condition).
- Since our tests are multiples of 2520, we do not need to test 1-10 as they are
    inherently valid
Both of these facts greatly speed up the process when compared to brute-forcing
it.
'''

m = 2520
x = m
while True:
    for i in xrange(10, 20):
        if x % (i+1) != 0:
            # break the for loop and continue with the while
            break
    else:
        # break the while loop when we find a satisfactory answer
        break
    x += m
print x
