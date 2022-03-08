import tkinter as tk
from tkinter import *

def pencere_oluştur():
    t2 = Toplevel(bg="BLUE")

pencere = tk.Tk()

t1 = Toplevel(bg="RED")

b = Button(text="pencere oluştur", command=pencere_oluştur)
b.place(x=10,y=10)
pencere.mainloop()


