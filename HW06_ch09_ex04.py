#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body
def uses_only(word, letters):
    """Returns True if the word contains only letters in the list of letters"""
    letter_is_from_word_bank = []
    for letter in letters:
        if letter in word:
            letter_is_from_word_bank.append(True)
        else:
            letter_is_from_word_bank.append(False)
    # Check if there is at least one letter which is not from the list of
    # letters (aka the word bank)
    if False in letter_is_from_word_bank:
        return False
    else:
        return True

def is_a_word(word, english_dictionary):
    """Returns true if the given word exists in the given English dictionary file
    
    Parameters:
    word -- the given word
    english_dictionary -- the filename for list of English words"""
    
    with open(english_dictionary, 'r') as fin:
        english_words = fin.readlines()
    words = []
    for line in english_words:
        words.append(line.strip())
    if word in words:
        return True
    else:
        return False

def find_words(word_bank, word_list):
    """Find all possible words that use a string of allowed characters
    
    Parameter:
    word_bank -- the given string of allowed letters
    word_list -- """
    with open(word_list, 'r') as fin:
        english_words = fin.readlines()
    all_words = []
    for line in english_words:
        all_words.append(line.strip())
    allowed_words = []
    for word in all_words:
        if uses_only(word, word_bank):
            allowed_words.append(word)
    return allowed_words
    
def form_sentences(allowed_words):
    """Form a few sentences from a list of words"""
    print("{} {} {}".format(allowed_words[0],allowed_words[1],allowed_words[2]))
    print("{} {} {}".format(allowed_words[4],allowed_words[3],allowed_words[2]))
    print("{} {} {}".format(allowed_words[3],allowed_words[1],allowed_words[2]))
    print("{} {} {}".format(allowed_words[3],allowed_words[1],allowed_words[2],allowed_words[4],allowed_words[0]))
    
##############################################################################
def main():
    print(uses_only("boxcar", "abcrox"))  # Call your function(s) here.
    print(uses_only("boxcar", "abcrox ft"))
    print(is_a_word("zebra","words.txt"))
    print("Here is a list of words I can use with the string 'acefhlo':")
    allowed_words = find_words("acefhlo","words.txt")
    print(allowed_words)
    print("Here are some sentences I can use from these words:")
    form_sentences(allowed_words)
    
if __name__ == '__main__':
    main()
