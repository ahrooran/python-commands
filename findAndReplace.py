find=input('Find: ')
replace=input('Replace with: ')

f_read=open('data.txt','r')
f_write=open('data2.txt','w')


for data in f_read:
	i=0
	while i < len(data):
		if data[i]==find[0]:
			if data [i:len(find)+i]==find:
				print(replace,end='',file=f_write)
				i +=len(find)-1
			else:
				print(data[i],end='',file=f_write)
		else:
			print(data[i],end='',file=f_write)
		i+=1









# new=msg.replace(find,replace)
# print(new)


# while i < len(msg):
# 	if msg[i:i+len(find)]==find:
# 		find=replace

# 	i+=1
# for find in msg:
# 	find.replace(find,replace)
# print(f)
# print(find, replace)
