# Straightforward. Replace the 1001 with the width of spiral

goal = 1001**2
diagonals = [1]
n = 1
i = 2
while n < goal:
    for x in xrange(4):
        n+=i
        diagonals.append(n)
    i +=2
return sum(diagonals)
