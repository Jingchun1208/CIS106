def compute_total_price_and_tax_amount (quantity, unit_price):
    total_price = quantity * unit_price
    tax_amount = total_price * 0.07
    return total_price, tax_amount

total_price = 0
tax_amount = 0

quantity = float(input("Enter quantity:"))
price = float(input("Enter price:"))
total_price, tax_amount = compute_total_price_and_tax_amount(quantity, price)


print("Total price: ", total_price)
print("Tax amount: ", tax_amount)
