price = 7
quantity = 4
tax_rate = 1.15
subtotal = price * quantity
tax_value = subtotal * 0.15

priceFormat = f"Price of item = {price} SAR"
quantityFormat = f"Quantity = {quantity}"
subtotalFormat = f"Subtotal = {subtotal} SAR"
taxFormat = f"Tax = {tax_value} SAR"
toalFormat = f"Total = {tax_rate*subtotal} SAR"

print (priceFormat)
print (quantityFormat)
print ("Tax rate = 15%")
print ("")
print (subtotalFormat)
print (taxFormat)
print (toalFormat)