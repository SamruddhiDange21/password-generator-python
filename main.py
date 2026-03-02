import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

while True:
    print("\nPassword Tool")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)

    elif choice == "2":
        password = input("Enter password: ")
        print("Password Strength:", check_strength(password))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")