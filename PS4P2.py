#input phase
item = input("Enter item type")
quantity = float(input("Enter quantity"))

#process phase
if item == "A":
  unit_price = 10.00
else: unit_price = 20.00

extended_price = quantity * unit_price

#output phase
print("Item: ", item)
print("Unit price: ", unit_price)
print("Extended price: ", extended_price)
