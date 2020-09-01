# Password generator by Acidix

import random
import string


def newPassword():
    alphabetLower = list(string.ascii_lowercase)
    alphabetUpper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    newPass = []

    # generates random characters
    for c in range(passlength):
        randomChar = random.choice(alphabetLower + alphabetUpper + numbers + symbols)

        newPass.append(randomChar)

    # converts list to string
    newPass = ("".join([str(i) for i in newPass]))
    print(newPass)

    def save_pass_to_file():
        with open("passwords.txt", "a") as f:
            f.write((newPass + "\n"))

    save_pass_to_file()


while True:
    try:
        passlength = (int(input("Enter password length: ")))
        if passlength <= 0 or passlength > 100:
            print("You need to enter a number between 1-100")
            continue

        else:
            newPassword()

    except ValueError:
        print("You need to enter a number between 1-100")
