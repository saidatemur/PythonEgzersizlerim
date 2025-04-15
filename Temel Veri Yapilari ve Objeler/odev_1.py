#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
from math import sqrt

"""""a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
sonuc=a*b*c
print("3 sayinin carpimi sonucu: {}".format(sonuc))


#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
kilo=int(input("kilonuz:"))
boy=int(input("boyunuz:"))
kitleIndeksi=kilo/boy**2
print("Bedeninizin kitle indeksi: {}".format(kitleIndeksi))


#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini
# alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
kilometre=int(input("gittiginiz kilometre yol:"))
yakit=int(input("aracin kilometre basi yaktigi yakit:"))
yakit_fiyati=int(input("yakit fiyatini giriniz:"))
yakilan_yakit=kilometre/yakit
odeme=yakit_fiyati*yakilan_yakit
print("{} km yol icin {} litre yakit yaktiniz odemeniz gereken tutar: {} ".format(kilometre,yakilan_yakit,odeme))

#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
ad=input("adinizi gitriniz:")
soyad=input("soyadinizi giriniz:")
numara=input("numaranizi giriniz:")
print("adiniz {}\nsoyadiniz {}\nnumaraniz {}".format(ad,soyad,numara))
"""

#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
a=int(input("ilk degeri giriniz:"))
b=int(input("ikinci degeri giriniz:"))
a,b=b,a
print("ilk deger {} ikinci deger {}".format(a,b))

#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2
a=int(input("dik ucgenin 1.kenari:"))
b=int(input("dik ucgenin 2.kenari:"))
c=sqrt(a**2+b**2)
print("ucgenin hipotenuzu {}".format(c))