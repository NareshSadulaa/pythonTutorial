import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special

    password= ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_Charac = random.choice(characters)
        password += new_Charac

        if new_Charac in digits:
            has_numbers = True
        elif new_Charac in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and  has_special

    return password

min_len = int(input("Enter minimum password length: "))
has_number = input("Do you have numbers? (y/n): ").lower() == "y"
has_specials = input("Do you have special characters? (y/n): ").lower() == "y"
passw = generate_password(min_len, has_number, has_specials)
print("The generated Password is:",passw)