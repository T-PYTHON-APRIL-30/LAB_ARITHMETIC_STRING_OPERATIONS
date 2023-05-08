price = 2.99
taxRate= 0.075
quiantity = 3
subtotal = price * quiantity
tax = subtotal * taxRate
totalPrice = tax + subtotal
print('Price of item: ${}'.format(price))
print('Quantity:${}'.format(quiantity))
print('Tax Rate: {}'.format(taxRate*100)+"%") 
print('\nSubtotal: ${}'.format(subtotal))
print('Tax: ${}'.format(round(tax,2)))
print('Total: ${}'.format(round(totalPrice,2)))