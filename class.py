'''
class str
    '' "" ''' '''

    def upper
    def lower
    def split
    def replace
    def append
    def insert

'''    

'''
# encopsulation : self c1,c2
class Calc:  #c1,c2
    def mysum(self,x,y):
        print(x+y)


    def mymul(self,x,y):
        print(x*y)
        

    # constructor
    def __init__(self,name):
        print(f'welcome{name}')
    
    
c1 = Calc('ahmed')
#c1.mysum(5,10)


#c2 = Calc()
#c2.mymul(10,30)
'''

'''
class Calc:
    def __init__(self):
        print(f'welcome {name}')
    
    def mysum(self,x,y):
        print(x+y)

    def mymul(self,x,y):
        print(x*y)

class SciCalc(Calc):
    
    def power(self,x,y):
        print(x**y)


s = SciCalc('ahmed')

s.mysum(3,4)
s.mymul(3,4)
s.power(3,4)
'''



# inheritance : B,C,A,D
class A:
    def do(self):
        print('in A')

class B(A):
    pass

class C:
    def do(self):
        print('in C')


class D(C,B):
    pass

j = D()
j.do()




'''
s = 'ahmed'
l = [1,2,3,4]
t = (1,2,3,4)

len(s)
len(l)
len(t)


# polymorphism
class str:
    def len

class list : inherit
    def len

class tuple : inherit
    def len
    
'''


'''
class Calc # main super parent

class SciCalc(Calc) # derived sub child
'''

class Calc :
    # property
    total = 0 # class vlaue
    
    def sum(self,x,y):
        print(x+y)


c = Calc()
print(c.total)
#c.sum(3,4)

c.total = 100  # instance-object value
print(c.total)

del c.total
print(c.total)

del c.total
print(c.total)
        

