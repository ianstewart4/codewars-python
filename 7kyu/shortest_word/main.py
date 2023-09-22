# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# My solution

def find_short(s):
    word_lengths = []
    for word in s.split():
        word_lengths.append(len(word))
    return min(word_lengths)  
