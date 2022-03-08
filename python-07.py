
m1 = [[2,0,3],
       [4,5,2],
       [7,0,1]]

for i in range(3):
    print(m1[i])

m2 = [[0,1,4],
       [0,1,2],
       [0,1,1]]
print()
for i in range(3):
    print(m2[i])
m3 = [[0,0,0],
      [0,0,0],
      [0,0,0]]
for  i in range(3):
    for j in range(3):
        m3[i][j]= m1[i][j] +m2[i][j]
print()
for i in range(3):
    print(m3[i])




