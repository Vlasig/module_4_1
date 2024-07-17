from math import inf

def divide(first, second):
    if second != 0:
        res = first/second
        return res
    else:
        return inf

# print(divide(45, 5))
# print(divide(23, 0))
