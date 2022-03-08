#sınıf ve nesne kavramı
a = input("Vize notunuz: ")
b = input("Fİnal notunuz: ")
class ogrenci:
    ad ="yasin"
    soyad="sağlam"

    def yazdir(self):
        print(self.ad)
        print(self.soyad)
    def ortalama(self,vize,final):
        c = (float(vize)*0.4)+(float(final)*0.6)
        return c

nesne = ogrenci()
print(nesne.ad,"-",nesne.soyad)
nesne.yazdir()

print("ortalama: ",nesne.ortalama(a,b))


