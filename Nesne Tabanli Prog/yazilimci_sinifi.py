class Yazilimci():
    diller=[]
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgilerigoster(self):
        print("""
        Yazilimci objesinin ozellikleri
        Isim:{}
        Soyisim:{}
        Numara:{}
        Maas:{}
        Bildigi Diller:{}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def zam_yap(self,zam_miktari):
        print("Zam yapiliyor")
        self.maas+=zam_miktari
    def dil_ekle(self,dil):
        print("Dil ekleniyor")
        self.diller.add(dil)


class main():
    yazilimci=Yazilimci("Saida","Temur","5675698754",60000,{"Java","Python","C"})
    yazilimci.bilgilerigoster()
    yazilimci.dil_ekle(".Net")
    yazilimci.zam_yap(5000)
    yazilimci.bilgilerigoster()