import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os
from encryption import Encrypt, Decrypt

class Database:
    def __init__(self):
        load_dotenv()
        self.connect()
        self.Encrypt = Encrypt()
        self.Decrypt = Decrypt()


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

    def hash_pw(self, pw):
        hashed = bcrypt.hashpw(bytes(pw, encoding="utf-8",), salt=bcrypt.gensalt(14))
        return hashed[7:] # cut out salt info

    def add_password(self, name, pw):
        encrypted = self.Encrypt.encrypt_password(pw=pw)

        cursor = self.mydb.cursor(buffered=True)
        conn = self.mydb
        sql = "INSERT INTO user (name, passwords) VALUES (%s, %s)"
        cursor.execute(sql, (name, encrypted))
        conn.commit()
        cursor.close()

    def remove_password(self, ids):
        cursor = self.mydb.cursor(buffered=True)
        conn = self.mydb
        sql = "DELETE FROM user WHERE id = %s"
        ids = (ids,) # convert id to tuple
        cursor.execute(sql, ids)
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
            print("-"*20)
            i["passwords"] = self.Decrypt.decrypt_password(i["passwords"])
            for k, v in i.items():
                print(f"{k}: {v}")

    def update_master_password(self, pw):
        cursor = self.mydb.cursor(buffered=True, dictionary=True)
        pw = (self.hash_pw(pw), )
        sql = "UPDATE master SET master_password = %s"
        cursor.execute(sql, pw)
        self.mydb.commit()
        print("Master password updated!")


    def search_password(self):
        cursor = self.mydb.cursor(buffered=True, dictionary=True)
        cursor.execute("SELECT * FROM user")
        info = cursor.fetchall()
        
        search = input("Enter name of saved password: ")
        for i in info:
            for k, v in i.items():
                if i["name"] == search:
                    name = i["name"]
                    pw = self.Decrypt.decrypt_password(i["passwords"])
                    print(f"Password for {name} is: {pw}")
                    return
                else:
                    print("No password found! Try the command 'show', to get all your stored passwords!")
                    return