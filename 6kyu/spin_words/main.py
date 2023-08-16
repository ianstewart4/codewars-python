# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

# My solution

def spin_words(sentence):
    words = sentence.split(' ')
    new_sentence = []
    for word in words:
        print(len(word))
        if len(word) > 4:
            new_sentence.append(word[::-1])
        else:
            new_sentence.append(word)
    return ' '.join(new_sentence)