"""
https://projecteuler.net/problem=4

Very straightforward. For this solution, we calculate all possible values and
test if they are palindromic by reversing the string. Keep the number if it is
our highest
"""
max = 999
min = 100
result = 0

for x in xrange(max, min, -1):
    for y in xrange(max, min, -1):
        product = x*y
        if str(product) == str(product)[::-1] and product > result:
            result = product
print result
