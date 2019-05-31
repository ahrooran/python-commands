
def reverse(word):
	newword=''
	i=len(word)-1
	while i >= 0:
		newword+=word[i]
		i-=1
	return newword

msg = input('Enter Message: ')
newmsg=''
word=''

for ch in msg:
	if ch ==' ':
		newmsg +=(reverse(word)+' ')
		word=' '
	else:
		word += ch
print(newmsg,reverse(word))

