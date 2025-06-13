from cryptography.fernet import Fernet

'''def setup_master_password():
    password = input("Set a new master password: ")

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    fer = Fernet(key)
    encrypted_password = fer.encrypt(password.encode())

    with open("master_pass.key", "wb") as f:
        f.write(encrypted_password)

setup_master_password()'''

from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as f:
        return f.read()

def load_encrypted_master():
    with open("master_pass.key", "rb") as f:
        return f.read()

input_password = input("Enter the master password: ")

key = load_key()
fer = Fernet(key)

try:
    encrypted_master = load_encrypted_master()
    decrypted_master = fer.decrypt(encrypted_master).decode()
    is_real_user = (input_password == decrypted_master)
except Exception as e:
    is_real_user = False 

fer_pwd = Fernet(key) if is_real_user else None


def view_real():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            user, passw = line.strip().split("|")
            print("User:", user, "| Password:", fer_pwd.decrypt(passw.encode()).decode())

def view_fake():
    print("User: discord | Password: dragon123")
    print("User: steam | Password: gamerx")

def add_real():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted = fer_pwd.encrypt(pwd.encode()).decode()
    with open("password.txt", "a") as f:
        f.write(name + "|" + encrypted + "\n")

def add_fake():
    input("Account Name: ")
    input("Password: ")
    print("✅ Password saved.")  # Fake

while True:
    mode = input("Add or view passwords? (add/view), or 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add_real() if is_real_user else add_fake()
    elif mode == "view":
        view_real() if is_real_user else view_fake()
    else:
        print("Invalid option.")

