# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(summand1, summand2):
    summands_and_sum = []
    summands_and_sum.extend([summand1, summand2])
    summands_and_sum.append([sum([summand1, summand2])])
    return summands_and_sum[2][0]

def main():
    print(nested_sum(1, 4))
    print(nested_sum(321, -325))
    print(nested_sum(-43, 43))
    
if __name__ == "__main__":
    main()