from tkinter import *
import tkinter as tk

pencere = tk.Tk()

pencere.geometry("500x500")

c = Canvas(bg="white",width=300,height=300)

c.place(x=10,y=10)

coord=10,10,200,200
yay = c.create_arc(coord,start=0,extent=180,fill="blue")

pencere.mainloop()