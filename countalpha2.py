

def countalpha(message, alpha):
	count=0
	i=0
	while i < len(message):
		if message[i].upper() == alpha:
			count +=1
		i+=1
	if count > 0:
		print(alpha,'=', count)


letters =input('enter a letter: ')
print(countalpha(letters))
