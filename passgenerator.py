import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def generate_password(length=14):
    chars = LETTERS + NUMBERS + PUNCTUATION
    password = ""
    for x in range(length):
        password_char = random.choice(chars)
        password = password + password_char
        print(password)

        generate_password()
