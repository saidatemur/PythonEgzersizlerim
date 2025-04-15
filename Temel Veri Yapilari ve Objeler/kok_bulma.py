"""
2.dereceden bir bilinmeyenli denklemin koklerini bulma
denklem: ax^2+bx+c
deltayi hesapla : b**2-4*a*c
birinci kok:(-b-delta**0.5)/(2*a)
ikinci kok:(-b+delta**0.5)/(2*a)
"""
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
delta=b**2-4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)
print("Birinci kok: {}\nIkinci kok: {}\n".format(x1,x2))

