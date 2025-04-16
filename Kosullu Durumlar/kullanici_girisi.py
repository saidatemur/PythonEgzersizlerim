print("""*********************
Kullanici Girisi
*********************
""")

sys_kullanici_adi="poncikk"
sys_parola="12345"

kullanici_adi=input("Kullanici adi:")
parola=input("parola:")


if (kullanici_adi==sys_kullanici_adi and parola!=sys_parola):
    print("Parola hatali...")
elif (kullanici_adi!=sys_kullanici_adi and parola==sys_parola):
    print("Kullanici adi hatali...")
elif (kullanici_adi!=sys_kullanici_adi and parola!=sys_parola):
    print("Kullanici adi ve parola hatali...")
else:
    print("Sisteme basariyla giris yapildi...")