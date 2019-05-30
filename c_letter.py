def change(message):
	i=0
	newmessage=""
	while i < len(message):
		ASCI =ord(message[i])
		if ASCI >= 65 and ASCI <= 90:
			newmessage+=chr(ASCI+32)
		else:
			if ASCI >= 91 and ASCI <= 122:
				newmessage+=chr(ASCI-32)
			else:
				if ASCI>=48 and ASCI<=57:
					newmessage+= str(int(chr(ASCI))*2)
				else:
					newmessage+=chr(ASCI)
		i+=1
	return newmessage

msg= input('enter any message: ')
print(change(msg))