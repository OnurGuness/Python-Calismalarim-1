#Encapsulation - Kapsülleme

class urun:
    def __init__(self):
        self.__fiyat = 1000 # fiyat değişkeni __ ile kapsüllenir
    def fiyatYaz(self):
        print("Ürün Fiyatı: ", self.__fiyat)
    def setFiyat(self,fiyat):
        self.__fiyat = fiyat
u = urun()
u.fiyatYaz()

u.__fiyat=900
u.fiyatYaz()

u.setFiyat(500)
u.fiyatYaz()


