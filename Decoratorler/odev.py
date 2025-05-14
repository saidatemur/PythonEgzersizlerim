def ekstra (fonk) :
    def wrapper (sayilar) :
        mukemmel_sayilar=list()
        for sayi in sayilar :
            i=1
            sonuc=0
            while i< sayi :
                if sayi % i ==0 :
                    sonuc+=i
                i+=1
            if sonuc == sayi :
                mukemmel_sayilar.append(sayi)

        fonk(sayilar)
        print("Mukemmel sayilar",mukemmel_sayilar)
    return wrapper



@ekstra
def asal_sayiler (sayilar) :
    asallar=list()
    for sayi in sayilar :
        sayac=0
        i=2
        while i < sayi:
            if (sayi % i == 0) :
                sayac+=1
            i+=1
        if (sayac == 0):
            asallar.append(sayi)
    print("Asal sayilar:", asallar)

asal_sayiler(range(2,2001))
