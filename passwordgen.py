import random

def password_generator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print(password_generator(10))