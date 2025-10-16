#Imports
import re
import tkinter as tk
from tkinter import messagebox
from string import punctuation
import sqlite3
from hashing import hash_password, verify_password


def validate_password(password):

    errors = []

    if len(password) < 8:
        errors.append("at least 8 characters long")

    if not re.search(r'[A-Z]', password):
        errors.append("at least one uppercase letter")

    if not re.search(r'[a-z]', password):
        errors.append("at least one lowercase letter")

    if not re.search(r'[0-9]', password):
        errors.append("at least one number")

    has_special = any(char in punctuation for char in password)
    if not has_special:
        errors.append("at least one special character")

    if errors:
        error_message = "Password must contain:\n- " + "\n- ".join(errors)
        return False, error_message


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    #Connect to database
    conn = sqlite3.connect('satellite_system.db')
    c = conn.cursor()

    #Check if user exists
    c.execute("SELECT password_hash FROM Users WHERE username = ?", (username,))
    result = c.fetchone()

    conn.close()

    if result:
        stored_hash = result[0]
        if verify_password(password, stored_hash):
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid password.")
    else:
        messagebox.showerror("Error", "User not found.")


def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    #Validate password strength
    is_valid, error_msg = validate_password(password)
    if not is_valid:
        messagebox.showerror("Invalid Password", error_msg)
        return

    #Hash the password
    hashed_password = hash_password(password)

    #Connect to database
    conn = sqlite3.connect('satellite_system.db')
    c = conn.cursor()

    try:
        #Insert new user
        c.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", 
                  (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    finally:
        conn.close()


#https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-16.php


#Create the main window
window = tk.Tk()
window.title("Satellite System - Login")
window.geometry("1920x1080")

#Create and place the username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(window, width=30)
username_entry.pack(pady=5)

#Create and place the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack(pady=5)

#Create button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

#Create and place the login button
login_button = tk.Button(button_frame, text="Login", command=validate_login, width=12, bg="#4CAF50", fg="white")
login_button.pack(side=tk.LEFT, padx=5)

#Create and place the register button
register_button = tk.Button(button_frame, text="Register", command=register_user, width=12, bg="#2196F3", fg="white")
register_button.pack(side=tk.LEFT, padx=5)

#Start the Tkinter event loop
window.mainloop()

