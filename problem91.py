# Problem 91
# Could have done this a lot smarter probably and saved some cycles, but whatev.
# pythagorean function takes 3 point, 2 of which are generated. Some points don't make sense since they are
# identical, so we check for those. We also get a lot of duplicate combinations, such as (4,5)(3,2) and
# (3,2)(4,5). To check for this, we simply compare the two points thanks to pythons tuples.
# The rest of it is straight forward.

n = 50

def pythagorean(p1, p2, p3):
    if p1 == p2 or p2 == p3 or p3== p1 or p3 > p2:
        return False

    d1 = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
    d2 = (p3[0]-p2[0])**2+(p3[1]-p2[1])**2
    d3 = (p1[0]-p3[0])**2+(p1[1]-p3[1])**2
    ds = [d1, d2, d3]

    c = max(ds)
    ds.remove(c)

    return c == ds[0]+ds[1]

count = 0

for x1 in xrange(0,n+1):
    for y1 in xrange(0, n+1):
        for x2 in xrange(0,n+1):
            for y2 in xrange(0, n+1):
                if pythagorean((0,0),(x1,y1),(x2,y2)):
                    count +=1
print count
