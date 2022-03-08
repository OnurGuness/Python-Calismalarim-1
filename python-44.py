from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("500x500")

c = Canvas(bg="white",width=400,height=400)

rectangle = c.create_rectangle(10,10,100,180,fill="red")

point = [200,200,340,280,350,350,390,325]
polygon =c.create_polygon(point,outline="blue",fill="yellow")

c.place(x=10,y=10)


pencere.mainloop()


