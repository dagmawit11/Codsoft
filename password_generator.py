import random
import string

def generate_password(length):
    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters into one string
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining length of the password with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the resultant password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def main():
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length for the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and display the password
    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()