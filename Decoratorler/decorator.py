


def ekstra (fonk):
    def wrapper (sayilar):
        ciftlerin_toplami=0
        ciftler=0
        teklerin_toplami=0
        tekler=0
        for sayi in sayilar:
            if (sayi % 2 == 0):
                ciftlerin_toplami += sayi
                ciftler += 1
            else:
                teklerin_toplami += sayi
                tekler += 1
        print("Cift sayilarin ortalamasi:",ciftlerin_toplami/ciftler)
        print("Tek sayilarin ortalamasi:", teklerin_toplami/tekler)
        fonk(sayilar)

    return wrapper




@ekstra
def ortalama_bul (sayilar):
    toplam=0
    for sayi in sayilar:
        toplam+=sayi
    print("Genel ortalama:",toplam/len(sayilar))

ortalama_bul([34,55,3,22,23,12,34,66,8,54])