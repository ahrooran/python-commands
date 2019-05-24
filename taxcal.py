name =input("Enter Name: ")
salary =int(input("Enter Salary: "))
if salary > 20000:
	tax = salary*25/100
else:
	tax = salary*15/100
netsalary = salary-tax

print ()
print("Hi" ,name,", with your salary being £",salary)
print("Your tax would be £",tax)
print("Which means your net salary is £",netsalary)