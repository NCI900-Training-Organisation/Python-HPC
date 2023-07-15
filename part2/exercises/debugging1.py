"""
Debug the below code so that it computes the correct sum of the numbers in the given data.txt file. 
Use the custom_sum() function to compute the sum.

"""


import os, sys

from custom_sum import custom_sum

if __name__ == "__main__":
    # fname = "/scratch/vp91/Monash2023/samuelyz/PyThon-HPC/part2/data/data.txt"
    fname = "../data/data.txt"
    f = open(fname, 'r')

    numbers = []
    for num_ in f:
        numbers += num_

    result = custom_sum(numbers)
    assert(result == 166), "Error: resulting sum is incorrect."
    print(f"Result ({result}) is correct!")