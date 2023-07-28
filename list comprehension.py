'''
names = ['ahmad','ali';'hassan';'mahamed']

#1
result = []
for n in names:
    result.append(len(n))

print(result)


#2

result2 = [len(n) for n in names]
print(result2)

'''

#even = [n for n in range(1,101) if n%2 ==0 ]
#print(even)

even = [f'{n} even' if n%2==0 else f'{n} odd' for n in range(1,101)]
print(even)
