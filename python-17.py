# Inheritance - Miras alma

class kus:
    tur_ad=""
    kus_ad=""

    def isimYaz(self):
        print("Tür adı: ",self.tur_ad)
        print("Kuş ismi: ",self.kus_ad)
class yirtici(kus):   #subclass - alt sınıf
    kanat_uzunlugu ="0"
    agirlik = "0"

class kartal(yirtici):
    alt_tur = ""

anadolu_kartali=kartal()

anadolu_kartali.tur_ad="anatolian eagle"
anadolu_kartali.kus_ad="siyah kartal"
anadolu_kartali.kanat_uzunlugu = "1.5 m"
anadolu_kartali.agirlik = "6 kg"
anadolu_kartali.alt_tur = "middle east eagle"

anadolu_kartali.isimYaz()
