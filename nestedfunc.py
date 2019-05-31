

def operations(day):
	if day == 1:
		def fun(a,b):
			c=a+b
			print('result is ',c)
	if day == 2:
		def fun(a,b):
			c=a-b
			print('result is ',c)
	return fun

x=input('')
y=input('')


ran=operations(2)
ran(5,2)



def add(a,b):
	c=a+b
	print('result is ',c)

def sub(a,b):
	c=a-b
	print('result is ',c)

def op(f,a,b):
	f(a,b)
op(add,10,20)
op(sub,50,10)

def dosomething(a=10,b=20,c=30,d=40):
	result = a+b+c+d
	print('the result is ',result)
dosomething()

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

# print(findlw(sentence))
print(findlw(sentence))