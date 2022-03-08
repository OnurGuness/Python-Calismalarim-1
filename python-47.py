from tkinter import *
import tkinter as tk

#bitmap = "errors","gray75","gray50","gray25","gray12",
# "hourglass","info","questhead","question","warning"

pencere = tk.Tk()
pencere.geometry("300x300")

b = Button(bitmap="question")
b.place(x=10,y=10)

pencere.mainloop()






