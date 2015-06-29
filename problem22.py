"""
https://projecteuler.net/problem=22

This one is fairly straight forward. Collect list of names, sort, generate list
of name value, and then sum it all up
"""
from urllib2 import urlopen
file = 'https://projecteuler.net/project/resources/p022_names.txt'
names = [x.strip('"') for x in urlopen(file).read().split(',')]
names.sort()

def getValue(name, sum = 0):
    sum = 0
    for char in name.lower():
        sum += (ord(char) - 96)
    return sum

result = sum([getValue(n)*(i+1) for i, n in enumerate(names)])
print result
