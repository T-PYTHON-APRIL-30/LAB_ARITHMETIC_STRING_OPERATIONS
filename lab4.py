'''
You are a cashier at a grocery store. Write a Python program to calculate the total cost of a customer's purchase, including tax.

Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).

Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).

Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).

Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".

Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".

Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".

Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).

'''

price = 30.99
quantity = 4
tax_rate = 1.5

subtotal = price*quantity

tax = subtotal * tax_rate

total_cost = subtotal + tax

print(f'Price of item: ${price}')
print(f'Quantity: {quantity}')
print(f'Tax rate: %{tax_rate}')
print()
print(f'Subtotal: ${subtotal}')
print(f'Tax: ${tax}')
print(f'Total: ${total_cost}')