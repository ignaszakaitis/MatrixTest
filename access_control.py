# access_control.py
import random

class AccessControl:
    def __init__(self):
        self.access_code = self.generate_access_code()
    
    def generate_access_code(self):
        return str(random.randint(1000, 9999))
    
    def verify_access(self, code):
        return code == self.access_code

if __name__ == "__main__":
    access = AccessControl()
    print(f"Doctor Access Code: {access.access_code}")
    user_code = input("Enter Access Code: ")
    if access.verify_access(user_code):
        print("Access Granted")
    else:
        print("Access Denied: Invalid Code")