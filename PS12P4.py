def scroll_text(text, number_of_characters_per_line, number_of_lines, direction):
    text = text.strip()
    repeated_text = (text * ((number_of_characters_per_line // len(text)) + 1))[:number_of_characters_per_line]

    for i in range(number_of_lines):
        if direction == "right":
            shifted_text = repeated_text[-(i + 1):] + repeated_text[:-(i + 1)]
        elif direction == "left":
            shifted_text = repeated_text[(i + 1):] + repeated_text[:(i + 1)]
        else: 
            print("Invalid direction.")
            return
        
        print(shifted_text)

line_of_text = input("Enter a line of text: ")
number_of_characters_per_line = int(input("Enter the number of characters per line: "))
number_of_lines = int(input("Enter the number of lines to print: "))
direction = input("Enter the scroll direction (right/left): ").lower()

scroll_text(line_of_text, number_of_characters_per_line, number_of_lines, direction)
