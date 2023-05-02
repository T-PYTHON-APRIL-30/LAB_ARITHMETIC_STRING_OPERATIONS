price = 2.99
quantity = 3
tax_rate = 0.075
tax_rate1= tax_rate*100
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
price_print = f"Price of item: ${price}"
print(price_print)
Quant_print = f"Quantity: {quantity}"
print(Quant_print)
rate_print = f"Tax rate: {tax_rate1}%"
print(rate_print)
print("----")
Sub_print = f"Subtotal is: ${subtotal}"
print(Sub_print)
Tax_print = f"Tax: ${tax:.2f}"
print(Tax_print)
tot_print = f"Total: ${total:.2f}"
print(tot_print)

