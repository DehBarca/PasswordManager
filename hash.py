import maskpass
import hashlib
import json

def ask():
    username = input("Enter your username: ")
    password =  maskpass.askpass(prompt="Enter your password: ", mask="*")

    passwords = {}
    passwords[username] = hashlib.sha256(password.encode('utf8')).hexdigest()
    print(passwords)
    return passwords

def save():
    file = open('data.txt', 'a')
    file.write(json.dumps(ask()))

print(save())