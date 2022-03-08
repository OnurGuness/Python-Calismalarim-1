# Dosya işlemleri

dosya = open("deneme.txt",mode='a',encoding='utf-8')
# c:\deneme.txt
# w - write modudur
#a -append üzerine ekle
#r - read okuma modu
#utf-8 karakter kodlama

dosya.write("birinci satır\n")
dosya.write("ikinci satır")

dosya.close()

#okuma işlemi
dosya = open("deneme.txt",mode='r',encoding='utf-8')
print(dosya.read())
dosya.close()


