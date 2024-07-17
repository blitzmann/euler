"""
https://projecteuler.net/problem=206
NOT DONE
"""

min = 1010101010
max = 1389026623
x = min
while x <= max:
    if x % 100000: print x
    num = str(long(x**2))
    num = ''.join([num[y] for y, u in enumerate(list(num)) if y  %2 == 0])
    for t in xrange(len(num)):
        if (t+1 != int(num[t])):
            break
    else:
        print num
        break
    x+=1

print 'done'