ones= ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fiffteen','sixteen','seventeen','nineteen']

tens= ['','','twenty','thirty','fourty','fiffty','sixty','seventy','eighty','ninty']

num=int(input('Enter Number: '))

awnser=''
if num >= 1000 and num <=9999:
	awnser += ones[int(num/1000)] + ' thousand'
	num %= 1000
if num >= 100 and num <= 900:
	awnser +=ones[int(num/100)] + ' hundred'
	num %= 100
if num >=20 and num <=90:
	awnser += tens(int(num/10)*10)
	num %= 10
if num >= 0 and num <= 19:
	awnser+=ones(num)
if num > 9999:
	print('Please Enter a number between 0 and 9999')

print(awnser)
