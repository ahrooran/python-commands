f=0
msg=input('')
find=input('')
replace=input('')
i=0

while i < len(msg):
	if msg[i:i+len(find)]==find:
		find=replace

	i+=1
print(f)
print(msg, replace)
