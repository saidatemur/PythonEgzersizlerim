""" Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

     Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

     BKİ 18.5'un altındaysa -------> Zayıf

     BKİ 18.5 ile 25 arasındaysa ------> Normal

     BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

     BKİ 30'un üstündeyse -------------> Obez
"""
"""
kilo=int(input("kilonuz:"))
boy=int(input("boyunuz:"))
bki=kilo/(boy**2)
print(bki)
if bki<18.5:
    print("Zayif")
elif (bki>18.5 and bki<25):
    print("Normal")
elif (bki>25 and bki<30):
    print("Fazla Kilo")
else:
    print("Obez")"""

"""Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
"""
a=int(input())
b=int(input())
c=int(input())
d=max(a,b,c)
print(d)
"""

""" Problem 3
Kullanıcının girdiği **vize1,vize2,final notlarına** notlarına göre harf notunu hesaplayın.
        Vize1 toplam notun %30'una etki edecek.
        Vize2 toplam notun %30'una etki edecek.
        Final toplam notun %40'ına etki edecek.

        Toplam Not >=  90 -----> AA
        Toplam Not >=  85 -----> BA
        Toplam Not >=  80 -----> BB
        Toplam Not >=  75 -----> CB
        Toplam Not >=  70 -----> CC
        Toplam Not >=  65 -----> DC
        Toplam Not >=  60 -----> DD
        Toplam Not >=  55 -----> FD
        Toplam Not <  55 -----> FF
"""

"""
vize1=int(input("vize1:"))
vize2=int(input("vize2:"))
final=int(input("final:"))
ort=(vize1*30+vize2*30 +final*40)/100
print(ort)

if ort>=90:
    print("AA")
elif ort>=85:
    print("BA")
elif ort>=80:
    print("BB")
elif ort>=75:
    print("CB")
elif ort>=70:
    print("CC")
elif ort>=65:
    print("DC")
elif ort>=60:
    print("DD")
elif ort>=55:
    print("FD")
else :
    print("FF")
"""


""" Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun. 

Eğer kullanıcı "Dörtgen" cevabını verirse ,  4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse ,  3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

*Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.*

*Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;*
"""
print("ucgen \ndortgen")
sekil=input("yukaridaki sekillerden birini girin:")
if sekil=="dortgen":
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))
    d=int(input("4.kenar:"))
    if (a==b and a==c and a==d and a==c and a==d and c==d):
        print("Kare")
    elif(a==c and b==d and a!=b):
        print("Dikdortgen")
    else:
        print("Dortgen")

elif sekil=="ucgen":
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")
