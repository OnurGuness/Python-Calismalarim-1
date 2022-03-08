import tkinter as tk
from tkinter.ttk import Combobox 

variable_1 = tk.StringVar()
variable_1.set("İl Seçin")
values_1 = ["Ankara","İstanbul","Afyonkarahisar"]
combobox_1 = Combobox (

    textvariable=variable_1,
    values=values_1

)
combobox_1.pack()

variable_2 = tk.StringVar()
variable_2.set("İlçe Seçin")
values_2 = {
    "Ankara": ["Mamak","Çankaya"],
    "İstanbul":["Kadıköy","Üsküdar"],
    "Afyonkarahisar":["Merkez","Sinanpaşa","Emirdağ"]
}
combobox_2 = Combobox(

    textvariable=variable_2,
    values=values_2["Ankara"]

)
combobox_2.pack()

def change():
    if combobox_1.get() =="Ankara":
        combobox_2.configure(values=values_2["Ankara"])
    elif combobox_1.get() == "İstanbul":
        combobox_2.configure(values=values_2["istanbul"])
    else:
        combobox_1.get() == "Afyonkarahisar"
        combobox_2.configure(values=values_2["Afyonkarahisar"])

combobox_1.bind("<<ComboboxSelected>>", lambda event: change())

