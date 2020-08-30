import random


def newPassword():

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    newPass = []
    value = 0

    while value < passlength:

         randomLetter = alphabet[random.randint(0,25)]
         randomNumber = numbers[random.randint(0,9)]
         newPass.append(randomNumber)
         newPass.append(randomLetter)
         value += 2


    print("".join([str(i) for i in newPass]))


passAmount = (int(input("Amount of passwords to generate: ")))
passlength = (int(input("Enter password length: ")))
newPassword()
