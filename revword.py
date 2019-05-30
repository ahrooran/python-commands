try:
	msg = input('Enter Message: ')

	i=len(msg)-1
	while i >=0:
		x=split(msg[i],end='')
		print(x)
		i-=1

except NameError:
	print('there is an issue with the names ')
except Exception:
	print('threrefw')
finally: 
	print('whatt')