import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()
        self.connect()


    def connect(self):
        try:
            self.mydb = mysql.connector.connect(host=os.getenv("HOST"),
                                            user=os.getenv("USER"),
                                            password=os.getenv("PASSWORD"),
                                            database=os.getenv("DATABASE"))
            print("Connection to server was successful!")
        except:
            print("Connection to server was unsuccessful!")
            input("Press enter to try again: ")
            self.connect()

    # retrieves hash from db, salt is added into hash and everything converted to binary
    def get_hash(self):
        cursor = self.mydb.cursor(buffered=True)
        cursor.execute("SELECT master_password FROM master")
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

    def add_password(self, name, pw):
        cursor = self.mydb.cursor(buffered=True)
        conn = self.mydb
        sql = "INSERT INTO user (name, passwords) VALUES (%s, %s)"
        cursor.execute(sql, (name, pw))
        conn.commit()
        cursor.close()

    def draw_passwords(self):
        cursor = self.mydb.cursor(buffered=True, dictionary=True)
        cursor.execute("SELECT * FROM user")
        info = cursor.fetchall()
        if not info:
            print("No passwords found!")
            return   
        
        for i in info:
            for k, v in i.items():
                print(f"{k}: {v}")
            print("------------------------------------------------------------------------------")