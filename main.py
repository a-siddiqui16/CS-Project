#Imports

import tkinter as tk


#Login Page

window = tk.Tk()

#Title
window.title("Login form")

#Default Resolution
window.geometry("1920x1080")

#Background Colour
window.configure(bg="#FFFFFF")

#Creating Widgets
login_label = tk.Label(window, text="Login")
username_label = tk.Label(window, text="Username")
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")
password_label - tk.Label(window, text="Password")
login_button = tk.Button(window, text="Login")

#Placing widgets on screen
login_label








window.mainloop()