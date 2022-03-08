#Anonim fonksiyonlar ve Lambda kullanımı
#fonksiyon_ismi = lambda değisken : islem

ikiKat = lambda x : x*2

print(ikiKat(5))

kareAlma = lambda y : y**2
print(kareAlma(10))

liste = [1,3,2,6,7,9,10]
yeni_liste = list(filter(lambda x : (x%2==1),liste))
print(yeni_liste)

yeni_liste2 = list(map(lambda x:(x*3),liste))
print(yeni_liste2)



