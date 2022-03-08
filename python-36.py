from tkinter import *
from tkinter import messagebox
import tkinter as tk

pencere = tk.Tk()

mb = Menubutton(text="Salatalar", relief=RAISED)
mb.place(x=20,y=20)

mb.menu = Menu(mb,tearoff=0)
mb['menu'] = mb.menu

mevsim_salata = IntVar()
coban_salata = IntVar()

mb.menu.add_checkbutton(label="Çoban Salata",variable=coban_salata)
mb.menu.add_checkbutton(label="Mevsim Salata",variable=mevsim_salata)


pencere.mainloop()








