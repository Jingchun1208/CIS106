#input phase
quantity= int(input("Enter the number of tickets"))

#process phase
if quantity >= 25:
  price_per_ticket = 50.00
elif 10 < quantity < 24:
  price_per_ticket = 60.00
elif 5 < quantity < 9:
  price_per_ticket = 70.00
else: price_per_ticket = 75.00

total_cost = quantity * price_per_ticket

#output phase
print("Number of tickets: ", quantity)
print("Price per ticket: ", price_per_ticket)
print("Total cost: ", total_cost)
