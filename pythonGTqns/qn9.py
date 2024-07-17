#Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.


import random 
import string
def generate_password(length=12):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    all_characters = upper + lower + special  + digits

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
    ]
    password += random.choices(all_characters,k=length-4)

    random.shuffle(password)
    return "".join(password)
password = generate_password(12)
print(f"Generated password :{password}")