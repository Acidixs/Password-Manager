import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()
        self.mydb = mysql.connector.connect(host=os.getenv("HOST"),
                                            user=os.getenv("USER"),
                                            password=os.getenv("PASSWORD"),
                                            database=os.getenv("DATABASE"))
    def connection(self):
        if self.mydb.is_connected():
            print("connection established!")
        else:
            print("no connection!")

    # retrieves hash from db, salt is added into hash and everything converted to binary
    def get_hash(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT master_password FROM user")
        myHash = cursor.fetchone()[0]
        mix = "$2b$14$" + myHash
        encoded = str.encode(mix)
        cursor.close()
        return encoded

    # converts password input to binary and compares it with hash from db
    def check_hash(self, pw):
        encoded = str.encode(pw)
        hashed = self.get_hash()
        return bcrypt.checkpw(encoded, hashed)