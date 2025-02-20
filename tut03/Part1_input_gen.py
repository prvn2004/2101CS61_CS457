import random
import string

def generate_password(length=8):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(all_chars, k=length))

with open("input.txt", "w") as file:
    for _ in range(1000):
        length = random.randint(5, 16)  # Passwords with random length between 5 and 16
        file.write(generate_password(length) + "\n")

print("File 'input.txt' created with 1000 passwords.")
