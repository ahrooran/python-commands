product = input("Name of Product: ")
price =float(input("Price? "))
qty = int(input("Qty? "))

ammount =qty*price
vat = ammount*15/100
bill = ammount + vat

print("Product", product)
print("VAT:", vat)
print ("Bill: ", bill)
print("Ammount: ", ammount)