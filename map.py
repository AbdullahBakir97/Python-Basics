'''
names = ['ahmed','ali','hassan','mohamed']


def myFunc(n):
    return len(n)


result = list(map(myFunc,names))
print(result)
'''



numbers = list(range(1,11))


def myFunc(n):
    return n*n

result = list(map(myFunc,numbers))
print(result)
