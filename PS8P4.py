def compute_pay_rate(job_code):
    if job_code == "L":
        pay_rate = 25
    elif job_code == "A":
        pay_rate = 30
    elif job_code == "J":
        pay_rate = 50
    else:
        print("You must enter 'L', 'A', or 'J'.")
        exit()
    return pay_rate

total_of_all_gross_pay = 0
user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    last_name = input("Enter last name:")
    job_code = input("Enter job code:")
    hours_worked = float(input("Enter hours worked:"))
    pay_rate = compute_pay_rate(job_code)

    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate
    else:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (1.5 * pay_rate)
        gross_pay = regular_pay + overtime_pay
    
    total_of_all_gross_pay = total_of_all_gross_pay + gross_pay
    
    print("Last name: ", last_name)
    print("Gross pay: ", gross_pay)

    user_choice = input("Do you want to do the program again? (yes/no)")

print("Total of all gross pay: ", total_of_all_gross_pay)
