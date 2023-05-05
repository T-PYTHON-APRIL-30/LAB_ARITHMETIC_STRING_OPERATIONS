#1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99


#2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quanitity = 3

tax_rate = 0.075

subtotal = quanitity*price
tax = tax_rate * subtotal
total = subtotal + tax


print(f"Price of item: ${price}")
print(f"Quantity: ${quanitity}")
print(f"Tax rate: {tax_rate*100}%")
print()
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")