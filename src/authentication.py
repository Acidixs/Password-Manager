import pyotp
import os


class Authentication:
    def __init__(self):
        pass
    
    def get_key(self):
        if os.path.isfile("2fa.txt"):
            with open("2fa.txt", "r") as f:
                key = f.read()
            return key
        else:
            print("Key not found!")
            self.create_key()

    def create_key(self):
        """Enter the key generated into your 2fa authenticator app,
        to start generating keys"""

        key = pyotp.random_base32()
        with open("2fa.txt", "w+") as f:
            f.write(key)
        print("Key created!")

            
    def verify(self, code):
        key = self.get_key()
        otp = pyotp.TOTP(key).now()
        return code == otp

