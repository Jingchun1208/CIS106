student_count = 0 

user_choice = input("Whether you what to do this program? (yes/no)")
while user_choice == "yes":
    #input phase
    last_name = input("Enter last name")
    exam1_score = float(input("Enter exam1 score"))
    exam2_score = float(input("Enter exam2 score"))
    #process phase
    average_score = (exam1_score + exam2_score) / 2 
    
    student_count = student_count + 1

    #output phase
    print("Last name: ", last_name)
    print("Average score: ", average_score)
    
    user_choice = input("Whether you what to do this program again? (yes/no)")

print("Number of students who entered data: ", student_count)
