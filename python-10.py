#Fonksiyonlar
#def fonksiyon_adi(parametre):
#   """Fonksiyon Açıklaması"""
#   islemler
#   return s

def ilk_fonksiyon():
    """Bu fonksiyon bizim ilk fonksiyonumuz"""
    print("fonksiyon tamamlandı")

ilk_fonksiyon()

print(ilk_fonksiyon.__doc__)

def merhaba(isim):
    print("merhaba ",isim)
merhaba("Yasin")

def topla(a,b):
    return a+b
def carp(a,b):
    return a*b
def kuvvet(a,b):
    return a**b
print(topla(5,8))
print(carp(78,98))
print(kuvvet(26,6))


