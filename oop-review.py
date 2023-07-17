'''
student:
    - create student (name) -> welcome
    -add mark
    -get avg
'''

'''
class student:
    def __init__(self,name):
        print (f'welcome {name} ')
        self.name = name
        self.marks = []
        

    def add_mark(self,mark):
        self.marks.append(mark)
        print(self.marks)

    def get_avg(self):
        print (self.marks)
        avg = sum(self.marks)/len(self.marks)
        print(f"{self.name} = {avg}")
    
    
s1 = student ('ahmad' ' ' 'mahmoud')
s2 = student('Ali')

s1.add_mark(50)
s1.add_mark(70)
s2.add_mark(80)
s2.add_mark(70)


s1.get_avg()
s2.get_avg()
'''

#s1.create_student('ahmed','mahmoud')


'''
    Bank:
        - create clint (name,age,gender)
        - deposit
        - withdraw
        - show details

'''
class User:
    
    
    def __init__(self,name,age,gender):
        print(f'welcome {name}')
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Gender  : {self.gender}")
        print(f"Balance : {self.balance}")    


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    

    def deposit(self,amount):
        self.balance += amount
        print(f"your current balance : {self.balance}")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print(f'insuffecient balance : {self.balance}')
            return
        
        self.balance -= amount
        print(f"your current balance : {self.balance}")

    
            
c1 = Bank('Ali',30,'Male')

c1.deposit(500)
c1.deposit(1000)

c1.withdraw(800)
c1.withdraw(1000)

c1.show_details()


