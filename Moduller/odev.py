import math
from math import *
print("""
*********************************************
Gelismis Hesap Makinesi

Yapmak istediginiz islemi seciniz(Cikmak icin q):
1.Toplama
2.Cikarma
3.Carpma
4.Bolme
5.Faktoriyel
6.Log
7.Mutlak Deger
8.Kare Kok
9.Kuvvet alma
10.Cos
11.Sin
12.Tan
13.e


*********************************************
""")


def cikarma(*sayilar):
    sonuc=0
    for i in sayilar:
        sonuc-=i
    return sonuc



def toplama(*sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc += i
    return sonuc



def carpma(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    return sonuc


"""def bolme(sayilar):
    sonuc = 0
    for i in sayilar:
        i = int(i)
        sonuc = i
    return sonuc"""


while True:
    islem=input("islem:")
    if islem =="1":
        sayilar=[]
        sayilar=int(input())
        print(toplama(sayilar))
    elif islem == "2":
        sayilar = int(input())
        print(cikarma(sayilar))
    elif islem == "3":
        sayilar = int(input())
        print(carpma(sayilar))
    elif islem == "4":
        sayilar = int(input())
        print(bolme(sayilar))
    elif islem == "5":
        sayilar=int(input())
        print(factorial(sayilar))
    elif islem == "6":
        sayilar=int(input())
        print(log(sayilar))
    elif islem == "7":
        sayilar=int(input())
        print(fabs(sayilar))
    elif islem == "8":
        sayilar=int(input())
        print(sqrt(sayilar))
    elif islem == "9":
        sayilar=int(input())
        print(pow(sayilar))
    elif islem == "10":
        sayilar=int(input())
        print(cos(sayilar))
    elif islem == "11":
        sayilar=int(input())
        print(sin(sayilar))
    elif islem == "12":
        sayilar=int(input())
        print(tan(sayilar))
    elif islem == "13":
        sayilar=int(input())
        print(exp(sayilar))
    elif islem == "q":
        break

