price=2.99
quantity=3
tax_rate=0.075

subtotal=price*quantity
tax=tax_rate*subtotal
total=subtotal+tax

print(f"Price of item: ${price}\n"+
      f"quantity: {quantity} \n"+
      f"Tax rate:{tax_rate*100}%\n\n"
      f"subtotal:${subtotal}\n"+
      f"tax: ${round(tax,2)}\n"
      f"Total: ${round(total,2)}")