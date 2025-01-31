sum_of_all_the_gross_pay= 0
number_of_employees= 0

employee_choice = input("Do you want to do this program? (yes/no)")
while employee_choice == "yes":
    #input phase
    last_name = input("Enter last name")
    hours_worked = float(input("Enter hours worked"))
    rate_of_pay = float(input("Enter rate of pay"))
    #process phase
    if hours_worked > 40:
        over_time_pay = (hours_worked - 40) * (rate_of_pay * 1.5)
        regular_pay = 40 * rate_of_pay 
        gross_pay = regular_pay + over_time_pay
    else: gross_pay = hours_worked * rate_of_pay
    sum_of_all_the_gross_pay = sum_of_all_the_gross_pay + gross_pay
    number_of_employees = number_of_employees + 1
    
    employee_choice = input("Do you want to do this program again? (yes/no)")

average_pay = sum_of_all_the_gross_pay / number_of_employees

 #output phase
print("Sum of all the gross pay: ", sum_of_all_the_gross_pay)
print("Number of employees: ", number_of_employees)
print("Average pay: ", average_pay)
