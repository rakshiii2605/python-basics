import random
import string

def generate_password(length=8, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""
    
    all_chars = letters + digits + symbols
    if not all_chars:
        return "Error: No characters selected!"
    
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    choice = input("Include symbols? (y/n): ").lower() == "y"
    print("Generated Password:", generate_password(length, choice))
