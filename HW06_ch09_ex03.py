#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import pdb

# Body

def avoids(word, forbidden_letters):
    """ return True if word NOT forbidden, aka if it's allowed """
    # Want allowed to be a list of all True's in order
    # to return True
    allowed_letters = []
    for letter in word:
        if letter not in forbidden_letters:
            allowed_letters.append(True)
        else:
            allowed_letters.append(False)
            
    # If there is at least one forbidden letter,
    # there will be at least one False in the list
    if False in allowed_letters:
        return False
    else:
        return True

def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    count = 0
    user_forbids_these = input("Please enter a string of forbidden letters: ")
    with open('words.txt', 'r') as fin:
        for word in fin:
            if avoids(word, user_forbids_these):
                count += 1
    print(count)
    
def forbidden_param(forbidden_letters):
    """ return count of words NOT forbidden by param"""
    count = 0
    with open('words.txt', 'r') as fin:
        for word in fin:
            if avoids(word, forbidden_letters):
                count += 1
    return count


def find_five():
    letter_and_count = []
    
    print("Calculating the number of words that each letter excludes...")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        count = 0
        with open('words.txt', 'r') as fin:
            for word in fin:
                if avoids(word, letter):
                    count += 1
        letter_and_count.append((letter, count))
    
    
    print("These are the 5 letters that together would exclude the smallest number of words:")
    five_forbidden = ""
    words_excluded = 0
    five_letter_and_count = sorted(letter_and_count, key=lambda t: t[1])[:5]
    
    print("Here is the sorted list:\n {}".format(five_letter_and_count))
    for letter, count in five_letter_and_count:
        five_forbidden += letter
        words_excluded += count
    print("The five letters are '{}' and the number of words excluded is {}.".format(five_forbidden, words_excluded))

##############################################################################
def main():
    # Your final submission should only call five_five
    # 
    # Below are my test cases
    # print(avoids("apple", "bcad"))
    # forbidden_prompt()
    # print(forbidden_param("bcadefg"))
    # print(forbidden_param("Zeus"))
    # print(forbidden_param("abcdefghijklmnopqrstuvqxyz"))
    find_five()

if __name__ == '__main__':
    main()
