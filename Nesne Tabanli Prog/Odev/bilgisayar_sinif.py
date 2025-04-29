class Bilgisayar():
    def __init__(self,marka,islemci,ram,depolama,ekran_boyutu,isletim_sistemi,durum,ag_baglantisi):
        self.marka=marka
        self.islemci=islemci
        self.ram=ram
        self.depolama=depolama
        self.ekran_boyutu=ekran_boyutu
        self.isletim_sistemi=isletim_sistemi
        self.durum=durum
        self.ag_baglantisi=ag_baglantisi

    def __str__(self):
        return "Marka:{}\nIslemci:{}\nRam:{}\nDepolama:{}\nEkran Boyutu:{}\nIsletim Sistemi:{}\nDurumu:{}\nAg Baglantisi:{}\n".format(self.marka,self.islemci,self.ram,self.depolama,self.ekran_boyutu,self.isletim_sistemi,self.durum,self.ag_baglantisi)
    