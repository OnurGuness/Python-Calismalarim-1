from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("500x500")

c = Canvas(bg="white",width=400,height=400)

oval = c.create_oval(10,50,100,100,fill="red")

c.place(x=10,y=10)

pencere.mainloop()