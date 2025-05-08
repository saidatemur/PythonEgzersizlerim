s=str()
with open("siir.txt","r",encoding="utf-8") as file:
    for satir in file:
        s+=satir[0]
print(s)