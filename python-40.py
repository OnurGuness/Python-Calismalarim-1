import tkinter as tk
from tkinter import *

pencere = tk.Tk()

pw1 = PanedWindow(bg="RED",width=200,height=150)
pw1.place(x=0,y=0)


lbl = Label(pw1,text="Kırmızı Pane")
lbl.place(x=10,y=10)

pw2 = PanedWindow(bg="BLUE",width=50,height=50)
pw2.place(x=50,y=50)


pencere.mainloop()