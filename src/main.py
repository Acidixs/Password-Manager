# Password manager by Acidix

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
            self.create_config()


    def create_config(self):
        config = [{"included": {"lower": True, "upper": True, "numbers": True, "symbols": True},
          "export": {"file": True, "database": True}}]

        print("Config missing. Creating one...")

        with open("config.json", "w+") as f:
            json.dump(config, f, indent=4)

        print("Config created.")


    def login(self):
        login = input("Enter master password: ")
        if Database().check_hash(login):
            print("Logged in.")
            self.run()
        else:
            print("Master password incorrect!")
            self.login()

    def get_cmd(self):
        commands = {"help": self.command.help,
                    "new": self.command.new,
                    "show": self.command.show,
                    "save": self.command.save,
                    "search": self.command.search,
                    "delete": self.command.delete}

        cmd = input("Enter command: ")
        if cmd not in commands.keys():
            print("Command not recognised. Try using the command 'help' to get the list of available commands")
        else:
            commands[cmd]()



    def run(self):
        while True:
            self.get_cmd()


if __name__ == "__main__":
    app = PasswordManager()
    app.check_config()
    app.login()
