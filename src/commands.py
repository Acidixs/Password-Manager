from database import Database
from generator import PasswordGenerator
import json

class Commands:
    def __init__(self):
        self.db = Database()
        self.pwg = PasswordGenerator()

    def save_pass_to_file(self, name, pw):
        with open("passwords.txt", "a+") as f:
            f.write((f"Name: {name} Password: {pw}" + "\n"))

    def check_export_config(self, name, pw):
        with open("config.json", "r") as f:
            data = json.load(f)

            if data[0]["export"]["database"]:
                self.db.add_password(name, pw)
                print("Password saved to database!")

            if data[0]["export"]["file"]:
                self.save_pass_to_file(name, pw)


    def new(self):
        name = input("Enter a name for the password: ")
        length = self.pwg.get_pw_length()
        pw = self.pwg.new_password(length)
        self.check_export_config(name, pw)
        print("Your new password is: {}".format(pw))

    def delete(self):
        ids = input("Enter id of password: ")
        self.db.remove_password(ids)

    def save(self):
        name = input("Enter a name for your password: ")
        pw = input("Enter your password: ")
        self.check_export_config(name, pw)
        print("Password stored in db!") 

    def show(self):
        print("Showing passwords...")
        self.db.draw_passwords()

    def help(self):
        print("List of available commmands: 'new', 'save', 'show'")
    
    def search(self):
        self.db.search_password()

    def update_master_password(self):
        pw = input("Enter master password: ")
        self.db.update_master_password(pw)