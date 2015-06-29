"""
https://projecteuler.net/problem=17

This one was a pain and not fun at all. There is probably a much more efficient
way of doing it, but I didn't care enough. We have three lists: ones-place
names, teens-place names, and tens-place names. This solution hardcodes the
number of digits to satisfy the problem, but it could be extended to go further.
The basic work flow:
- If there is a number in the thousands place, obtain number word and add length
    of "thousand"
- If there is a number in the hundreds place, obtain number word and add length
    of "hundred"
- The last two digits use a special function to determine if we need to use a
    combination of tens list with ones list, or use the teens list.
- Finally, if we have digits in tens/ones and in thousands or hundreds, add
    length of "and"
"""

ones = [
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
        # anything with a 1 in the tens is in the teens list
        return len(teens[int(s[-1])])
    else:
        # else, we get the tens word (0 will just be ""), and the ones word
        return len(tens[int(s[-2])])+len(ones[int(s[-1])])

def numLetters(i):
    s = str('%04d' % i)  # pad for easier handling
    r = 0

    if int(s[0]) != 0:  # thousands place
        r += len(ones[int(s[0])])+len("thousand")
    if int(s[1]) != 0:  # hundreds places
        r += len(ones[int(s[1])])+len("hundred")

    n = getTens(s[-2:])

    if n > 0 and r > 0:
        # we we are in this block, we have a thousand or hundred and
        # something to append, so we need "and"
        r += len("and")

    r += n  # add the tens values
    return r

r = 0
for x in xrange(1000):
    r += numLetters(x+1)
print r
