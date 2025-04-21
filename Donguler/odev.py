#Problem 1
#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
"""sayi=int(input("Bir sayi giriniz:"))
i=1
toplam=0
while i<sayi:
    if sayi%i==0:
        toplam+=i
    i+=1
if toplam!=sayi:
    print("girdiginiz sayi mukemmel sayi degildir")
else:
    print("girdiginiz sayi mukemmel sayidir")
"""


#Problem 2
#Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
"""sayi=(input("bir sayi giriniz:"))
uzunluk=len(sayi)
sonuc=0
deger=int(sayi)
for eleman in sayi:
    print(eleman)
    sonuc+=int(eleman)**uzunluk
    print(sonuc)
if sonuc!=deger:
    print("girdiginiz sayi armstrong sayisi degildir")
else:
    print("girdiginiz sayi armstrong sayisidir")
"""

#Problem 3
#1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
"""sayilar=[*range(1,11)]
print(sayilar)
for i in sayilar:
    print("************************")
    for j in sayilar:
        print("{}x{}={}".format(i,j,i*j))
"""
#Problem 4
#Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği
#sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı
#zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""toplam=0
while True:
    sayi=input("Sayi giriniz (sonuc icin q ye basiniz):")
    if sayi!="q":
        sayi1=int(sayi)
        toplam+=sayi1
    else:
        break
print(toplam)
"""

#Problem 5
#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
#Bu işlemi ***continue*** ile yapmaya çalışın.
"""
for i in range(1,101) :
    if i%3==0:
        print(i)
    else:
        continue
"""
#Problem 6
#Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan
# sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
liste=[i for i in range(1,101) if i%2==0]
print(liste)