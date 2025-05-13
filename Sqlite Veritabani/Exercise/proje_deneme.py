import time

from kutuphane import *
print("""
**************
Kutuphane Programina hosgeldiniz.
Islemler:
1.Kitaplari goster
2.Kitaplari sorgula
3.Kitap ekle
4.Kitap sil
5.Baski yukselt

Cikmak icin "q" ye tikla

***************
""")
kutuphane=Kutuphane()

while True:
    islem=input("Yapacaginiz islem:")
    if islem=="q":
        print("Cikis yapiliyor......")
        break
    elif islem=="1":
        kutuphane.kitaplari_goster()
    elif islem=="2":
        isim=input("Hangi kitabi istiyorsunuz?")
        print("Kitap sorgulaniyor")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif islem=="3":
        isim=input("Kitabin ismi:")
        yazar = input("Kitabin yazari:")
        yayinevi = input("Kitabin yayinevi:")
        tur = input("Kitabin turu:")
        baski = input("Kitabin baskisi:")
        kitap=Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor....")
        time.sleep(2)
        kutuphane.kitap_ekle(kitap)
        print("Kitap eklendi....")

    elif islem=="4":
        isim=input("Hangi kitabi silmek istiyorsunuz?")
        cevap=input("Emin misiniz? (E/H)")
        if cevap=="E":
            print("Kitap siliniyor.....")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi......")

    elif islem=="5":
        isim=input("Hnagi kitabin baskisini yukseltmek istiyorsunuz ?")
        print("Baski yukleniyor.......")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baski yukseltildi")
    else:
        print("Gecersiz islem")
