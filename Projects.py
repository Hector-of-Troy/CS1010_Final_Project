

import tkinter

ash = tkinter.Tk()
ash.geometry('800x800')
ash.title("MLB Stats")
ash.configure(bg="light blue")

def button_1():
        bob = tkinter.Tk()
        bob.geometry('500x500')
        bob.title("MLB Teams Available")
        bob.configure(bg="blue")
button_1 = tkinter.Button(ash, text="Teams", command=button_1)
button_1.pack()

def two_button():
        mercy = tkinter.Tk()
        mercy = tkinter.Tk()
        mercy.geometry('500x500')
        mercy.title("MLB Players Available")
        mercy.configure(bg="red")
two_button = tkinter.Button(ash, text="Players", command=two_button)
two_button.pack()

ash.mainloop()
