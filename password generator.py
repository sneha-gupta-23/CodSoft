import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    if length < 1:
        return "Error! Password length must be at least 1."

    # Define character sets for password generation
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "Error! No character types selected. Please select at least one character type."

    # Generate a random password using the specified character set
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    print("\n \t*****Password Generator*****")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Password length must be at least 1.")
        except ValueError as ve:
            print(f"Invalid input. {ve}")
            continue

        use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated password: {password}")

        next_password = input("Do you want to generate another password? (yes/no): ")
        if next_password.lower() != 'yes':
            break

if __name__ == "__main__":
    main()