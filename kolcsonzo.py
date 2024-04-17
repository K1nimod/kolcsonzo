class kocsonzo:
    
    def __init__(self,nev,jazon,eora,eperc,vora,vperc):
        self.nev = nev
        self.jazon = jazon
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc
        
f = open("kolcsonzesek.txt", "r", encoding="utf-8")


kolcsonzo = {}

for sor in f:
    sor = sor.split(';')
    if sor[1] in kolcsonzo.keys():
        kolcsonzo[sor[1]] += 1 
    else:
        kolcsonzo[sor[1]] = 1

for k,v in kolcsonzo.items():
    print(k,v)