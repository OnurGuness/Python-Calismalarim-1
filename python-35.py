import tkinter as tk
from tkinter import *

def fonksiyon():
    print("Menu secildi")

pencere = tk.Tk()

menucubugu = Menu(pencere)

dosya = Menu(menucubugu,tearoff=0)
dosya.add_command(label="Yeni",command=fonksiyon)
dosya.add_command(label="Aç",command=fonksiyon)
dosya.add_separator()
dosya.add_command(label="Çıkış",command=fonksiyon)
menucubugu.add_cascade(label="Dosya",menu=dosya)

duzen = Menu(menucubugu,tearoff=0)
duzen.add_command(label="Kes",command=fonksiyon)
duzen.add_command(label="Kopyala",command=fonksiyon)
duzen.add_separator()
duzen.add_command(label="Yapıştır",command=fonksiyon)

menucubugu.add_cascade(label="Duzen",menu=duzen)

pencere.config(menu=menucubugu)
pencere.mainloop()








