import os, sys


from custom_sum import custom_sum


if __name__ == "__main__":
    fname = "/scratch/vp91/Monash2023/samuelyz/Python-HPC/part2/data/data.txt"
    f = open(fname, 'r')
    
    numbers = []
    for num_ in f:
        try:
            x = int(num_.strip('\n'))
        except ValueError:
            continue
        numbers.append(x)

    result = custom_sum(numbers)
    assert(result == 166), "Error: resulting sum is incorrect."

    print(f"Result ({result}) is correct!")