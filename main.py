import random



def newPassword():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    alphabetUpper = [c.upper() for c in alphabet]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    newPass = []
    defaultLength = 50

    while defaultLength > 0:
        randomLetter = alphabet[random.randint(0, 25)]
        randomNumber = numbers[random.randint(0, 9)]
        randomUpperLetter = alphabetUpper[random.randint(0, 25)]

        newPass.append(randomLetter)
        newPass.append(randomUpperLetter)
        newPass.append(randomNumber)

        defaultLength -= 1

    newPassLength = ("".join([str(i) for i in newPass]))
    print(newPassLength[0:passlength])

    def save_pass_to_file():
        with open("passwords.txt", "w") as f:
            f.write(newPassLength)


passlength = (int(input("Enter password length: ")))
newPassword()
