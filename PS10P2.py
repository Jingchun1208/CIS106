def compute_square_footage(length, width, height):
    total_square_footage = (2 * length * width + 2 * length * height + 2 * width * height)
    return total_square_footage

user_choice = input("Do you want to do the program? (yes/no)")

while user_choice == "yes":
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))
    total_square_footage = compute_square_footage(length, width, height)
    number_of_gallons = total_square_footage / 50

    print("Square footage of the room: ", total_square_footage)
    print("Number of gallons needed: ", number_of_gallons)

    user_choice = input("Do you want to do the program again? (yes/no)")
