from random import shuffle

class Plosca:

    def __init__(self, sirina=4, visina=4):
        self.sirina = sirina
        self.visina = visina
        self.karte = []
        for _ in range(visina):
            vrstica = []
            for _ in range(sirina):
                vrstica.append(None)
            self.karte.append(vrstica)

    def dodaj_karte(self, kup_kart):
        for i in range(self.visina):
            for j in range(self.sirina):
                self.karte[i][j] = kup_kart[]

class Karta:

    def __init__(self, ime):
        self.ime = ime

# ustvarimo ploščo
p = Plosca()

# pripravimo kup kart
kup_kart = []
with open(imena_kart.txt) as f:
    for vrstica in f:
        kup_kart.append(Karta(vrstica.strip()))
        kup_kart.append(Karta(vrstica.strip()))

# premešamo kup                
shuffle(kup_kart)

# raydelimo karte
p.dodaj_karte(kup_kart)
