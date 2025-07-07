import hashlib
import os

def create_master_key():
    master = "master_key.txt"
    if os.path.exists(master):
        print("Master key already exists.")
        return
    master_key = input("Create a master key: ")
    hashed_key = hashlib.sha256(master_key.encode()).hexdigest()
    
    with open(master,"w") as f:
        f.write(hashed_key)
    
    print("Master key saved successfully.")
create_master_key()
