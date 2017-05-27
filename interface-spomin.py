import tkinter as tk
from random import shuffle
from functools import partial
import time
import datetime

class Plosca:

    def __init__(self, sirina=4, visina=4):
        self.sirina = sirina
        self.visina = visina
        self.karte = []

    def naredi_seznam(self):        
        for _ in range(self.visina):
            vrstica = []
            for _ in range(self.sirina):
                vrstica.append(None)
            self.karte.append(vrstica)

    def dodaj_karte(self, kup_kart):
        for i in range(self.visina):
            for j in range(self.sirina):
                self.karte[i][j] = kup_kart.pop()

class Karta:

    def __init__(self, ime):
        self.ime = ime

    def __str__(self):
        return "{}".format(self.ime)

    def __repr__(self):

        return "{}".format(self.ime)

class Program:

    def __init__(self, osnovno_okno):
        self.osnovno_okno = osnovno_okno
        self.p = Plosca()
        self.kup_kart = []
        self.prvi_gumb = None
        self.drugi_gumb = None
        self.prvi_i = None
        self.prvi_j = None
        self.drugi_i = None
        self.drufi_j = None
        self.gumbi = []
        self.stevec_pravilnih = 0
        self.stevec_poskusov = 0
        self.ime_datoteke = None
        self.potrebno_stevilo_za_zmago = None
        
    def deset(self):
        self.p.sirina = 10
        self.ime_datoteke = "imena_kart_10x4.txt"
        self.pozeni()
        self.potrebno_stevilo_za_zmago = 20 #20
        
    def stiri(self):
        self.p.sirina = 4
        self.ime_datoteke = "imena_kart_4x4.txt"
        self.pozeni()
        self.potrebno_stevilo_za_zmago = 8 #8
           
    def pozeni(self):
        self.naredi_okno()
        self.p.naredi_seznam()
        self.pripravi_kup_kart()
        self.razdeli_karte()
        self.naredi_gumbe()
        self.naslovi()

    def naredi_okno(self):
        self.okno = self.osnovno_okno
        self.okno.wm_title("Igra Spomin")
        self.frame_naslova = tk.Frame(self.okno)
        self.frame_naslova.pack()

        self.frame_stevcev = tk.Frame(self.okno)
        self.frame_stevcev.pack()
        
        self.frame_igre = tk.Frame(self.okno)
        self.frame_igre.pack()

    def naslovi(self):
        slika_naslova = tk.PhotoImage(file = "naslov.png")
        
        self.naslov = tk.Label(self.frame_naslova, image = slika_naslova)
        self.naslov.image = slika_naslova
        self.naslov.pack()
        
        self.stevilo_poskusov_text = tk.Label(self.frame_stevcev, text = 'Število Poskusov:')
        self.stevilo_poskusov_text.grid(row = 0, column = 0)

        self.stevilo_poskusov = tk.Label(self.frame_stevcev, text = "")
        self.stevilo_poskusov.grid(row = 0, column = 1)

    def razdeli_karte(self):
        self.p.dodaj_karte(self.kup_kart)

    def pripravi_kup_kart(self):
        with open(self.ime_datoteke) as f:
            for vrstica in f:
                self.kup_kart.append(Karta(vrstica.strip()))
                self.kup_kart.append(Karta(vrstica.strip()))

        shuffle(self.kup_kart)
        
    def naredi_gumbe(self):
        self.gumbi = []
        for i in range(self.p.visina):
            vrstica = []
            for j in range(self.p.sirina):
                k = self.p.karte[i][j]
                action_with_arg = partial(self.prikazi, [i,j])
                slika_karte = tk.PhotoImage(file = "blank.gif")
                gumb = tk.Button(self.frame_igre, text = "", image = slika_karte, command = action_with_arg, bg = "white")
                gumb.image = slika_karte
                gumb.grid(row = i, column = j)
                vrstica.append(gumb)
            self.gumbi.append(vrstica)
            
    def prikazi(self, l):
        i = l[0]
        j = l[1]
        gumb = self.gumbi[i][j]
        if gumb is None or self.prvi_gumb == gumb:
            pass
        else:
            if self.drugi_gumb == None:
                if gumb["text"] == "":
                    ime_slike = "{}.gif".format(self.p.karte[i][j])
                    trenutna_slika = tk.PhotoImage(file = ime_slike)
                    gumb.configure(text = self.p.karte[i][j], image = trenutna_slika)
                    gumb.image = trenutna_slika
                else:
                    slika_karte = tk.PhotoImage(file = "blank.gif")
                    gumb.configure(text = "", image = slika_karte)
                    gumb.image = slika_karte


                if self.prvi_gumb is None:
                    self.prvi_gumb = gumb
                    self.prvi_i = i
                    self.prvi_j = j
                else:
                    self.drugi_gumb = gumb
                    self.drugi_i = i
                    self.drugi_j = j

                    self.dodaj_poskus()
                    
                    self.enakost(self.prvi_gumb, self.drugi_gumb)
            else:
                pass

    def enakost(self, prvi, drugi):
        if prvi != drugi:
            if prvi["text"] == drugi["text"]:

                prvi.configure(command = None)
                drugi.configure(command = None)

                self.gumbi[self.prvi_i][self.prvi_j] = None
                self.gumbi[self.drugi_i][self.drugi_j] = None

                self.prvi_gumb = None
                self.drugi_gumb = None
                self.prvi_i = None
                self.drugi_i = None
                self.prvi_j = None
                self.drugi_j = None

                self.dodaj_pravilno_resitev()  
                
            else:
                drugi.after(800, lambda: self.obrni_karti(prvi, drugi))

        else:
            pass

    def dodaj_poskus(self):
        self.stevec_poskusov += 1
        self.stevilo_poskusov.configure(text = str(self.stevec_poskusov))

    def dodaj_pravilno_resitev(self):
        self.stevec_pravilnih += 1
        if self.stevec_pravilnih == self.potrebno_stevilo_za_zmago:
                self.konec()
           
    def obrni_karti(self, gumb_prvi, gumb_drugi):
        slika_karte = tk.PhotoImage(file = "blank.gif")
                            
        gumb_prvi.configure(text = "", image = slika_karte)
        gumb_prvi.image = slika_karte
                            
        gumb_drugi.configure(text = "", image = slika_karte)
        gumb_drugi.image = slika_karte
                            
        self.prvi_gumb = None
        self.drugi_gumb = None

    def konec(self):
        self.stevilo_poskusov_text.configure(font = "50", fg = "green")
        
        self.stevilo_poskusov.configure(font = "50", fg = "green")
        
        datoteka_rezultati = None
        if self.p.sirina == 4:
            datoteka_rezultati = "rezultati_4x4.txt"
        else:
            datoteka_rezultati = "rezultati_10x4.txt"
        
        datum = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        with open(datoteka_rezultati, "a") as r:
            r.write("{} poskusov ....... {}\n".format(str(self.stevec_poskusov), datum))
    
