def format_name(full_name):
    stripped_name = full_name.strip()
    name_parts = stripped_name.split()
    first_name, last_name = name_parts[0], name_parts[1]
    formatted_name = last_name + ", " + first_name[0].upper() + "."
    return formatted_name

user_input = input("Enter your full name (First Last): ")

name = format_name(user_input)
print(name)
