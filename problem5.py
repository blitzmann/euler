'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Start with the examples answer. Our final result must be a multiple of this answer (otherwise it would not satisfy the 1-10), which allows us to jump through a large amount of integers to test. We can also eliminate the first 10 checks as they would be inherently validated by the use of our multiple
'''

m = 2520
x = m
while True:
    for i in xrange(10,20):
        if x % (i+1) != 0:
            break
    else:
        break
    x += m
print x
