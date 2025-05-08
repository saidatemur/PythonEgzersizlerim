with open("mailler.txt","r",encoding="utf-8") as file:
    karakter='@'
    for satir in file:
        satir=satir.strip("\n")
        if karakter in satir and satir.endswith(".com") :
            print(satir)