#map, filter ve reduce

#map dizi elemanlarının tamamına uygulanacak işlemlerde kullanılır

liste = [2,5,6,7,9]
yeni_liste = list(map(lambda x:x**2,liste))
print(yeni_liste)

#map ile birden fazla fonksiyon uygulaması
def ikiKat(x):
    return x*2

def yari(x):
    return x/2

fonk = [ikiKat,yari]

for i in range(5):
    deger = list(map(lambda x:x(i),fonk))
    print(deger)


#filter dizi elemanlarının seçilmesinde kullanılır

liste = [1,5,6,9,16,27,45,46]
uce_bolunenler = list(filter(lambda x:x%3==0,liste))
print(uce_bolunenler)

# reduce dizi elemanlarının toplanması,çarpılması gibi işlemlerde kullanılır
from functools import reduce 
toplam = reduce(lambda x,y:x+y,liste)
print(toplam)


