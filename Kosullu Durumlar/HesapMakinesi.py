print("""
**************************
Hesap Makinesi Programi

Islemler:
1. Toplama islemi
2. Cikarma islemi
3. Carpma islemi
4. Bolme islemi
**************************
""")

a=int(input("Birinci sayi:"))
b=int(input("Ikinci sayi:"))
islem=input("islem giriniz:")
if islem=='1':
    print("{} ile {} nin tolami {} dir".format(a,b,a+b))
elif islem=='2':
    print("{} ile {} nin farki {} dir".format(a, b, a - b))
elif islem=='3':
    print("{} ile {} nin carpimi {} dir".format(a, b, a * b))
elif islem=='4':
    print("{} ile {} nin bolumu {} dir".format(a, b, a / b))
else:
    print("Gecersiz islem girildi")