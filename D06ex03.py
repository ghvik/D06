#!/usr/bin/env python
# D06ex03.py
# Reading from a text file
#
####################################################################################

def how_many_e(file_name):
    """Counts how many e's appear in the file
    
    Parameter:
    file_name -- the given file to read
    """
    count = 0
    with open(file_name) as fin:
        for line in fin:
            for letter in line.split()[0]:
                if letter == 'e':
                    count += 1
                
    print("There are {} instances of the letter 'e'.".format(count))

def names_with_e(file_name):
    """Prints the names with at least one 'e'
    
    Parameter:
    file_name -- the given file to read
    """
    words_with_e = []
    with open(file_name) as fin:
        for line in fin:
            has_an_e = False
            for letter in line.split()[0]:
                if letter == 'e':
                    has_an_e = True
            if has_an_e:
                words_with_e.append(line.split()[0])

    print("These are the names with at least one 'e': {}".format(words_with_e))

def main():
    how_many_e("roster.txt")
    names_with_e("roster.txt")
    
if __name__ == "__main__":
    main()