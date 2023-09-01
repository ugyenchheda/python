import num2words as n2w
import os
from tkinter import *

def num_to_words():
    given_num = float(num.get())
    num_in_word = n2w.num2words(given_num)
    display.config(text=str(num_in_word).capitalize())

root = Tk()
root.title("Spell Number")
root.geometry("300x350")

num = StringVar()

# Adding title
title = Label(root, text="Number to Words converter", fg="Orange", font=("vardena", 15, 'bold')).place(x=15, y=10)

# Options
formats_label = Label(root, text="Formats supported :  ", fg="green", font=("vardena", 10, 'bold')).place(x=15, y=70)
pos_format_label = Label(root, text="1. Positives :  ", fg="green", font=("vardena", 10, 'bold')).place(x=50, y=90)
neg_format_label = Label(root, text="2. Negatives ", fg="green", font=("vardena", 10, 'bold')).place(x=50, y=110)
float_format_label = Label(root, text="3. Zeros  ", fg="green", font=("vardena", 10, 'bold')).place(x=50, y=130)
zero_format_label = Label(root, text="4. Floating points/decimals/fractions  ", fg="green", font=("vardena", 10, 'bold')).place(x=50, y=150)

btn = Button(master=root, text="calculate",fg="white",width=20, font=("vardena", 10, 'bold') ,command=num_to_words, bg="green").place(x=100,y=230)

display = Label(root, text="",fg="black", font=("vardena", 10, 'bold'))
display.place(x=10, y=300)

script_directory = os.path.dirname(os.path.abspath(__file__))

#give image location here
image_path = os.path.join(script_directory, 'digittospell', 'number.png')
photo = PhotoImage(file=image_path)
root.iconphoto(False, photo)

root.mainloop()
