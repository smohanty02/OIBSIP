import hashlib
import os

# Data structure to store user information
users = {}

def register_user():
    print("\n=== Welcome to the Online Book Club Registration ===")
    username = input("Enter your desired username: ")
    if username in users:
        print("Sorry, this username is already taken. Please choose another one.")
        return
    password = input("Create a password: ")
    # Hash and salt the password before storing
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    users[username] = {
        'salt': salt,
        'key': key
    }
    print("Congratulations! You have successfully registered to the Online Book Club.")

def login():
    print("\n=== Welcome to the Online Book Club Login ===")
    username = input("Enter your username: ")
    if username not in users:
        print("User not found. Please register to access the Online Book Club.")
        return
    password = input("Enter your password: ")
    # Retrieve salt and key for the user
    salt = users[username]['salt']
    key = users[username]['key']
    # Hash the provided password with the stored salt
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Compare the hashed passwords
    if new_key == key:
        print("Login successful! Welcome to the Online Book Club.")
        access_book_club(username)
    else:
        print("Invalid password. Please try again.")

def access_book_club(username):
    print("\n=== Online Book Club ===")
    print(f"Welcome, {username}! Here you can discuss your favorite books, share recommendations, and connect with other book lovers.")

def main():
    print("=== Welcome to the Online Book Club ===")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for visiting the Online Book Club. See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
