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
        chars = self.load_config()
        password = "".join(map(str, [random.choice(chars) for _ in range(length)]))
        return password

        # saves password to passwords.txt
    def save_pass_to_file(self, paswd):
        with open("passwords.txt", "a+") as f:
            f.write((paswd + "\n"))


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
        
    def get_length(self):
        while True:
            try:
                length = int(input("Enter password length: "))
                return length
            except ValueError:
                print("Please enter a number!")
                continue


    def login(self):
        login = input("Enter master password: ")
        if Database().check_hash(login):
            print("Logged in.")
            self.run()
        else:
            print("Master password incorrect!")
            self.login()



    def run(self):
        while True:
            length = self.get_length()
            pw = self.newPassword(length)
            self.save_pass_to_file(pw)
            print(pw)

            


if __name__ == "__main__":
    app = PasswordGenerator()
    app.check_config()
    app.login()
