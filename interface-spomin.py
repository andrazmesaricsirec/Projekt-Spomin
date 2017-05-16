from program_spomin import Plosca, Karta
import tkinter as tk
from random import shuffle
from functools import partial
# ustvarimo ploščo
p = Plosca()

# pripravimo kup kart
kup_kart = []
with open("imena_kart.txt") as f:
    for vrstica in f:
        kup_kart.append(Karta(vrstica.strip()))
        kup_kart.append(Karta(vrstica.strip()))

# premešamo kup                
shuffle(kup_kart)

# razdelimo karte
p.dodaj_karte(kup_kart)


okno = tk.Tk()

def prikazi(l):
    i = l[0]
    j = l[1]
    gumb = gumbi[i][j]
    gumb.configure(text="a")


gumbi = []
for i in range(p.visina):
    vrstica = []
    for j in range(p.sirina):
        k = p.karte[i][j]
        action_with_arg = partial(prikazi, [i,j])
        gumb = tk.Button(text = "{}".format((i,j)), command = action_with_arg)
        gumb.grid(row = i, column = j)
        vrstica.append(gumb)
    gumbi.append(vrstica)

