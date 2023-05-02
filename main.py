price = 2.99
print("Price of item: $" + str(price))

quantity = 3
print("Quantity: " + str(quantity))

tax_rate = 7.5/100
print("Tax rate: 7.5% \n")

subtotal = price * quantity
print("Subtotal: $" + str(subtotal))

tax = subtotal * tax_rate
print("Tax: $" + str(round(tax, 2)))

total = subtotal + tax
print("Total: $" + str(round(total, 2)))