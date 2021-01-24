import json
import string
import random

class PasswordGenerator:
    def __init__(self):
        self.alphabetLower = list(string.ascii_lowercase)
        self.alphabetUpper = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = list(string.punctuation)

    def new_password(self, length):
        chars = self.load_config()
        password = "".join(map(str, [random.choice(chars) for _ in range(length)]))
        return password

    def get_pw_length(self):
        while True:
            try:
                length = int(input("Enter password length: "))
                return length
            except ValueError:
                print("Please enter a number!")
                continue

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