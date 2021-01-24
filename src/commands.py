from database import Database
from generator import PasswordGenerator

class Commands:
    def __init__(self):
        self.db = Database()
        self.pwg = PasswordGenerator()


    def new(self):
        name = input("Enter a name for the password: ")
        length = self.pwg.get_pw_length()
        pw = self.pwg.new_password(length)
        self.db.add_password(name, pw)
        print("Your new password is: {}".format(pw))

    def save(self):
        name = input("Enter a name for your password: ")
        pw = input("Enter your password: ")
        self.db.add_password(name, pw)
        print("Password stored in db!") 

    def show(self):
        print("Showing passwords...")
        self.db.draw_passwords()

    def help(self):
        print("List of available commmands: 'new', 'save', 'show'")