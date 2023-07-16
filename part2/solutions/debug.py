
def halve(x):
    return x/2

def average1(x, y):
    return halve(x+y)

def average2(x, y):
    return x+y/2


if __name__ == "__main__":
    x = float(input("Number 1: "))
    y = float(input("Number 2: "))

    print(f"Average is: {average2(x, y)}")
