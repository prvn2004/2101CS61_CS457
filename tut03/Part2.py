def validate_password(password, criteria):
    if len(password) < 8:
        print(f"'{password}' is invalid: Less than 8 characters. Skipping validation.")
        return False

    valid = True
    if 1 in criteria and not any(char.isupper() for char in password):
        print(f"'{password}' is invalid: Missing uppercase letters.")
        valid = False
    if 2 in criteria and not any(char.islower() for char in password):
        print(f"'{password}' is invalid: Missing lowercase letters.")
        valid = False
    if 3 in criteria and not any(char.isdigit() for char in password):
        print(f"'{password}' is invalid: Missing numbers.")
        valid = False
    if 4 in criteria:
        special_chars = "!@#"
        if not any(char in special_chars for char in password):
            print(f"'{password}' is invalid: Missing special characters (!, @, #).")
            valid = False
        elif any(char not in special_chars and not char.isalnum() for char in password):
            print(f"'{password}' is invalid: Contains disallowed special characters.")
            valid = False

    if valid:
        print(f"'{password}' is a valid password.")
    return valid

def main():
    password_list = [
        "abc12345", 
        "abc", 
        "123456789", 
        "abcdefg$", 
        "abcdefgABHD!@313", 
        "abcdefgABHD$$!@313"
    ]

    print("Select the criteria to check (Enter numbers separated by commas):")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Special characters (!, @, #)")

    user_input = input("Enter your choices (e.g., 1,3,4): ")
    criteria = [int(choice.strip()) for choice in user_input.split(",") if choice.strip().isdigit()]

    print("\nChecking passwords...\n")
    for password in password_list:
        validate_password(password, criteria)

if __name__ == "__main__":
    main()
