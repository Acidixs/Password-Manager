from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self):
        pass

    def new_key(self):
        key = Fernet.generate_key()
        with open("key.txt", "wb") as f:
            f.write(key)

    def load_key(self):
        with open("key.txt", "rb") as f:
            key = f.read()
        return key

    def encrypt_password(self, pw):
        pw = bytes(pw, "utf-8")
        key = self.load_key()
        f = Fernet(key)
        encrypted = f.encrypt(pw)
        return encrypted


class Decrypt(Encrypt):

    def decrypt_password(self, pw):
        token = bytes(pw, encoding="utf-8")
        key = self.load_key()
        f = Fernet(key)
        decrypted = f.decrypt(token)
        return decrypted.decode("utf-8")



