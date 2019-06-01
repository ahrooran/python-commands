def findlw(sentence):
	lword=''
	longest=0
	for word in sentence:
		if len(word) > longest:
			lword = word
			longest=len(word)
	if len(word) == longest:
		print('there are duplicates')

	return lword


words = input('Enter Message: ')
sentence=words.split()

print(findlw(sentence))
print('there')
