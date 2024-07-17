"""
https://projecteuler.net/problem=112

This is pretty self explanatory. I sort the integer value by converting to a string, and if it's neither ascending or 
descending, I increment a counter. I check this counter against total to get a percentage.
"""

i = 0
x = 0
while True:
    x += 1
    t = str(x)

    if "".join(sorted(t)) != t and "".join(sorted(t, reverse=True)) != t:
        i +=1

    if float(i)/float(x) == 0.99:
        break

print x