import random
import time

print("""
*********************************************
Sayi Tahmin Oyunu

1 ile 40 arasinda sayiyi tahmin edin.
*********************************************
""")
rastgele_sayi=random.randint(1,40)
tahmin_hakki=7
while True:
    tahmin=int(input("Tahmininiz:"))
    if tahmin<rastgele_sayi:
        print("Bilgiler sorgulaniyor....")
        time.sleep(1)
        print("Daha yuksek sayi soyleyin!")
        tahmin_hakki-=1
    elif tahmin>rastgele_sayi:
        print("Bilgiler sorgulaniyor....")
        time.sleep(1)
        print("Daha kucuk sayi soyleyin!")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulaniyor....")
        time.sleep(1)
        print("Tebrikler! Sayimiz:",rastgele_sayi)
        break
    if tahmin_hakki==0:
        print("Tahmin hakkiniz bitmistir!")
        print("Sayimiz:",rastgele_sayi)
        break

