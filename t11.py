f=0
msg=input('')
find=input('')

i=0
while i < len(msg):
	if msg[i:i+len(find)]==find:
		f=f+1
		i=i+len(find)-1
	i+=1
print(f)
