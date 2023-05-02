price = 2.99
quantity = 3
tax_rate = 7.5
subtotal = (price * quantity)

print("Price of item: $", price)
print("Quantity:", quantity)
print("Tax rate:", tax_rate ,"%")

print("Subtotal $" ,subtotal)

tax =  subtotal * 0.15
print("tax $",tax)

total = subtotal + tax
print("Total: $", total)
