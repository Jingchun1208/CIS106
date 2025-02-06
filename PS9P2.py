def compute_batting_average(number_of_hits, at_bats_at_the_keyboard):
    batting_average = number_of_hits / at_bats_at_the_keyboard
    return batting_average

count_of_the_number_of_players = 0
player_choice = input("Do you want to do the program? (yes/no)")

while player_choice == "yes":
    last_name = input("Enter last name:")
    number_of_hits = float(input("Enter number of hits:"))
    at_bats_at_the_keyboard = float(input("Enter at bats at the keyboard:"))
    batting_average = compute_batting_average(number_of_hits, at_bats_at_the_keyboard)

    count_of_the_number_of_players = count_of_the_number_of_players + 1

    print("Last name: ", last_name)
    print("Batting average: ", batting_average)

    player_choice = input("Do you want to do the program again? (yes/no)")

print("Number of players: ", count_of_the_number_of_players)
