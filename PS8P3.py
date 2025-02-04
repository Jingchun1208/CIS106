def compute_miles_per_gallon(miles_travelled, gallons_used):
    compute_miles_per_gallon =  miles_travelled / gallons_used 
    return compute_miles_per_gallon

number_of_trips = 0

user_choice = input("Do you want to do the program?(yes/no)")

while user_choice == "yes":
    destination_city = input("Enter destination city:")
    miles_travelled = float(input("Enter miles travelled:"))
    gallons_used = float(input("Enter gallons used:"))
    miles_per_gallon = compute_miles_per_gallon(miles_travelled, gallons_used)

    number_of_trips = number_of_trips + 1
    print("Destination city: ", destination_city)
    print("Miles travelled: ", miles_travelled)
    print("Miles per gallon: ", miles_per_gallon)
    
    user_choice = input("Do you want to do the program again?(yes/no)")

print("Number of trips: ", number_of_trips)
