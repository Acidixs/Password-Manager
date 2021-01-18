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

    def get_hash(self):
        cursor = self.mydb.cursor()

        query = "SELECT master_password FROM user"
        cursor.execute(query)
        myHash = cursor.fetchone()[0]
        cush = "$2b$14$" + myHash
        bcush = str.encode(cush)
        dcush = bcush.rstrip(b"\x00")
        cursor.close()
        return(dcush)

    def check_hash(self, pw):
        encoded = str.encode(pw)
        b = encoded.rstrip(b"\x00")
        hashed = self.get_hash()
        return bcrypt.checkpw(b, hashed)
 