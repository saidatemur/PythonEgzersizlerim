"""

Asal Sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.

"""
def asal_mi(sayi):
    if sayi==1:
        return False
    elif sayi==2:
        return True
    else:
        i=2
        sayac=0
        while i<sayi:
            if sayi%i==0:
                sayac+=1
            i+=1
        if sayac>0:
            return False
        else:
            return True
while True:
    sayi=input("Sayi:")
    if sayi=="q":
        break
    else:
        sayi=int(sayi)
        if asal_mi(sayi):
            print("Sayi asaldir")
        else:
            print("Sayi asal degildir")