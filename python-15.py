# Constructer (yapıcı) fonksiyonlar

class cokgen:
    def __init__(self,g,y):
        self.genişlik = g
        self.yükseklik= y
    def alan(self):
        return self.genişlik*self.yükseklik
dikdortgen = cokgen(20,10)
print(dikdortgen.genişlik," , ",dikdortgen.yükseklik)
print(dikdortgen.alan())

