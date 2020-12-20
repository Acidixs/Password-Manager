# Password generator by Acidix

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.alphabetLower = list(string.ascii_lowercase)
        self.alphabetUpper = list(string.ascii_uppercase)
        self.numbers = list(string.digits)
        self.symbols = list(string.punctuation)


    def newPassword(self, length):
        newPass = []

        # generates random characters
        for _ in range(length):
            randomChar = random.choice(self.alphabetLower + self.alphabetUpper + self.numbers + self.symbols)
            newPass.append(randomChar)

        # converts list to string
        newPass = ("".join([str(i) for i in newPass]))
        print(newPass)

        # saves password to passwords.txt
    def save_pass_to_file(self, paswd):
        with open("passwords.txt", "a+") as f:
            f.write((paswd + "\n"))


    def valid_length(self, length):
        return 0 < length <= 100


    def run(self):
        while True:
            try:
                paswd = (int(input("Enter password length: ")))
                if self.valid_length(paswd):
                    self.newPassword(paswd)
                    self.save_pass_to_file(paswd)
                else:
                    print("(!) Password length must be 1-100")
                    continue
            except ValueError:
                print("(!) You need to enter an int value!")
                continue

if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()

