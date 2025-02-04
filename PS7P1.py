#input phase 
principle_amount = float(input("Enter principle amount:"))
interest_rate = float (input("Enter interest rate:"))

beginning_balance = principle_amount
total_interest = 0

print("Year", "   Beginning balance", "   Ending balance")

for Year in range (1,6,1):
    interest = beginning_balance * interest_rate
    ending_balance = beginning_balance + interest
    total_interest = total_interest + interest
    print(Year, "          ", beginning_balance,"              ",ending_balance)
    
    beginning_balance = ending_balance
    
response = input("Do you want to calculate interest? (yes/no)")

#output phase
print("Accumulated interest for the 5 years: ", total_interest)
