import tkinter as tk
from tkinter import *

def sec():
    print("Seçim 1 ",c1.get())
    print("Seçim 2 ",c2.get())

def rsec():
    print(r.get())

pencere = tk.Tk()

pencere.geometry("300x300")

c1 = IntVar()
c2 = IntVar()
cb1 = Checkbutton(text="Seçim 1",variable=c1,onvalue=1,offvalue=0,command=sec)
cb2 = Checkbutton(text="Seçim 2",variable=c2,onvalue=1,offvalue=0,command=sec)
cb1.place(x=20,y=20)
cb2.place(x=100,y=20)


r = IntVar()
rb1 = Radiobutton(text="Radio 1",variable=r,value=1,command=rsec)
rb2 = Radiobutton(text="Radio 2",variable=r,value=2,command=rsec)
rb1.place(x=20,y=50)
rb2.place(x=100,y=50)
pencere.mainloop()









