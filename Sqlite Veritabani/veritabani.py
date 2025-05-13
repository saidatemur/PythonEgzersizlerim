import sqlite3
con=sqlite3.connect("kutuphane.db")
cursor=con.cursor()
def tablo_ekleme():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(Isim TEXT, Yazar TEXT, Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('Istanbul Hatirasi','Ahmet Umit','Everest Yayincilik',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
       
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste=cursor.fetchall()
    print("Kitaplik tablosunun bilgileri")
    for i in liste:
        print(i)
    
def verileri_al2():
    cursor.execute("SELECT Isim,Yazar FROM kitaplik")
    liste=cursor.fetchall()
    print("Kitaplarin isimi ve yazarlari")
    for i in liste:
        print(i)

def verilari_al3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik where Yayinevi == ?",(yayinevi,))
    liste=cursor.fetchall()
    print("Belli yayinevinin kitap bilgileri")
    for i in liste:
        print(i)

def veriyi_guncelle(eski_yayin, yeni_yayin):
    cursor.execute("UPDATE kitaplik SET Yayinevi=? WHERE Yayinevi=? ",(yeni_yayin,eski_yayin))
    con.commit()
   
def veriyi_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE Yazar=?",(yazar,))
    con.commit()

veriyi_sil("Ahmet Umit")
verileri_al()
con.close()
