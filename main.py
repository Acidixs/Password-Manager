# Password generator by Aleksander Bø
import random
import string


def newPassword():
    alphabet = list(string.ascii_lowercase)
    alphabetUpper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    newPass = []
    defaultLength = 50

    while defaultLength > 0:
        randomLetter = random.choice(alphabet)
        randomUpperLetter = random.choice(alphabetUpper)
        randomNumber = random.choice(numbers)
        randomSymbol = random.choice(symbols)

        randomChar = [randomLetter, randomUpperLetter, randomNumber, randomSymbol]

        newPass.append(random.choice(randomChar))

        defaultLength -= 1

    newPass = ("".join([str(i) for i in newPass]))
    print(newPass[0:passlength])

    def save_pass_to_file():
        with open("passwords.txt", "a") as f:
            f.write((newPass[0:passlength]) + "\n")
            f.close()

    save_pass_to_file()


passlength = (int(input("Enter password length: ")))
newPassword()
