def compute_tuition_owed(credit_hours, district_code):
    if district_code == "I":
       tuition_owed = 250 * credit_hours
    elif district_code == "O":
        tuition_owed = 550 * credit_hours
    else: 
        print("You must enter I or O") 
        exit()
    return tuition_owed

total_of_all_tuition_owed = 0
user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    student_last_name = input("Enter student last name:")
    credit_hours = float(input("Enter credit hours:"))
    district_code = input("Enter district code:")
    tuition_owed = compute_tuition_owed(credit_hours, district_code)
    total_of_all_tuition_owed = total_of_all_tuition_owed + tuition_owed

    print("Student name: ", student_last_name)
    print("Tuition owed: ", tuition_owed)
    
    user_choice = input("Do you want to do the program again? (yes/no)")

print("Total of all tuition owed: ", total_of_all_tuition_owed)
