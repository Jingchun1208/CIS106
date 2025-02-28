def add_numbers_to_list1(number_list):
    x = int(input("How many items are in the list? "))
    for _ in range(x):
        i = int(input("Please enter a number: "))
        number_list.append(i)
    return number_list  

def add_numbers_to_list2(number_list):
    number_list.insert(0, 99)

def add_number_to_list3(number_list):
    number_list[0] = 100

def add_numbers_to_list4(number_list, number_list2):
    number_list.extend(number_list2)

def remove_value(number_list):
    number_list.remove(800)

def remove_value_from_list2(number_list):
    number_list.remove(700)  # Assuming you meant to remove a specific value here

def display(number_list):
    for z in number_list:
        print(z)

def count_a_gradea(grades_list):
    print("There are", grades_list.count("A"), "A grades.")

def count_a_gradeb(grades_list):
    print("The first 'B' is at position", grades_list.index("B"))

def check_f_grade(grades_list):
    if "F" in grades_list:
        print("There is F in the list.")
    else:
        print("Grade F is not in the list.")

def clear_second_list(number_list):
    number_list.clear()

def delete_second_list():
    second_list = [500, 600, 700, 800, 900]
    del second_list
    print("second_list deleted.")

def playersort(players):
    players.sort()
    for i in players:
        print(i)

def copyplayers(players, players2):
    y = players.copy()
    players2.append(y)
    for y in players2:
        print(y)
    return players2

def backwards(players, players2):
    players.sort()
    for t in players:
        print(t)
    z = players.copy()
    players2.append(z)
    w = reversed(players)
    print(list(w))


# Running the code for each function in sequence
number_list = []
number_list = add_numbers_to_list1(number_list)
add_numbers_to_list2(number_list)
add_number_to_list3(number_list)

number_list2 = [500, 600, 700, 800, 900]
add_numbers_to_list4(number_list, number_list2)

remove_value(number_list)

# Add additional code to remove a specific value, like 800
remove_value_from_list2(number_list)

display(number_list)

grades_list = ["A", "B", "C", "A", "A", "C"]
count_a_gradea(grades_list)
count_a_gradeb(grades_list)
check_f_grade(grades_list)

clear_second_list(number_list)
delete_second_list()

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players2 = []
playersort(players)
copyplayers(players, players2)
backwards(players, players2)
