#Create a login form in python with Tkinter (no date) w3resource. Available at: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-16.php (Accessed: 15 October 2025). 

import tkinter as tk
from tkinter import messagebox
import sqlite3
from hashing import hash_password, verify_password

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to database
    conn = sqlite3.connect('satellite_system.db')
    c = conn.cursor()

    # Check if user exists
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

    # Hash the password
    hashed_password = hash_password(password)

    # Connect to database
    conn = sqlite3.connect('satellite_system.db')
    c = conn.cursor()

    try:
        # Insert new user
        c.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", 
                  (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    finally:
        conn.close()

# Create the main window
parent = tk.Tk()
parent.title("Login Form")
parent.geometry("300x200")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(parent)
username_entry.pack(pady=5)

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack(pady=5)

# Create button frame
button_frame = tk.Frame(parent)
button_frame.pack(pady=10)

# Create and place the login button
login_button = tk.Button(button_frame, text="Login", command=validate_login, width=10)
login_button.pack(side=tk.LEFT, padx=5)

# Create and place the register button
register_button = tk.Button(button_frame, text="Register", command=register_user, width=10)
register_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
parent.mainloop()