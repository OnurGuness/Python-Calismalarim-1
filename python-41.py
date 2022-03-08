from tkinter import *
import tkinter as tk

pencere = tk.Tk()

pencere.geometry("500x500")

c = Canvas(bg="white",width=300,height=300)

line = c.create_line(0,0,150,150,fill="red",width=3)
line2 = c.create_line(50,75,225,75,fill="blue",width=5)
line3 = c.create_line(50,50,50,275,fill="green",width=2)
c.place(x=10,y=10)

pencere.mainloop()




