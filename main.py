from tkinter import *
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    length = random.randint(8, 16)
    for i in range(length):
        char_index = random.randint(40, 122)
        password += chr(char_index)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    file = open("info.txt", mode="a")
    website_value = website_entry.get()
    email_username_value = email_username_entry.get()
    password_value = password_entry.get()
    file.write(f"Website: {website_value} | Email/username: {email_username_value} | Password: {password_value} \n")
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)
    file.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.geometry("600x400")
window.config(padx=40)


img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=190)
canvas.create_image(100, 95, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Times", 15))
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font=("Times", 15))
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Times", 15))
password_label.grid(column=0, row=3)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, sticky="w")

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, sticky="w", pady=20)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(width=15, text="Generate password", command=generate_password)
generate_button.grid(column=1, row=3, sticky="e")

add_button = Button(width=35, text="Add", command=add_to_file)
add_button.grid(column=1, row=4, pady=20)






window.mainloop()
