"""
https://projecteuler.net/problem=45

We generate the numbers numbers and store them in a list, one list for each
function. Periodically, we check the intersection of each list and test if
they have 3 or more common elements (first one is 1, and second one is used
in example). We do this check every 5000 iterations - doing it every time to
"break early" would waste time. So instead of breaking the loop as soon as
we get the answer, we continue until the intersection check, and then return
the third element if applicable
"""

def t(n):
    return (n*(n+1))/2

def h(n):
    return (n*((2*n)-1))

def p(n):
    return (n*((3*n)-1))/2


lt = []
lh = []
lp = []
n = 0
while True:
    n += 1
    lt.append(t(n))
    lh.append(h(n))
    lp.append(p(n))
    if n % 5000 == 0:
        intersect = set(lt).intersection(lh).intersection(lp)

        if len(intersect) >= 3:
            print list(intersect)[2]
            break

