def findlw(sentence):
	lword=''
	longest=0
	for word in sentence:
		if len(word) > longest:
			lword = word
			longest=len(word)
	return lword


words = input('Enter Message: ')
sentence=words.split()

print(findlw(sentence))