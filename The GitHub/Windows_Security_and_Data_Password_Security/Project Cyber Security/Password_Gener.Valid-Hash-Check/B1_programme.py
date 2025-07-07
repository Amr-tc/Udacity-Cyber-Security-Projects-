import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    length = 12  # Fixed length for the password. You can change it if you like.
    password = ""

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    # Check if password contains uppercase letters, symbols, and digits
    chk_upper = any(char.isupper() for char in password)
    chk_symbol = any(char in string.punctuation for char in password)
    chk_digit = any(char.isdigit() for char in password)

    # If all criteria are met, return the password
    if chk_upper and chk_symbol and chk_digit:
        return password
    # Otherwise, recursively call pass_gen() until a strong password is generated
    else:
        return generate_password()


'''
# Do not change the code below
'''
# Generate a password that meets the criteria
password = generate_password()
print(password)

