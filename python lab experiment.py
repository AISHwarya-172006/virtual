character = input("Enter a single character: ")
if len(character) != 1:
    print("Please enter exactly one character.")
else:
    if '0' <= character <= '9':
        print("The character is a digit.")
    elif 'a' <= character <= 'z':
        print("The character is a lowercase letter.")
    elif 'A' <= character <= 'Z':
        print("The character is an uppercase letter.")
    else:
        print("The character is a special character.")
