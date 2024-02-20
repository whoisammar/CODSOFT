import string
import random
import tkinter as tk
from tkinter import *

def Generator():
    # Function to generate a password based on user input
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    number = string.digits
    special = string.punctuation

    all_chars = small + capital + number + special
    passlen = int(len_entry.get())

    # Generating a password by sampling characters randomly
    password = ''.join(random.sample(all_chars, passlen))
    gen_entry.delete(0, 'end')
    gen_entry.insert(0, password)

root = Tk()
root.configure(bg="white")
root.title("Password Generator")
root.geometry('925x500+300+200')
root.resizable('False', 'False')

# Loading an image for the background
img = PhotoImage(file='image.png')
Label(root, image=img, border=0, bg="white").place(x=50, y=100)

frame = Frame(root, width=350, height=390, bg='white')
frame.place(x=500, y=60)

# Heading label
heading = Label(frame, text='Password Generator', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=25, y=10)

# Entry for user's name
def on_entry_focus_in(e):
    user.delete(0, 'end')

def on_entry_focus_out(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Name')

user = Entry(frame, width=20, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 10))
user.place(x=45, y=96)
user.insert(0, 'Name')
user.bind('<FocusIn>', on_entry_focus_in)
user.bind('<FocusOut>', on_entry_focus_out)
Frame(frame, width=265, height=2, bg='black').place(x=45, y=120)

# Entry for password length
def on_len_focus_in(e):
    len_entry.delete(0, 'end')

def on_len_focus_out(e):
    name = len_entry.get()
    if name == '':
        len_entry.insert(0, 'Password Length')

len_entry = Entry(frame, width=20, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 10))
len_entry.place(x=45, y=160)
len_entry.insert(0, 'Password Length')
len_entry.bind('<FocusIn>', on_len_focus_in)
len_entry.bind('<FocusOut>', on_len_focus_out)
Frame(frame, width=265, height=2, bg='black').place(x=45, y=185)

# Entry to display the generated password
gen_entry = Entry(frame, width=20, fg='black', border=0, bg='white', font=('MS UI Gothic', 10, 'bold'))
gen_entry.place(x=45, y=220)
Frame(frame, width=265, height=2, bg='black').place(x=45, y=245)

# Button to trigger the password generation
Button(frame, width=25, pady=7, text='Generate Password', fg='white', bg='#57a1f8',font=('Microsoft YaHei UI Light', 10, 'bold'), command=Generator).place(x=60, y=280)

root.mainloop()