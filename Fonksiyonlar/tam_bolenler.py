def tam_bolenler(sayi):
   sayilar=[]
   for i in range(2,sayi):
       if sayi % i == 0:
           sayilar.append(i)
   return (sayilar)
while True:
    sayi=input("Sayi:")
    if sayi=="q":
        break
    else:
        sayi=int(sayi)
        print("Sayinin tam bolenleri:",tam_bolenler(sayi))
