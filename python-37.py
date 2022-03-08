import tkinter as tk
from tkinter import *

def secim():
    print(lb.curselection())

pencere = tk.Tk()

lb = Listbox(selectmode=MULTIPLE)
lb.insert(0,"Php")
lb.insert(1,"C++")
lb.insert(2,"Java")
lb.insert(3,"Python")

lb.place(x=10,y=10)

b = Button(text="Seçilenler",command=secim)
b.place(x=135,y=50)

lb.place(x=10,y=10)


pencere.mainloop()








