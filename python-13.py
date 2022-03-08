#Global, local ve nonlocal değişkenler

x = 2  #global

def fonksiyon():
    x = 5  #local değişken
    print("iç değer: ",x)

fonksiyon()

print("dışarı: ",x) #global olan x değişkenini alıyoruz

sayi = 10 #global

def f2():
    global sayi
    sayi = sayi * 2
    print("sayi değeri: ",sayi)
f2()





