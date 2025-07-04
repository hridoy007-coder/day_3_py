import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letteres =string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # print(letteres, digits, special)
    characters = letteres
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return password

min_length = int(input("Enter the minimum length of the password: "))
has_numbers = input("Include numbers? (yes/no): ").lower() == "y"
has_special = input("Include special characters? (yes/no): ").lower() == "y"
password = generate_password(min_length, has_numbers, has_special)
print("The generated password is:", password)