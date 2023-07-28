

from functools import reduce

numbers = list(range(1,101))


def mysum(x,y):
    return x+y



result = reduce(mysum,numbers)
print(result)
