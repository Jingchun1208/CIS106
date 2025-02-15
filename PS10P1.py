def compute_next_month_sales(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar":
        forecast_percent = 0.1
    elif month == "Apr" or month == "May" or month == "Jun":
        forecast_percent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        forecast_percent = 0.2
    elif month == "Oct" or month == "Nov" or month == "Dec":
        forecast_percent = 0.25
    else:
        print("You must enter month.")
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales
    
user_choice = input("Do you want to do the program? (yes/no): ")

while user_choice == "yes":
    last_name = input("Enter last name:")
    month = input("Enter the month:")
    sales = float(input("Enter the sales value: "))
    next_month_sales = compute_next_month_sales(month, sales)
    
    print("Last name: ", last_name)
    print("Month: ", month)
    print("Next month sales: ", next_month_sales)

    user_choice = input("Do you want to do the program again? (yes/no): ")

