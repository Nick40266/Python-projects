## Password saver
import csv
import os
import getpass
from cryptography.fernet import Fernet

if not os.path.exists("key.key"):
    with open("key.key", "wb") as k:
        k.write(Fernet.generate_key())

with open("key.key", "rb") as k:
    key = k.read()
lock = Fernet(key)



def add():
    acc = input("Account name: ")
    pwd = getpass.getpass("Password: ")
    with open("passwords.csv", "a", newline="") as f:
        
        doc = csv.DictWriter(f, fieldnames=["Account", "Password"])
        if f.tell() == 0:    
            doc.writeheader()

        doc.writerow({"Account":acc, "Password":lock.encrypt(pwd.encode()).decode()})

def view():
    with open("passwords.csv", "r") as f:
        doc = csv.DictReader(f)
        for line in doc:
            line["Password"] = lock.decrypt(line["Password"].encode()).decode()
            print(line)

while True:
    purpose = input("Would you like to add or view a password? (Enter add | view | q to quit) ")
    if purpose == "add":
        add()
    elif purpose == "view":
        view()
    elif purpose == "q":
        break
    else:
        print("Invalid choice")        