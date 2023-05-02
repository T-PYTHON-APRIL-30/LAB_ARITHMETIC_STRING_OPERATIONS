price = 100
quantity = 3
tax_rate = 15
subtotal = (price * quantity)

print("Price of item", price)
print("Quantity", quantity)
print("Tax rate", tax_rate)

print("Subtotal" ,subtotal)

tax =  subtotal * 0.15
print("tax",tax)

total = subtotal + tax
print("Total:", total)

about_Cost = "subtotal is {} , tax is {} and total is {} ".format(subtotal, tax, total )
print(about_Cost)

