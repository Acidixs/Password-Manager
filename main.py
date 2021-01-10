# Password generator by Acidix

import random
import string
import json
import os.path
import bcrypt
from database import Database

class PasswordGenerator:
    def __init__(self):
        self.alphabetLower = list(string.ascii_lowercase)
        self.alphabetUpper = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = list(string.punctuation)


    def newPassword(self, length):
        newPass = []
        chars = self.load_config()

        # generates random characters
        for _ in range(length):
            newPass.append(random.choice(chars))

        # converts list to string
        newPass = ("".join([str(i) for i in newPass]))
        return newPass

        # saves password to passwords.txt
    def save_pass_to_file(self, paswd):
        with open("passwords.txt", "a+") as f:
            f.write((paswd + "\n"))


    def valid_length(self, length):
        return 0 < length <= 100

    def load_config(self):
        included = []
        with open("config.json", "r") as f:
            data = json.load(f)
        
        if data["included"][0]["lower"]:
            included.extend(self.alphabetLower)

        if data["included"][0]["upper"]:
            included.extend(self.alphabetUpper)

        if data["included"][0]["numbers"]:
            included.extend(self.numbers)

        if data["included"][0]["symbols"]:
            included.extend(self.symbols)
        
        return included

        
    def check_config(self):
        if os.path.isfile("config.json"):
            print("Config found!")
        else:
            included = {}
            included["included"] = []
            included["included"].append(
                        {"lower": True,
                        "upper": True,
                        "numbers": True,
                        "symbols": True})

            print("Config missing. Creating one...")
            with open("config.json", "w+") as f:
                json.dump(included, f, indent=4)

            print("File created.")


    def run(self):
        while True:
            login = input("Enter master password: ")
    
            if Database().check_hash(login):
                print("Logged in!")
            else:
                print("wrong password")
                continue

            try:
                length = (int(input("Enter password length: ")))
                if self.valid_length(length):
                    self.save_pass_to_file(self.newPassword(length))
                    print(self.newPassword(length))
                else:
                    print("(!) Password length must be 1-100")
                    continue
            except ValueError:
                print("(!) You need to enter an int value!")
                continue

if __name__ == "__main__":
    app = PasswordGenerator()
    app.check_config()
    app.run()
