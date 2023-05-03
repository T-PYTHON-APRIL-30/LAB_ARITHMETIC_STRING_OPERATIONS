'''You are a cashier at a grocery store. Write a Python program to calculate the total cost of a customer's purchase, including tax.

Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).

Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).

Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).

Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".

Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".

Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".

Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).

Example output:

Price of item: $2.99
Quantity: 3
Tax rate: 7.5%

Subtotal: $8.97
Tax: $0.67
Total: $9.64'''
price = 5.5
print("price of item:", "SAR", price)
quantity = 4
print("Quantity:",quantity)
tax_rate =15
Tax_rate =price * 0.15
print("Tax rate:",Tax_rate)
subtotal = price * quantity
print("subtotal:",subtotal)
print("Tax:",Tax_rate)
Total=subtotal + Tax_rate
print("total:",Total)