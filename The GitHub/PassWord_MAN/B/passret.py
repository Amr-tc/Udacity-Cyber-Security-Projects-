import hashlib
import os
from cryptography.fernet import Fernet

master = "master_key.txt"
passwords = "passwords.txt"

def verify_master_key():
    if not os.path.exists(master):
        print("Err : create a master key first")
        return False

    master_key = input("Enter your master key: ")
    hashed_key = hashlib.sha256(master_key.encode()).hexdigest()

    with open(master, "r") as f:
        stored_hashed_key = f.read().strip()

    return hashed_key == stored_hashed_key

def dec_pwd(enc_pwd: str, key: str):
    return Fernet(key.encode()).decrypt(enc_pwd.encode()).decode()

def retrieve_pwd():
    if not verify_master_key():
        print("Incorrect master key.")
        return

    site = input("Enter domain to retrieve password: ")

    if not os.path.exists(passwords):
        print("Password file not found.")
        return

    with open(passwords, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == site:
                user = lines[i + 1].strip()[1:]  
                key = lines[i + 2].strip()[1:]   
                enc = lines[i + 3].strip()[1:]
                
                decrypted_pwd = dec_pwd(enc, key)
                print(f"Username: {user}")
                print(f"Password: {decrypted_pwd}")
                return
    print("Domain not found.")
retrieve_pwd()
