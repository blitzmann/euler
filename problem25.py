"""
https://projecteuler.net/problem=25

We incorporate a Fibonacci generator and continue until we reach our
goal number of digits
"""
def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
digits = 1000
i = 0
for x in f:
    if len(str(x)) == digits:
        break
    i += 1
print i
