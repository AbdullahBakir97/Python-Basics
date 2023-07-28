numbers = list(range(1,11))


def myFilter(n):
    if n%2==0:
        return n


result = list(filter(myFilter,numbers))
print(result)


result = list(map(myFilter,numbers))
print(result)


