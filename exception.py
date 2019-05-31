try: 
	x=int(input('enter number to divide: '))
	y=int(input('this is a second number: '))
	result=x/y

	print('result = ',result)

except ZeroDivisionError: 
	print('Cannot divide by zero')

except ValueError:
	print('error with value input')

except Exception:
	print('exception default')

finally: 
	print('this will always execute')
