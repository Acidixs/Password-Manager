import random


def newPassword():

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    newPass = []

    for l in alphabet:
        randomLetter = alphabet[random.randint(0,25)]
        newPass.append(randomLetter)
        newPassLength = newPass[0:passLength]


    print("".join(newPassLength))


passLength = (int(input("Choose password length: ")))

newPassword()

