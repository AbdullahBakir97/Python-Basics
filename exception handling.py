# exception handling

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

