from textwrap import indent
import tkinter as tk
from tkinter import messagebox
from generatepassword import PasswordGenerator
import pyperclip
import json


FONT = 'Ubuntu Mono'
DEFAULT_EMAIL = ""
STORED_PASSWORDS = "passwords.txt"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_generator = PasswordGenerator()

def generate_password():
    password_generator.generate()
    new_passwd = password_generator.generated_password
    entry_password.insert(0,new_passwd)
    pyperclip.copy(new_passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def reset_fields():
    entry_website.delete(0,tk.END)
    entry_password.delete(0,tk.END)
    entry_username.delete(0,tk.END)
    entry_username.insert(0, DEFAULT_EMAIL)

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
        
    is_complete = len(website) and len(username) and len(password) != 0

    if is_complete:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            reset_fields()
    else:
        messagebox.showerror(title="Oops!", message=f"You have empty fields")

# ---------------------------- UI SETUP ------------------------------- #



#window setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#lock img
lock_img = tk.Canvas(width=200,height=200, highlightthickness=0)
lock_img_path2img = tk.PhotoImage(file="logo.png")
lock_img.create_image(100,100, image=lock_img_path2img)
lock_img.grid(row=0,column=1)

#labels & buttons

label_website = tk.Label(text="Website:", font=(FONT,14))
label_username = tk.Label(text="Email/Username:", font=(FONT,14))
label_password = tk.Label(text="Password:", font=(FONT,14))

entry_website = tk.Entry(width=38)
entry_website.focus()
entry_username = tk.Entry(width=38)
entry_username.insert(0, DEFAULT_EMAIL)
entry_password = tk.Entry(width=21)

button_gen_psswd = tk.Button(text="Generate Password", command=generate_password)
button_add = tk.Button(text="Add", width=36, command = save_password)

#positions
lock_img.grid(row=0,column=1)

label_website.grid(row=1,column=0)
entry_website.grid(row=1,column=1,columnspan=2)

label_username.grid(row=2,column=0)
entry_username.grid(row=2,column=1,columnspan=2)

label_password.grid(row=3,column=0)
entry_password.grid(row=3,column=1)
button_gen_psswd.grid(row=3,column=2)

button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()