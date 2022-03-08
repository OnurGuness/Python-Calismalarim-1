import tkinter as tk
from tkinter import *

#rgb - red green blue

def renk():
    r = sred.get()
    g = sgreen.get()
    b = sblue.get()
    #hex = 16lık koda dönüştürme
    rh = hex(int(r))
    gh = hex(int(g))
    bh = hex(int(b))
    color = "#" + rh.replace("0x","") + gh.replace("0x","") + bh.replace("0x","")
    print(color)
    pencere.configure(bg=color) #6b3


pencere = tk.Tk()

pencere.geometry("300x300")

lred = Label(text="Kırmızı")
lred.place(x=20,y=20)
sred = Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sred.place(x=75,y=20)

lgreen = Label(text="Yeşil")
lgreen.place(x=20,y=50)
sgreen = Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sgreen.place(x=75,y=50)

lblue = Label(text="Mavi")
lblue.place(x=20,y=80)
sblue = Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sblue.place(x=75,y=80)


pencere.mainloop()










