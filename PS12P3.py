def comma_separated_values(line):
    items = line.split(',')
    for item in items:
        print(item.strip())

line_of_values = input("Enter a line of comma-separated values: ")

comma_separated_values(line_of_values)
