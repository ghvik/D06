#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e():
    """Return True if a given word doesn't have the letter 'e' in it
    
    Parameter:
    word -- the given word to check"""
    
    with open("words.txt", 'r') as fin:
        for word in fin:
            has_e = False
            for letter in word:
                if letter == "e":
                    has_e = True
            if not has_e:
                print("This word does not have an 'e': {}".format(word))

##############################################################################
def main():
    has_no_e()  # Call your function(s) here.

if __name__ == '__main__':
    main()
