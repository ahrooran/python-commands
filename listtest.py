numbers=[]
while True:
	num =int(input('enter num: '))
	if num ==0:
		print(numbers)
		break
	else:
		numbers.append(num)

highest = numbers [0]
i = 1
while i <len(numbers):
	if numbers[i] > highest:
		highest=numbers[i]
	i+=1
print('This is the Highest: ',highest)

