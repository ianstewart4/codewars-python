# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# My solution

def duplicate_count(text):
    text_counts = {}
    dupe_count = 0
    for letter in text:
        letter = letter.lower()
        if letter in text_counts and text_counts[letter] == 1:
            dupe_count += 1
            # Mark that this duplicate has been counted
            text_counts[letter] += 1
        elif letter not in text_counts:
            text_counts[letter] = 1
            
    return dupe_count
