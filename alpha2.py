
alpha=input('Enter letter: ')
if ord(alpha) >= 65 and ord(alpha) <= 90:
	print('Converted to: ',chr(ord(alpha)+32))
	print('ASCI code is: ',ord(alpha))

else:
	if ord(alpha) >=97 and ord(alpha)<=122:
			print('Converted to: ',chr(ord(alpha)-32))
			print('ASCI code is: ',ord(alpha))
	else:
		if ord(alpha) >=48 and ord(alpha)<=57:
			print('It is a digit')
			print('ASCI code is: ',ord(alpha))
		else:
			print('this is another charachter')
			print('ASCI code is: ',ord(alpha))
alpha2=int(input('Enter a number: '))
print('charachter code is: ',chr(alpha2))