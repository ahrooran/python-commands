


print("Enter your marks:")
p = int(input("What's your marks for Physics? "))
c = int(input("What's your marks for Chemistry? "))
m = int(input("What's your marks Maths? "))
total = p+c+m
per=total*100/450
outof=150*3

print("----------------MARKS----------------")
print("Physics:", p)
print("Chemistry:", c)
print("Maths:", m)
print("-------------------------------------")
print("Total:", total, "out of", outof)
print("Percentage:", per,"%")
print("-------------------------------------")
