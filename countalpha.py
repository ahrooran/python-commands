alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
message=upper.input('Enter messege: )


i=0
while i < len(message):
	alpha[ord(message[i])-65]+=1
	i+=1


i=0
while i <=25:
	if alpha[i]>0:
		print(chr(i+65),'=',alpha[i])
	i+=1


