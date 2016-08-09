#!/usr/bin/env python
# D06ex03.py
# Write 10 random numbers to a file
########################################################################

from random import randint


def write_random_numbers():
    for n in range(10):
        print(randint(1,50))
        
def main():
    write_random_numbers()
    
if __name__ == "__main__":
    main()