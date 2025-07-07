import hashlib
import os
from cryptography.fernet import Fernet

def gen_key():
    return Fernet.generate_key().decode()

def enc_pwd(pwd: str, key: str):
    return Fernet(key.encode()).encrypt(pwd.encode()).decode()

def save_pwd():
    file = "passwords.txt"
    site = input("Enter domain: ")
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    key = gen_key()
    enc = enc_pwd(pwd, key)
    hash_ = hashlib.sha256(pwd.encode()).hexdigest()
    
    with open(file,"a") as f:
        f.write(f"{site}\n:{user}\n:{key}\n:{enc}\n:{hash_}\n")
    print("Password saved.")

save_pwd()
