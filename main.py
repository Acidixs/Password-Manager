import random
import string


def newPassword():
    alphabet = list(string.ascii_lowercase)
    alphabetUpper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    newPass = []
    defaultLength = 50

    while defaultLength > 0:
        randomLetter = random.choice(alphabet)
        randomNumber = random.choice(numbers)
        randomUpperLetter = random.choice(alphabetUpper)

        newPass.append(randomLetter)
        newPass.append(randomUpperLetter)
        newPass.append(randomNumber)

        defaultLength -= 1

    newPassLength = ("".join([str(i) for i in newPass]))
    print(newPassLength[0:passlength])

    def save_pass_to_file():
       with open("passwords.txt", "a") as f:
        f.write((newPassLength[0:passlength])+"\n")
        f.close()

    save_pass_to_file()


passlength = (int(input("Enter password length: ")))
newPassword()
#Hello