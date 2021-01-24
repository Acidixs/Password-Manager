# Password manager by Acidix

import random
import string
import json
import os.path
import bcrypt
import commands
from database import Database

class PasswordManager:
    def __init__(self):
        self.db = Database()
        self.command = commands.Commands()

    def check_config(self):
        if os.path.isfile("config.json"):
            print("Config found!")
        else:
            included = {}
            included["included"] = []
            included["included"].append(
                        {"lower": True,
                        "upper": True,
                        "numbers": True,
                        "symbols": True})

            print("Config missing. Creating one...")
            with open("config.json", "w+") as f:
                json.dump(included, f, indent=4)

            print("File created.")
        

    def login(self):
        login = input("Enter master password: ")
        if Database().check_hash(login):
            print("Logged in.")
            self.run()
        else:
            print("Master password incorrect!")
            self.login()

    def get_cmd(self):
        commands = ("help, new, show, save")

        cmd = input("Enter command: ")
        if cmd not in commands:
            print("Command not recognised. Try using the command 'help' to get the list of available commands")

        elif "help" in cmd:
            self.command.help()
        elif "new" in cmd:
            self.command.new()
        elif "save" in cmd:
            self.command.save()
        elif "show" in cmd:
            self.command.show()


    def run(self):
        while True:
            self.get_cmd()


if __name__ == "__main__":
    app = PasswordManager()
    app.check_config()
    app.login()