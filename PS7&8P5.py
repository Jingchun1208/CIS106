#input phase
f = open("Code/PS7P5.txt", "r")

total_tuition = 0
number_of_students = 0 

last_name = str(f.readline().rstrip('\n'))

#process phase
while last_name != "":
    district_code = f.readline()
    credits = float(f.readline())

    if district_code == "I\n":
        cost_per_credit = 250
    else: cost_per_credit = 500
    tuition = cost_per_credit * credits
    number_of_students = number_of_students + 1
    total_tuition = total_tuition + tuition
    #output phase
    print("Last name: ", last_name)
    print("Tuition: ", tuition)
    print("Credit: ", credits)
    
    last_name = str(f.readline().rstrip('\n'))
f.close()

#output phase
print("Total tuition: ", total_tuition)
print("Total number of students: ", number_of_students)
