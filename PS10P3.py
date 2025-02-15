def compute_out_the_door_price (make, model, msrp, electric_vehicle_code):
    if make == "Honda" and model == "Accord":  
       percent_off = 0.1
    elif make == "Toyota" and model == "Rav4":
         percent_off = 0.15
    elif electric_vehicle_code == "Y":
         percent_off = 0.3
    else: percent_off = 0.05
    
    discount=percent_off * msrp
    newmsrp = msrp - discount
    msrpwtax = newmsrp*1.07
    return newmsrp, msrpwtax
    

total_MSRP_sum = 0
sum_of_sales_price = 0 
user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    make = input("Make:")
    model = input("Model:")
    electric_vehicle_code = input("Electric vehicle code:")
    msrp = float(input("MSRP:"))
    newmsrp, msrpwtax = compute_out_the_door_price(make, model, msrp, electric_vehicle_code)
    total_MSRP_sum = total_MSRP_sum + msrp
    sum_of_sales_price = sum_of_sales_price + msrpwtax

    print("MSRP: ", msrp)
    print("Discounted MSRP: ", newmsrp)
    print("MSRP with tax: ", msrpwtax)

    user_choice = input("Do you want to do the program again? (yes/no)")

print("Total MSRP sum: ", total_MSRP_sum)
print("Sum of sale price: ", sum_of_sales_price)
