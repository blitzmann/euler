"""
https://projecteuler.net/problem=44

This takes way too much time, but it works. We start generating pentagontal
numbers and add them to a list. As we continue, we loop through the numbers
we have already generated and check if the difference is already in the list,
anid the addition is pentagontal via a test (since we haven't stored ahead
of our current position)
"""
import math

n = 0
p_nums = []
keepGoing = True
def isPentagonal(p):
    return (1 + math.sqrt((24*p) + 1))/6 % 1 == 0

while keepGoing:
    p = n*((3*n)-1)/2
    for x in p_nums:
        if p-x in p_nums and isPentagonal(p+x):
            print p-x, n
            n += 9999999999
            keepGoing = False
            break
    p_nums.append(p)
    n += 1
