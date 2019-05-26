bill = float(input("Whats the bill? "))
given =float(input("Cash given: "))

cash=float(given)-float(bill)

c_50 = cash // 50
c_20 = cash % 50 // 20
c_10 = cash % 50 % 20 // 10
c_5 = cash % 50 % 20 % 10 // 5
c_2 = cash % 50 % 20 % 10 % 5 // 2
c_1 = cash % 50 % 20 % 10 % 5 % 2 //1
c_05 = cash % 50 % 20 % 10 % 5 % 2 %1 //0.5



print("Change Due: £{}".format(cash))
print("-------------------------------------------")
if c_50 >=1:
	print("£50 x",int (c_50))
if c_20 >=1:
	print("£20 x",int(c_20))
if c_10 >= 1:
	print("£10 x",int(c_10))
if c_5 >= 1:
	print("£5 x",int(c_5))
if c_2 >= 1:
	print("£2 x",int(c_2))
if c_1 >= 1:
	print("£1 x",int(c_1))
if c_05 >= 1:
	print("50p x",int(c_05))


