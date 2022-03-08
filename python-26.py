# pack, grid, place

import tkinter as tk

pencere = tk.Tk()
pencere.geometry("300x300")
etiket1 = tk.Label(text = "etiket1", bg= "blue",fg="yellow",font="Verdana 22")
etiket1.pack(side="left") # top,left,right,bottom

etiket2 = tk.Label(text = "etiket2", bg= "red",fg="yellow",font="Verdana 22")
etiket2.pack(fill="x") # x,y

etiket3 = tk.Label(text = "etiket3", bg= "green",fg="yellow",font="Verdana 22")
etiket3.pack(fill="x")

etiket4 = tk.Label(text = "etiket4", bg= "black",fg="yellow",font="Verdana 22")
etiket4.pack(expand_="yes") # yes,no
pencere.mainloop()

#grid
pencere2 = tk.Tk()
p2e1 = tk.Label(text = "etiket1", bg= "blue",fg="yellow",font="Verdana 22")
p2e1.grid(row=0,column=0)

p2e2 = tk.Label(text = "etiket2", bg= "red",fg="yellow",font="Verdana 22")
p2e2.grid(row=1,column=1)

pencere2.mainloop()

#place
pencere3 = tk.Tk()
pencere3.geometry("300x300")
p3e1 = tk.Label(text = "etiket1", bg= "blue",fg="yellow",font="Verdana 22")
p3e1.place(x=44,y=20)

p3e2 = tk.Label(text = "etiket2", bg= "red",fg="yellow",font="Verdana 22")
p3e2.place(x=150,y=20)

pencere3.mainloop()