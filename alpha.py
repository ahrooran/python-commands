
alpha=input('enter letter: ')
if ord(alpha) >= 65 and ord(alpha) <= 90:
	print('Uppercase')

else:
	if ord(alpha) >=97 and ord(alpha)<=122:
			print('lowercase')
	else:
		if ord(alpha) >=48 and ord(alpha)<=57:
			print('digits')
		else:
			print('other charachters')

print(chr(ord(alpha)+32))

