# Welcome to my Grocery Store

price = 2.99
quantity = 3
tax = 0.075

#Just to make the output clear
print("-"*20)

print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {100*tax}%")

#Just to make the output clear
print("-"*20)

# tot = total
totSub = price*quantity # Calculating the total price of items

totTax = price*tax # Total price "with the tax" for one item
totAmount = totTax*quantity 

total = totSub + totAmount 

print(f"Subtotal: ${totSub}")
print(f"Tax: ${totAmount}")
print(f"Total: ${total}")

#Just to make the output clear
print("-"*20)