class Zacetek:

    def __init__(self, osnovno_okno):
        self.osnovno_okno = osnovno_okno

        self.frame = tk.Frame(self.osnovno_okno)
        self.frame.pack()
        
        self.naslov = tk.Label(self.frame, text = "Igra Spomin", font = ("bold", 20))
        self.naslov.grid(row = 0, column = 0, columnspan = 2)
        
        self.gumb_4x4 = tk.Button(self.frame, text = 'Start 4x4', width = 25, command = self.zazeni_program_4x4, fg = "green")
        self.gumb_4x4.grid(row = 1, column = 0)
        
        self.gumb_10x4 = tk.Button(self.frame, text = 'Start 10x4', width = 25, command = self.zazeni_program_10x4, fg = "green")
        self.gumb_10x4.grid(row = 1, column = 1)
        
        self.gumb_rezultati_4x4 = tk.Button(self.frame, text = 'Rezultati 4x4', width = 25, command = self.zazeni_program_rezultati_4x4)
        self.gumb_rezultati_4x4.grid(row = 2, column = 0)
        
        self.gumb_rezultati_10x4 = tk.Button(self.frame, text = 'Rezultati 10x4', width = 25, command = self.zazeni_program_rezultati_10x4)
        self.gumb_rezultati_10x4.grid(row = 2, column = 1)

        self.gumb_rezultati_izbris = tk.Button(self.frame, text = 'Izbrisi Rezultate', width = 51, command = self.izbrisi_rezultate, fg = "red")
        self.gumb_rezultati_izbris.grid(row = 3, column = 0, columnspan = 2)
        

    def zazeni_program_4x4(self):
        self.zazeni_program = tk.Toplevel(self.osnovno_okno)
        pr = Program(self.zazeni_program)
        self.zacetek_programa = Program(self.zazeni_program)
        self.zacetek_programa.stiri()

    def zazeni_program_10x4(self):
        self.zazeni_program = tk.Toplevel(self.osnovno_okno)
        pr = Program(self.zazeni_program)
        self.zacetek_programa = Program(self.zazeni_program)
        self.zacetek_programa.deset()

    def zazeni_program_rezultati_4x4(self):
        self.zazeni_program = tk.Toplevel(self.osnovno_okno)
        self.zacetek_programa = Rezultati(self.zazeni_program, 4)

    def zazeni_program_rezultati_10x4(self):
        self.zazeni_program = tk.Toplevel(self.osnovno_okno)
        self.zacetek_programa = Rezultati(self.zazeni_program, 10)

    def izbrisi_rezultate(self):
        open("rezultati_4x4.txt", "w").close()
        
        open("rezultati_10x4.txt", "w").close()

