#Imports

import re
from string import punctuation #Imports all of the special characters
from hashing import hashed


#Text Based UI -> Moving to Tkinter

print("Option 1: Login")


username = input("Enter username")
password = input("Enter password")


def validate(user_password):

    is_valid = True

    #Checks minimum length
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        is_valid = False

    #Checks for uppercase letter
    if not re.search(r'[A-Z]', password):
        print("Password must contain at least once uppercase letter")

    #Checks for lowercase letter
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter")

    #Checks for digit
    if not re.search(r'[0-9]', password):
        print("Password must contain at least one number")

    #Checks for special character

    has_special = False
    for char in password:
        if char in punctuation:
            has_special = True
            break

    if not has_special:
        print("Password must contain at least one special character")
        is_valid = False

    #Return the result (whether the password is acceptable or not)
    if is_valid:
        return True
    else:
        return False
    
while validate(password) == False:
    print("Password is invalid")
    password = input("Enter password: ")


    
