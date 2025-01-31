sum_of_discount = 0

users_choice = input("Do you want to do this program? (yes/no)")

while users_choice == "yes":
    #input phase
    quantity = float(input("Enter quantity:"))
    price = float(input("Enter price:"))

    #process phase
    extended_price = quantity * price
    if extended_price >  10000.00:
        discount = 0.25
    else: discount = 0.10
    discount_amount = extended_price * discount 
    total= extended_price - discount_amount
    sum_of_discount= sum_of_discount + discount_amount
    
    #output phase
    print("Extended price: ", extended_price)
    print("Discount amount: ", discount_amount)
    print("Total: ", total)

    users_choice = input("Do you want to do this program again? (yes/no)")

print("Sum of discount: ", sum_of_discount)
