#input phase
quantity = float(input("Enter quantity"))

#process phase
if quantity >= 1000: 
  unit_price = 3.00
else: unit_price = 5.00
extended_price = quantity * unit_price

tax = extended_price * 0.7
total = extended_price + tax

#output phase
print("Quantity: ", quantity)
print("Unit price: ", unit_price)
print("Extended price: ", extended_price)
print("Tax: ",tax)
print("Total: ", total)
