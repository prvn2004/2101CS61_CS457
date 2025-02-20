import re

def validate_password(password, criteria):
    reasons = []  # List to store all missing requirements

    # Check for prohibited characters (always invalid)
    if re.search(r"[^a-zA-Z0-9!@#]", password):  
        reasons.append("Password contains prohibited characters.")

    # Check for required criteria
    if 1 in criteria and not re.search(r"[A-Z]", password):
        reasons.append("Password must contain at least one uppercase letter.")
    if 2 in criteria and not re.search(r"[a-z]", password):
        reasons.append("Password must contain at least one lowercase letter.")
    if 3 in criteria and not re.search(r"[0-9]", password):
        reasons.append("Password must contain at least one digit.")
    if 4 in criteria and not re.search(r"[!@#]", password):
        reasons.append("Password must contain at least one special character (!, @, #).")

    # If there are no reasons, password is valid
    if not reasons:
        return "valid"
    
    # Return the list of reasons why the password is invalid
    return reasons

def main():

    print("Enter the criteria to check (separated by commas):")
    print("1: Uppercase letters (A-Z) - Presence REQUIRED if in criteria, PROHIBITED if NOT")
    print("2: Lowercase letters (a-z) - Presence REQUIRED if in criteria, PROHIBITED if NOT")
    print("3: Numbers (0-9) - Presence REQUIRED if in criteria, PROHIBITED if NOT")
    print("4: Special characters (!, @, #) - Presence REQUIRED if in criteria, PROHIBITED if NOT")

    try:
        criteria_input = input("Enter criteria (e.g., 1,3,4): ")
        criteria = [int(c.strip()) for c in criteria_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    valid_count = 0
    invalid_count = 0
    skipped_count = 0  

    password_list = [
    "abc12345",  
    "abc",  
    "123456789",  
    "abcdefg$",  
    "abcdefgABHD!@313",  
    "abcdefgABHD$$!@313",  
    "MyPassword123!",  
    "admin@1234",  
    "welcome@2025",  
    "Password1!",  
    "test@12345",  
    "qwerty12345",  
    "helloWORLD@2025",  
    "P@ssw0rD",  
    "complexPassword1234!@",  
    "SimplePass1",  
    "Test@1234#",  
    "admin1234",  
    "12345!@#",  
    "secure$Passw0rd",  
    "Alpha123!@#456",  
    "LongPassw0rd$WithSpecialChars",  
    "TooShort",  
    "qwerty!@",  
    "123!ABCabc",  
    "!!password999",  
    "goodpass12@",  
    "qwertyuiop!#",  
    "XxYyZz123!",  
    "Complex&Password2025@",  
    "12345Qwerty!",  
    "p@ssWorD1234",  
    "Another#Password1",  
    "Hello@1234!",  
    "321qweR@#$",  
    "Valid@Password12",  
    "Short8!",  
    "ThisIsALongPassword1#!"  
]

    # try:
    #     with open('input.txt', 'r') as file:
    #         password_list = [line.strip() for line in file.readlines()]
    # except FileNotFoundError:
    #     print("The file 'input.txt' was not found.")
    #     return



    for password in password_list:
        if len(password) < 8:
            print(f"Password '{password}' is too short (less than 8 characters). Skipping validation.")
            skipped_count += 1
            continue

        validation_result = validate_password(password, criteria)

        if validation_result == "valid":
            print(f"Password '{password}' is valid.")
            valid_count += 1
        else:
            # If invalid, print all the reasons for invalidity
            print(f"Password '{password}' is invalid: {', '.join(validation_result)}")
            invalid_count += 1

    print("\n--- Summary ---")
    print(f"Valid passwords: {valid_count}")
    print(f"Invalid passwords: {invalid_count}")
    print(f"Skipped (too short): {skipped_count}")

if __name__ == "__main__":
    main()
