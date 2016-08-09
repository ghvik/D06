#!/usr/bin/env python
# D06ex04.py
# Reading from a text file and writing to another file
#
####################################################################################

def how_many_e(file_in, file_out):
    """Counts how many e's appear in the file
    
    Parameter:
    file_in -- the given file to read
    file_out -- the file name to write output to
    """
    count = 0
    with open(file_in) as fin:
        for line in fin:
            for letter in line.split()[0]:
                if letter == 'e':
                    count += 1
    
    with open(file_out, 'w') as fout:
        fout.write("There are {} instances of the letter 'e'.\n".format(count))

def names_with_e(file_in, file_out):
    """Prints the names with at least one 'e'
    
    Parameter:
    file_name -- the given file to read
    file_out -- the file name to write output to
    """
    words_with_e = []
    with open(file_in) as fin:
        for line in fin:
            has_an_e = False
            for letter in line.split()[0]:
                if letter == 'e':
                    has_an_e = True
            if has_an_e:
                words_with_e.append(line.split()[0])
                
    with open(file_out, 'a') as fout:
        fout.write("These are the names with at least one 'e': {}".format(words_with_e))

def main():
    how_many_e("roster.txt", "names_with_e.txt")
    names_with_e("roster.txt", "names_with_e.txt")
    
if __name__ == "__main__":
    main()