max = 999
min = 100
result = 0

# We basically calculate all possible values, keeping
# our highest value in a variable
# At the end of the loops, just spit the value out
for x in xrange(max, min, -1):
    for y in xrange(max, min, -1):
        product = x*y
        if str(product) == str(product)[::-1] and product > result:
            result = product
print result
