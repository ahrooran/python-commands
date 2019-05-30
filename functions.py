def tax(salary):
	if salary > 1500:
		t=salary*21/100
	else:
		t=salary*15/100
	return t
salary=int(input('Enter sal: '))
print('your tax: ',tax(salary))
print('your net: ',salary-tax(salary))

def msg():
	print('thank')
	print('you')

msg()

def addition(a,b):
	result = a+b
	print('the result is', result)

addition(2,10)
def difff(z,y):
	if z > y:
		r = y-z
	else:
		r = z-y
	return r

num = int(input('type '))
num2 = int(input('type '))

print('diff is: ',difff(num,num2))

