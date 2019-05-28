
msg = input('Enter Message: ')
word=0
i=0
while i < len(msg):
	if msg[i] == " ":
		word = word + 1
	i+=1
print('There are',(word+1),'words.')