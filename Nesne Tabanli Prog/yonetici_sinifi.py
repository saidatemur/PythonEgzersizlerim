class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin init fonku")
        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgilerigoster(self):
        print("""
        Calisan sinifinin bilgileri
        Isim:{}
        Maas:{}
        Departman:{}
        """.format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman

class Yonetci(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yonetici sinifinin init fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisi_sayisi=kisi_sayisi

    def bilgilerigoster(self):
        print("""
        Yonetici sinifinin bilgileri
        Isim:{}
        Maas:{}
        Departman:{}
        Sorumlu Kisi Sayisi:{}
        """.format(self.isim,self.maas,self.departman,self.kisi_sayisi))


    def zaam_yap(self,zam_miktati):
        self.maas+=zam_miktati


class Main():
    yonetici=Yonetci("Saida Temur",60000,'Bilisim',15)
    yonetici.departman_degistir("Insan Kaynaklari")
    yonetici.zaam_yap(10000)
    yonetici.bilgilerigoster()
    yonetici2=Yonetci("SudeNaz Kutuk",60000,"Bilisim",5)
