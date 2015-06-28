"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

"""
This one was a pain and not fun at all. There is probably a much more efficient way of doing it, but I didn't care enough.
"""

ones = [ # it says ones, but also includes 10-19
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

# special function to handle last two digits
def getTens(s):
    if int(s[-2]) == 1:
        # anything with a 1 in the tens needs to be accessed special treatment
        return len(teens[int(s[-1])])
    else:
        # else, we get the tens words (0 will just be ""), and the ones word
        return len(tens[int(s[-2])])+len(ones[int(s[-1])])

def numLetters(i):
    s = str('%04d' % i) # pad for easier handling
    r = 0

    if int(s[0]) != 0: # thousands place
        r += len(ones[int(s[0])])+len("thousand")
    if int(s[1]) != 0: # hundreds places
        r += len(ones[int(s[1])])+len("hundred")

    n = getTens(s[-2:])

    if n > 0 and r > 0:
        # we we are in this block, we have a thousand or hundred and
        # something to append, so we need "and"
        r += len("and")

    r += n # add the tens values
    return r

r = 0
for x in xrange(1000):
    r += numLetters(x+1)
print r
