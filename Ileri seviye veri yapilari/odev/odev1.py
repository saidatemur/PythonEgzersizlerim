"""cumle="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
cumle.lower()
for i in cumle:
    adet=0
    for j in cumle:
        if j==i:
            adet+=1

    print(i,":",adet)"""

#ikinci yontem
s="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans=dict()

for karakter in s:
    if karakter in frekans:
        frekans[karakter]+=1
    else:
        frekans[karakter]=0
for i,j in frekans.items():
    print(i,":",j)
