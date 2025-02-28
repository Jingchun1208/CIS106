def process_text(text):
    cleaned_text = ' '.join(text.split())
    reversed_text = ''.join(reversed(text))
    return reversed_text

line_of_text = input("Enter a line of text: ")

result = process_text(line_of_text)
print(result)
