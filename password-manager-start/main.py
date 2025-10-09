import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

standard_email = "banteas@hotmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]


    password_list = (password_letters + password_symbols + password_numbers)

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()
    website_len = len(website)
    password_len = len(password)
    new_file = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website_len == 0 or password_len == 0:
        messagebox.showerror("Error", "Please enter the website and the password.")

    else:
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data.update(new_file)
        with open('passwords.json', 'w') as file:
            json.dump(data, file, indent=4)
            messagebox.showinfo(website, "Password and Email have been saved.")

        website_entry.delete(0, END)
        username_entry.delete(0, END)
        username_entry.insert(0, standard_email)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showerror("Error", "No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(website, f" Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No details for {website} exists")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(window, width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(window, text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(window,width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(window,width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, standard_email)

password_entry = Entry(window,width=24)
password_entry.grid(row=3, column=1, sticky="EW")


# Buttons
search_button = Button(window, text="Search",command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

password_button = Button(window, text="Generate Password",command=password_generator)
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(window, text="Add",width=36,command=save)
add_button.grid(row=4, column=1,columnspan=2, sticky="EW")

window.mainloop()
