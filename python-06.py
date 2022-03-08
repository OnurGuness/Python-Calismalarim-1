dizi = [0,1,2,3,4,5,6,7,8,9]

dizi[0]=5

print(dizi)
print(dizi[0])
print(dizi[1])
print(dizi[0:5])
print(dizi[3:7])
print(dizi[:3])
print(dizi[5:])
print(dizi[-1])
print(dizi[-2])

#dizi uzunluğu
print(len(dizi))
#string diziler
sdizi = ["elma","armut","portakal","muz"]
print(sdizi[0])

sdizi.append("üzüm")
print(sdizi)
del sdizi[1]
print(sdizi)
sdizi.remove("portakal")
print(sdizi)

sdizi.pop(2)
print(sdizi)

sdizi += ["armut","üzüm","portakal"]
print(sdizi)

sdizi *= 2
print(sdizi)

sayilar = [1,6,12,21,34,21,67,21,78,23,21,56,90,21]
sayilar.sort()
print(sayilar)

sayilar.reverse()
print(sayilar)

print(sayilar.count(21))

sayilar.clear()
print(sayilar)

sayilar.insert(0,12)
sayilar.insert(1,34)
sayilar.insert(1,23)
print(sayilar)

#2 boyutlu diziler
matris = [[1,3,6],[0,3,2],[2,7,3]]
print(matris)

print(matris[0])
print(matris[0][2])




