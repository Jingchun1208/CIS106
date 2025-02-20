def compute_commission_and_target (sales):
    if sales > 100000:
        commission = sales * 0.1
    else: commission = sales * 0.05
    
    next_year_target = sales * 1.05
    return commission, next_year_target

last_name = input("Enter last name:")
sales = float(input("Enter sales:"))
commission, next_year_target = compute_commission_and_target (sales)

print("Last name:", last_name)
print("Commission:", commission)
print("Next year target:", next_year_target)
