import random as r
#random()
print(r.random())

#uniform(min,max)
print(r.uniform(1,10))

#randint(min,max)
print(r.randint(1000,1500))

#randrange(min,max,range)
print(r.randrange(1,10))
print(r.randrange(0,100,8))

#sample(liste,adet
sayi = range(1,50)
print(r.sample(sayi,6))


#shuffle(liste)
sayi = list(range(1,10))
r.shuffle(sayi)
print(sayi)

#choice(liste)
sayi = list(range(200,300))
print(r.choice(sayi))
meyve = ["elma","armut","kiraz","karpuz","erik","kavun"]
print(r.choice(meyve))

