
price = 2.99
quantity = 3
tax_rate = 0.075
subtotal = price * quantity
tax:float = subtotal * tax_rate
total = subtotal + tax 

print("Price of item:",price,"SAR")
print("Quantity:", quantity)
print("Tax rate:", tax_rate,"SAR")
print("Subtotal:" , subtotal,"SAR")
print("Tax:" ,tax,"SAR")
print("Total:" ,total,"SAR") 