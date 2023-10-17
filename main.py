import random
import string

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    if use_digits:
        if length < 6:
            raise ValueError("For passwords with digits, length must be at least 6 characters.")

    if use_special:
        if length < 8:
            raise ValueError("For passwords with special characters, length must be at least 8 characters.")

    password = random.sample(characters, length)
    random.shuffle(password)
    return ''.join(password)

try:
    password_length = int(input("Enter the desired password length: "))
    use_digits = input("Use digits in the password? (yes/no): ").lower() == "yes"
    use_special = input("Use special characters in the password? (yes/no): ").lower() == "yes"

    password = generate_password(password_length, use_digits, use_special)
    print("Random Password:", password)
except ValueError as e:
    print("Error:", e)
except KeyboardInterrupt:
    print("\nPassword generation canceled.")
