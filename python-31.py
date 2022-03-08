import tkinter as tk
from tkinter import *

from tkinter import messagebox

def goster():
    messagebox.showinfo("Mesaj metni burada gösterilir!", "Hoşgeldiniz")
    mesaj.set("Bu da pencere mesajı")
    m.place(x=75,y=100)

pencere = tk.Tk()

mesaj = StringVar()
m = Message(textvariable=mesaj,relief=RAISED)

b = Button(text="Mesaj Göster",command= goster)
b.place(x=20,y=20)


pencere.mainloop()












