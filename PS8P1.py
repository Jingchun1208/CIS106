def compute_total(quantity, price):
    total = quantity * price

    if total > 100000:
        total = total * 0.9
    else: total = total
    return total

total_extended_price = 0
users_choice = input("Do you want to compute extended price? (yes/no)")

while users_choice == "yes":
    quantity = float(input("Enter quantity"))
    price = float(input("Enter price"))
    total = compute_total(quantity, price)
    total_extended_price = total_extended_price + total
    print("Total extended price: ", total_extended_price)

    users_choice = input("Do you want to compute extended price again? (yes/no)")

print("Total extended price: ", total_extended_price)

