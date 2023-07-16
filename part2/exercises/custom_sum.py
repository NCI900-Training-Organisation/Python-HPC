
def custom_sum(x):
    if type(x[0]) == str:
        z = ""
        for y in x:
            z += y
    elif type(x[0]) == int:
        z = 0
        z = sum(x)
    
    return z