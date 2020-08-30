import random


def newPassword():

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    newPass = []
    value = 0

    while value < passlength:


        randomLetter = alphabet[random.randint(0,25)]
        newPass.append(randomLetter)
        value += 1

    print("".join(newPass))


passlength = (int(input("Enter password length: ")))
newPassword()
