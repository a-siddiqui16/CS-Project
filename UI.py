#Imports
import re
import tkinter as tk
from tkinter import messagebox
from string import punctuation  #Imports all of the special characters
from hashing import hash_password, verify_password





def validate(user_password):
    is_valid = True

    #Checks minimum length
    if len(user_password) < 8:
        print("Password must be at least 8 characters long")
        is_valid = False

    #Checks for uppercase letter
    if not re.search(r'[A-Z]', user_password):
        print("Password must contain at least one uppercase letter")
        is_valid = False

    #Checks for lowercase letter
    if not re.search(r'[a-z]', user_password):
        print("Password must contain at least one lowercase letter")
        is_valid = False

    #Checks for digit
    if not re.search(r'[0-9]', user_password):
        print("Password must contain at least one number")
        is_valid = False

    #Checks for special character
    has_special = False
    for char in user_password:
        if char in punctuation:
            has_special = True
            break

    if not has_special:
        print("Password must contain at least one special character")
        is_valid = False

    #Return the result (whether the password is acceptable or not)
    return is_valid


def validate_login(password, stored_hash):
    """
    Validates user login by checking if the password matches the stored hash
    
    Args:
        password: The password entered by the user
        stored_hash: The hashed password stored in the database
    
    Returns:
        True if password matches, False otherwise
    """
    return verify_password(password, stored_hash)

    
while not validate(password):
    print("Password is invalid")
    password = input("Enter password: ")


#Hash the validated password
hashed_password = hash_password(password)
print(f"Successfully logged in as {username}")
print(f"Hashed password: {hashed_password}")
