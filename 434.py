'''
x = 5
y = 6
z = 7

if all([x==5 , y==6 , z==7]):
    print('----')
'''

'''
x = 0
while x < 10 :
    print(x)
    x += 1
'''

start = input('Enter Start : ')
end = input('Enter End : ')
print(type(start))
for x in range(start,end):
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")
