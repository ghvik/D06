# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_of_numbers, sum_of_numbers=0):
    """Recursively finds the sum of numbers in a n-nested list
    where n is any number, and the nests appears anywhere.
    
    Parameters:
    lists_of_numbers -- the nested list of numbers
    sum_of_numbers -- the sum of the numbers in all the nested lists
                    (initial value = 0)
    """
    for obj in list_of_numbers:
        if isinstance(obj, list):
            sum_of_numbers = nested_sum(obj, sum_of_numbers)
        else:
            sum_of_numbers += obj
    return sum_of_numbers

def main():
    print(nested_sum([1, [4]]))
    print(nested_sum( [1,2,3,[4,5],[-1,-2,-3,[-4,-5]],6] ))
    print(nested_sum([-43, 43,[],[],[[]],8]))
    
if __name__ == "__main__":
    main()