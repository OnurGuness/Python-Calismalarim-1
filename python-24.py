#Python ile görsel programlama
# GUI - Kullanıcı Arayüzü Tasarımı

import tkinter as tk

pencere = tk.Tk()
#Tasarım ve çalışacak kodlar
pencere.title("İlk Arayüz Programı")
pencere.geometry("500x300+70+70")

etiket = tk.Label(text="Etiket - Label",font = "Verdana 18 bold")
etiket.pack()
# pack() komponentleri paketler
# grid() arayüzün parçalara bölünüyor
# place() x,y koordinatları ile yerleşim


pencere.mainloop()





