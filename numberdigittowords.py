import num2words as n2w
import os
from tkinter import *

def num_to_words():
    given_num = float(num.get())
    num_in_word = n2w.num2words(given_num)
    display.config(text=str(num_in_word).capitalize())

root = Tk()
root.title("Spell Number")
root.geometry("330x330")

num = StringVar()

# Adding title
title = Label(root, text="Number to Words converter", fg="green", font=("vardena", 15, 'bold')).place(x=30, y=25)

# Options
formats_label = Label(root, text="Formats supported :  ", fg="black", font=("vardena", 13)).place(x=30, y=70)
pos_format_label = Label(root, text="1. Positives :  ", fg="black", font=("vardena", 10)).place(x=50, y=90)
neg_format_label = Label(root, text="2. Negatives ", fg="black", font=("vardena", 10)).place(x=50, y=110)
float_format_label = Label(root, text="3. Zeros  ", fg="black", font=("vardena", 10)).place(x=50, y=130)
zero_format_label = Label(root, text="4. Floating points/decimals/fractions  ", fg="black", font=("vardena", 10)).place(x=50, y=150)

num_entry_label = Label(root, text="Enter Digit to Convert:", fg="Black", font=("vardena", 10)).place(x=100, y=200) 
num_entry = Entry(root,textvariable=num,width=28).place(x=80, y=230)

btn = Button(master=root, text="Convert",fg="white",width=20, font=("vardena", 10, 'bold') ,command=num_to_words, bg="green").place(x=80,y=260)

display = Label(root, text="",fg="black", font=("vardena", 10, 'bold'))
display.place(x=10, y=300)

script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, 'digittospell', 'pandacoding.png')
photo = PhotoImage(file=image_path)
root.iconphoto(False, photo)

root.mainloop()
