# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# My solution

def accum(s):
    new_s = ''
    for index, letter in enumerate(s):
        if index != len(s) - 1:
            new_s += letter.upper() + letter.lower() * (index) + '-'
        else:
            new_s += letter.upper() + letter.lower() * (index)
    return new_s
