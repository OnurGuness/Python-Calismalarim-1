from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("300x300")

imaj = PhotoImage(file="game.gif")

kimaj = imaj.subsample(7,7)

bimaj = PhotoImage(file="pc.gif")
bimaj = bimaj.subsample(10,10)
b = Button(text="Oyun",image=kimaj,compound=LEFT)
b.place(x=10,y=10)
b2= Button(text="Oyun",image=bimaj, compound=RIGHT)
b2.place(x=75,y=10)



pencere.mainloop()