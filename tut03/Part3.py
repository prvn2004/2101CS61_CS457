def validate_password(password, criteria):
    if len(password) < 8:
        return "skip"  # Skip validation for passwords with length < 8

    valid = True
    if 1 in criteria and not any(char.isupper() for char in password):
        valid = False
    if 2 in criteria and not any(char.islower() for char in password):
        valid = False
    if 3 in criteria and not any(char.isdigit() for char in password):
        valid = False
    if 4 in criteria:
        special_chars = "!@#"
        if not any(char in special_chars for char in password):
            valid = False
        elif any(char not in special_chars and not char.isalnum() for char in password):
            valid = False

    return "valid" if valid else "invalid"

def main():
    print("Select the criteria to check (Enter numbers separated by commas):")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Special characters (!, @, #)")

    user_input = input("Enter your choices (e.g., 1,3,4): ")
    criteria = [int(choice.strip()) for choice in user_input.split(",") if choice.strip().isdigit()]

    valid_count = 0
    invalid_count = 0
    skipped_count = 0

    with open("input.txt", "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        result = validate_password(password, criteria)
        if result == "valid":
            valid_count += 1
        elif result == "invalid":
            invalid_count += 1
        elif result == "skip":
            skipped_count += 1

    print("\nResults:")
    print(f"Total passwords checked: {len(passwords)}")
    print(f"Valid passwords: {valid_count}")
    print(f"Invalid passwords: {invalid_count}")
    print(f"Skipped (less than 8 characters): {skipped_count}")

if __name__ == "__main__":
    main()
