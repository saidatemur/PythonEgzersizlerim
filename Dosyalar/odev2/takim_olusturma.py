with open("futbolcular.txt","r",encoding="utf-8") as file:
    galatasaraylar=[]
    fenerler=[]
    besiktaslar=[]
    for i in file:
      i=i[:-1]
      liste=i.split(",")
      if liste[1]=="Galatasaray":
          galatasaraylar.append(i)
      elif liste[1]=="Fenerbahçe":
          fenerler.append(i)
      else:
          besiktaslar.append(i)
    with open("fb.txt","w",encoding="utf-8") as file:
        for i in fenerler:
            file.write(i+"\n")
    with open("gs.txt","w",encoding="utf-8") as file:
        for i in galatasaraylar:
            file.write(i+"\n")
    with open("bjk.txt","w",encoding="utf-8") as file:
        for i in besiktaslar:
            file.write(i+"\n")
