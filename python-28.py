import tkinter as tk
from tkinter.ttk import *

def secimAl():
    print(combo.get())

pencere = tk.Tk()

combo = Combobox()
combo['values'] = ("İstanbul","Ankara","İzmir","Bursa","Adana","Afyon")
combo.current(0)
combo.place(x=20,y=20)

button = tk.Button(text='İşlem',command=secimAl)
button.place(x=20,y=60)


pencere.mainloop()










