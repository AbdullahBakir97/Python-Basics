'''
def mysum(x=0,y=0):
    print(x+y)



mysum(5,10)    
'''
'''
# defination
def mysum(x,*vartuple):
    result = x
    for i in vartuple:
        result += i
    print(result)


# call
mysum(5,10,5,6,8,5)
'''
'''
f = 0
print(f)

def do():
    global f
    f = 5
    print(f)

do()
print(f)
'''


def mysum(x,y):
    return x+y

print(mysum(5,10))


mysum2 = lambda x,y:x+y
print(mysum2(5,10))


d = (lambda x,y:x+y)(5,10)


    
