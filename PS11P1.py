def compute_discount(quantity, price, discount_rate):
    exprice = quantity * price
    discount_amount = exprice * discount_rate
    discounted_price = exprice - discount_amount
    return discount_amount, discounted_price

quantity = float(input("Enter quantity:"))
price = float(input("Enter price:"))
discount_rate = float(input("Enter discount rate:"))
discount_amount,discounted_price = compute_discount(quantity, price, discount_rate)

print("Quantity: ", quantity)
print("Price: ", price)
print("Discount amount: ", discount_amount)
print("Discounted price: ", discounted_price)
