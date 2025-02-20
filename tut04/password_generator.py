import random
import string

# List of common dictionary words (for weak passwords)
dictionary_words = [
    "password", "123456", "qwerty", "letmein", "monkey", "sunshine", "football",
    "iloveyou", "admin", "welcome", "123abc", "password1", "superman", "batman",
    "dragon", "hello", "shadow", "trustno1", "flower", "butterfly", "sunflower"
]

# Function to generate a strong password
def generate_strong_password():
    length = random.randint(12, 16)  # Random length between 12 and 16
    upper = random.choices(string.ascii_uppercase, k=2)
    lower = random.choices(string.ascii_lowercase, k=4)
    digits = random.choices(string.digits, k=3)
    special = random.choices("!@#$%^&*()_+-=[]{}|;:,.<>?/~", k=2)
    all_chars = upper + lower + digits + special
    random.shuffle(all_chars)
    return "".join(all_chars)

# Function to generate a weak password
def generate_weak_password():
    choice = random.choice(["short", "dictionary", "simple"])
    if choice == "short":
        return "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 8)))
    elif choice == "dictionary":
        return random.choice(dictionary_words)
    else:  # "simple"
        return random.choice(dictionary_words) + str(random.randint(1, 99))

# Generate 1000 passwords (50% strong, 50% weak)
passwords = []
for _ in range(500):
    passwords.append(generate_strong_password())  # Strong passwords
    passwords.append(generate_weak_password())    # Weak passwords

# Shuffle passwords to mix strong and weak ones
random.shuffle(passwords)

# Save passwords to input.txt
with open("input.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")

print("Generated 1000 passwords and saved them to input.txt.")
