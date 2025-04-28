#Problem 1
"""liste = ["345", "sadas", "324a", "14", "kemal"]

for eleman in liste:

    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass  # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.

"""
#Problem 2
def çift_mi(sayı):
    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass
