"""
https://projecteuler.net/problem=92

We create a recursive function that computes the square sum and returns true if 
it's 89. Takes over a minute to compute all < 10,000,000, but it works. Also has 
a progress indicator every 1,000 integers
"""
end = 10000000
n = 0

def square_sum(n):
    s = sum(map(lambda x: int(x)**2, list(str(n))))
    if s == 1:
        return False
    if s == 89:
        return True
    return square_sum(s)

r = 0
while n < end:
    if n % 1000 == 0:
        print n
    n += 1
    if square_sum(n):
        r += 1

print r
