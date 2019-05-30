def wordcount(msg):
	word =1
	i=0
	while i < len(msg):
		if msg[i] ==' ':
			word +=1
		i+=1
	return word

a = input('type a msg: ')
print('number of words: ',wordcount(a))