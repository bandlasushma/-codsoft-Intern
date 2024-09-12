import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Ask the user for the password length
    length = int(input("Enter the desired password length (e.g., 12): "))
    
    # Generate the password
    password = generate_password(length)
    
    print(f"Generated Password: {password}")

if __name__ == "_main_":
    main()
