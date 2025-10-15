#Create a login form in python with Tkinter (no date) w3resource. Available at: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-16.php (Accessed: 15 October 2025). 

import tkinter as tk
from tkinter import messagebox
from hashing import hash_password, verify_password

def validate_login():
  username = username_entry.get()
  password = password_entry.get()
  
  hashed_password = hash_password(password) #Hash the password
  if verify_password(password, hashed_password):
    messagebox.showinfo("Login Successful")
  else:
    messagebox.showerror("Login Failed", "Invalid password.")

#Create the main window
# Create the main window
parent = tk.Tk()
parent.title("Login Form")

#Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

#Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

#Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

#Start the Tkinter event loop
parent.mainloop()

  