import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 8 characters."

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
