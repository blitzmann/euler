"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from urllib2 import urlopen
file = 'https://projecteuler.net/project/resources/p022_names.txt'
names = [x.strip('"') for x in urlopen(file).read().split(',')]
names.sort()

def getValue(name):
    sum = 0
    for char in name.lower():
        sum += (ord(char) - 96)
    return sum

result = sum([getValue(n)*(i+1) for i, n in enumerate(names)])
