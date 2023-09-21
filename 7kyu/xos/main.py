# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# My solution

def xo(s):
    total = 0
    for letter in s:
        if letter.lower() == 'x':
            total += 1
        elif letter.lower() == 'o':
            total -= 1
    if total == 0:
        return True
    else:
        return False
