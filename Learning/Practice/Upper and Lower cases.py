# Input string
input_string = input("Enter a string: ")

# Convert the case of each character
converted_string = ""
for char in input_string:
    if char.islower():
        converted_string += char.upper()
    elif char.isupper():
        converted_string += char.lower()
    else:
        converted_string += char

# Print the converted string
print("Converted string:", converted_string)
