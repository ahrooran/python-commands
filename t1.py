found =0
msg=input("")
char=input("looking for?")
i=0
while i <len(msg):
	if msg[i] == char:
		found = found + 1
	i+=1
print(found)