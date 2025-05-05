
#Problem 1
"""def carpma(list):
    return list[0]*list[1]

liste=[(3,4),(10,3),(5,6),(1,9)]
sonuc=list(map(carpma,liste))
print(sonuc)"""

#Problem 2
"""def ucgen(list):
    x = list[0]
    y = list[1]
    z = list[2]
    if x%3==0 and y%4==0 and z%5==0:
        return (x,y,z)
liste=[(3,4,5),(6,8,10),(3,10,7)]
sonuc=list(filter(ucgen,liste))
print(sonuc)"""

#Problem 3
from functools import reduce
liste=[1,2,3,4,5,6,7,8,9,10]
ciftler=list(filter(lambda x:x % 2 == 0,liste))
sonuc=reduce(lambda x,y:x+y,ciftler)
print(sonuc)

#Problem 4
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(isimler,soyisimler):
    print(i,j)