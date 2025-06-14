import random
import string
import json
import os

DATA_FILE = "passwords.json"

def generate_password(length=12):
    if length < 4:
        return "Password too short!"
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(chars, length))

def save_password(service, username, password):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data[service] = {"username": username, "password": password}

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Password saved successfully!")

def view_password(service):
    if not os.path.exists(DATA_FILE):
        print("No passwords saved yet.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if service in data:
        print(f"\nService: {service}")
        print(f"Username: {data[service]['username']}")
        print(f"Password: {data[service]['password']}")
    else:
        print("No entry found for this service.")

def main():
    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Generate & Save Password")
        print("2. View Saved Password")
        print("3. Exit")

        choice = input("Choose an option (1–3): ")

        if choice == "1":
            service = input("Enter service name (e.g., Gmail): ")
            username = input("Enter your username/email: ")
            length = int(input("Enter desired password length: "))
            password = generate_password(length)
            print("Generated Password:", password)
            save_password(service, username, password)

        elif choice == "2":
            service = input("Enter service name to view: ")
            view_password(service)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
