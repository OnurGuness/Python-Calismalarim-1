#Recursive Fonksiyonlar
#6! =6.5.4.3.2.1

def faktoriyel(n):
    if n==1 or n==0:
        return 1
    else:
        return n * faktoriyel(n-1)

print(faktoriyel(6))

def toplam(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + toplam(liste[1:])
liste = [2,3,4,5,6]
print(toplam(liste))


