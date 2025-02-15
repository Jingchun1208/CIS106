def compute_the_train_ticket_price (miles_from_downtown_Chicago):
    if miles_from_downtown_Chicago >=30:
       ticket_price = 12
    elif 20<= miles_from_downtown_Chicago <= 29:
        ticket_price=10
    elif 10<= miles_from_downtown_Chicago <= 19:
        ticket_price = 8
    else: ticket_price = 5
    return ticket_price

sum_price_of_ticket = 0
user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    last_name = input("Enter last name: ")
    miles_from_downtown_Chicago = float(input("Enter miles from downtown Chicago:"))
    ticket_price = compute_the_train_ticket_price (miles_from_downtown_Chicago)
    sum_price_of_ticket = sum_price_of_ticket + ticket_price

    print("Last name: ", last_name)
    print("miles from downtown Chicago:", miles_from_downtown_Chicago)
    print("Ticket price: ", ticket_price)

    user_choice = input("Do you want to do the program? (yes/no)")

print("Sum price of all tickets: ", sum_price_of_ticket)
