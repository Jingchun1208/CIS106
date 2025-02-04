#input phase
f = open("Code/PS7P3.txt", "r")

total_sum_of_bonuses_paid = 0
last_name = f.readline().rstrip()

#process phase
while last_name != "":  
    salary = f.readline()
    salary = float(salary) 
    if salary >= 100000:
        bonus_rate = 0.2
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.1
    
    bonus = salary * bonus_rate
    total_sum_of_bonuses_paid = total_sum_of_bonuses_paid + bonus
    
    #output phase
    print("Last name: ", last_name)
    print("Salary: ", salary)
    print("Bonus: ", bonus)

    last_name = str(f.readline().rstrip('\n'))

f.close()   

#output phase
print("Total sum of bonuses paid: ", total_sum_of_bonuses_paid)