class Rezultati:
    def __init__(self, osnovno_okno, stevilo_polj):
        self.osnovno_okno = osnovno_okno
        self.stevilo_polj = stevilo_polj
        
        datoteka_rezultati = None
        if self.stevilo_polj == 4:
            datoteka_rezultati = "rezultati_4x4.txt"
        else:
            datoteka_rezultati = "rezultati_10x4.txt"
            
        self.osnovno_okno.wm_title("Rezultati")
        self.listbox = tk.Listbox(self.osnovno_okno)
        self.listbox.configure(width = 0, height = 25)
        
        with open(datoteka_rezultati, "r") as r:
            rezultati = r.readlines()
        rezultati = [x.strip() for x in rezultati] #brez /n

        self.listbox.pack()
        self.listbox.insert(tk.END, "Rezultati:")

        for rezultat in rezultati:
            self.listbox.insert(tk.END, rezultat)

def tk_okno():
    okno = tk.Tk()
    okno.wm_title("Zacetni meni")
    zacetek_programa = Zacetek(okno)
    okno.mainloop()

tk_okno()







#https://s-media-cache-ak0.pinimg.com/originals/74/0b/df/740bdfde43a6acc7dd91ae8818ad4f7d.jpg
#http://www.dogsinpictures.com/images/brown_white_clipart_dog_with_red_collar.jpg
#https://s-media-cache-ak0.pinimg.com/736x/e1/ff/ec/e1ffecab3045b6cc5703d5c3af05976a.jpg
#http://clipartix.com/panda-clipart-image-5792/
#https://openclipart.org/image/800px/svg_to_png/214620/1424522664.png
#http://images.clipartpanda.com/cupcake-clipart-Cupcake_Clipart_07.jpeg
#http://content.mycutegraphics.com/graphics/food/whole-pizza.png
#https://img.clipartfest.com/ef3d4171ede068fa9c442dcb73879406_electric-guitar-clip-art-electric-guitar-clipart_600-447.png
#http://images.clipartpanda.com/hot-air-balloon-clip-art-hot-air-balloon-md.png






        
    




