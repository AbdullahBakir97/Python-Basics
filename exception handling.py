# exception handling

# if-else 
import math

age = input('Enter Age')
if age.replace('.',',').isnumeric():
    if float(age) > 0:
        print(round(100/float(age)),2)
        print(math.floor(100/float(age)))
        print(math.ceil(100/float(age)))
    else:
        print('please enter number > 0')
else:
    print('please enter number')

print('procesing')

#############################################
#try-except 
try:
    age = int(input('Enter Age:'))
    print(100/age)
    # processing x

    # close

 '''
    #all exceptions
except Exception:
     print('please enter number and number > 0')
    '''

except ValueError:
    print('please enter number and number > 0')
    # close


except ZeroDivisionError:
    print('please enter number and number > 0')
    # close


else: # no excptions
    print('in else')




finally: # always
    print('closing ....')


print('procesing')

