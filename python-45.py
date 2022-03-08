from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("500x500")

c = Canvas(bg="white",width=400,height=400)

text = c.create_text(150,100,text="Bu bir canvas yazısıdır",font="Ariel 16 bold")


c.place(x=10,y=10)


pencere.mainloop()








