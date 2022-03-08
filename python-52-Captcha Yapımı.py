from tkinter import *
import random as r


def yap():
    c.delete("all")
    h = []
    for i in range(0,5):
        h.append(chr(r.randint(65,90)))
    renk = ["black","purple","blue","green","gray"]
    fnt = ["Verdana","Ariel","Papyrus","Calibri"]

    b1 = c.create_text(40+r.randint(0,10), 40+r.randint(0,10), text=h[0],font=fnt[r.randint(0,3)]+" 32 bold",fill=renk[r.randint(0,4)])
    b2 = c.create_text(80+r.randint(0,10), 40+r.randint(0,10), text=h[1], font=fnt[r.randint(0,3)]+" 32 bold",fill=renk[r.randint(0,4)])
    b3 = c.create_text(120+r.randint(0,10), 40+r.randint(0,10), text=h[2], font=fnt[r.randint(0,3)]+" 32 bold",fill=renk[r.randint(0,4)])
    b4 = c.create_text(160+r.randint(0,10), 40+r.randint(0,10), text=h[3], font=fnt[r.randint(0,3)]+" 32 bold",fill=renk[r.randint(0,4)])
    b5 = c.create_text(200+r.randint(0,10), 40+r.randint(0,10), text=h[4], font=fnt[r.randint(0,3)]+" 32 bold",fill=renk[r.randint(0,4)])

    for i in range(0,10):
        f = c.create_line(r.randint(5,295),r.randint(5,195),r.randint(5,295),r.randint(5,195),fill=renk[r.randint(0,4)],width=r.randint(1,3))

pencere = Tk()
pencere.geometry("300x200")

c = Canvas(width=280,height=100,bg="white")
b = Button(text="OLUŞTUR",font="Verdana 14 bold",command=yap)

b.place(x=100,y=120)
c.place(x=10,y=10)

pencere.mainloop()


















