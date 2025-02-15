def compute_assessed_value (county, market_value):
    if county == "cook":
        assessed_value_percent = 0.9
    elif county == "DuPage":
        assessed_value_percent = 0.8
    elif county == "McHenry":
        assessed_value_percent = 0.75
    elif county == "Kane":
        assessed_value_percent = 0.6
    else: assessed_value_percent = 0.7

    assessed_value = market_value * assessed_value_percent
    return assessed_value

total_market_value = 0
total_assessed_value = 0
user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    county = input("Enter county:")
    market_value = float(input("Enter market value:"))
    assessed_value = compute_assessed_value (county, market_value)
    total_market_value = total_market_value + market_value
    total_assessed_value = total_assessed_value + assessed_value

    print("County: ", county)
    print("Market value: ", market_value)
    print("Assessed value: ", assessed_value)

    user_choice = input("Do you want to do the program? (yes/no)")
    
print("Total market value: ", total_market_value)
print("Total assessed value: ", total_assessed_value)
