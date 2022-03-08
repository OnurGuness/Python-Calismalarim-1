from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("500x500")

c = Canvas(bg="white",width=400,height=400)

dosya = PhotoImage(file = "bisiklet.gif")

imaj = c.create_image(150,150,anchor=SW, image=dosya)

c.place(x=10,y=10)


pencere.mainloop()