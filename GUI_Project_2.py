from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
from tkmacosx import Button

def login():
    if username_entry.get() and password_entry.get():
        try:
            # Check if Flask server is running
            server_response = requests.get('http://localhost:5050/')
            if server_response.status_code == 200:
                url = 'http://localhost:5050/login'
                resp = requests.post(url, data={'id': username_entry.get(), 'password': password_entry.get()})
                if resp.ok:
                    messagebox.showinfo("Success", "Login Succesfully")

                    protected_page = Toplevel()
                    url = 'http://localhost:5050/index'
                    msg = requests.get(url).text
                    text = Label(protected_page, text=msg, font=('Algerian', 14))
                    text.grid(row=0, column=0, padx=10, pady=5, sticky="w")

                elif resp.status_code == 401:
                    messagebox.showerror("Warning", "User Not Found. Please Double Check your Student ID")
                else:
                    messagebox.showerror("Warning", "Incorrect Password")
            else:
                messagebox.showerror("Warning", "Flask server is not running")
        except requests.ConnectionError:
            messagebox.showerror("Warning", "Connection to Flask server failed")
    else:
         messagebox.showerror("Warning", "Please enter username and password.")

window = tk.Tk()
window.title(' Student Login Page')
window.geometry('600x600')
window.minsize(600, 600)

session = requests.session()

bg_image = Image.open('/Users/LaurenTruelove/Desktop/ITM360/Project2/templates/studentlogin.png')
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(window, image=bg_photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

header_label = tk.Label(window, text="Welcome to Student Login!", bg="white", fg="black", font=('Arial', 20))
header_label.pack(pady=10)

username_label = tk.Label(window, text="Username:", bg="white", fg="black")
username_label.pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:", bg="white", fg="black")
password_label.pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack()

login_button = Button(window, text="LOGIN", bg='green', fg='white', font=("Arial", 12), borderless=1, command=login)
login_button.place(relx=0.5, rely=0.40, anchor='center')

open_eye_img = Image.open('/Users/LaurenTruelove/Desktop/ITM360/Project2/templates/show_eye.png') 
open_eye_img = open_eye_img.resize((20, 20))

closed_eye_img = Image.open('/Users/LaurenTruelove/Desktop/ITM360/Project2/templates/hide_eye.png')
closed_eye_img = closed_eye_img.resize((20, 20))

open_eye_photo = ImageTk.PhotoImage(open_eye_img)
closed_eye_photo = ImageTk.PhotoImage(closed_eye_img)

def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_hide_button.config(image=closed_eye_photo)
    else:
        password_entry.config(show='')
        show_hide_button.config(image=open_eye_photo)

show_hide_button = tk.Button(window, image=closed_eye_photo, command=toggle_password_visibility)
show_hide_button.place(relx=0.64, rely=0.26, anchor='w')

window.mainloop()


