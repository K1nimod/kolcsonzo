class Kolcsonzes:
    def __init__(self,nev,jarmuazonosito,elvitelora,elvitelperc, visszaora, visszaperc):
        self.nev = nev
        self.jarmuazonosito = jarmuazonosito
        self.elvitelora = elvitelora
        self.elvitelperc = elvitelperc
        self.visszaora = visszaora
        self.visszaperc = visszaperc
        
    def __str__(self):
        return f"{self.nev} {self.jarmuazonosito} {self.elvitelora} {self.elvitelperc} {self.visszaora} {self.visszaperc}"
        
f = open("kolcsonzesek.txt", "r", encoding="utf-8")
f.readline()
lista = []

for sor in f:
    sor = sor.strip().split(";")
    lista.append(Kolcsonzes(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5]))

f = open("kolcsonzesek.txt", "r", encoding="utf-8")
f.readline()

kolcsonzes = {}
napi = 0
db = 0

for line in f:
    temp = line.strip().split(";")
    if line[1] in kolcsonzes.keys():
        kolcsonzes[line[1]] +=1
    else:
        kolcsonzes[line[1]] =1
    db +=1
print(f"5. feladat: {db} kölcsönzés adatai vannak a forrásban")

nev = input("Adja meg a nevet: ")

for sor in lista:
    if nev == "":   
        print(f"{sor[2]}:{sor[3]}-{sor[4]}:{sor[5]}")





print("10. feladat")
for k,v in kolcsonzes.items():
    print(f"{k} - {v}")