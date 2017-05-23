from program_spomin import Plosca, Karta
import tkinter as tk
from random import shuffle
from functools import partial
import time
import turtle


class Program:

    def __init__(self):
        self.p = Plosca()
        self.kup_kart = []
        self.prvi_gumb = None
        self.drugi_gumb = None
        self.prvi_i = None
        self.prvi_j = None
        self.drugi_i = None
        self.drufi_j = None
        self.gumbi = []
        self.stevec = 0
        self.stevec_poskusov = 0
        
        
    def pozeni(self):
        self.naredi_okno()
        self.pripravi_kup_kart()
        self.razdeli_karte()
        self.naredi_gumbe()
        self.naslovi()

    def naredi_okno(self):
        self.okno = tk.Tk().wm_title("Igra Spomin")
        self.frame_naslova = tk.Frame(self.okno)
        self.frame_naslova.pack()

        self.frame_stevcev = tk.Frame(self.okno)
        self.frame_stevcev.pack()
        
        self.frame_igre = tk.Frame(self.okno)
        self.frame_igre.pack()

    def naslovi(self):
        self.naslov = tk.Label(self.frame_naslova,text = 'SPOMIN', font=(30))
        self.naslov.pack()


        
        self.stevilo_poskusov_text = tk.Label(self.frame_stevcev, text = 'Število Poskusov:')
        self.stevilo_poskusov_text.grid(row = 0, column = 0)

        self.stevilo_poskusov = tk.Label(self.frame_stevcev, text = "")
        self.stevilo_poskusov.grid(row = 0, column = 1)

    def razdeli_karte(self):
        self.p.dodaj_karte(self.kup_kart)

    def pripravi_kup_kart(self):
        with open("imena_kart.txt") as f:
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
                gumb = tk.Button(self.frame_igre, text = "", image = slika_karte, command = action_with_arg)
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

                    self.stevec_poskusov += 1
                    self.stevilo_poskusov.configure(text = str(self.stevec_poskusov))
                    
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

                self.stevec += 1

                if self.stevec == 8:
                    self.konec()
                
                
            else:
                drugi.after(1000, lambda: self.obrni_karti(prvi, drugi))

        else:
            pass

    def obrni_karti(self, gumb_prvi, gumb_drugi):
        slika_karte = tk.PhotoImage(file = "blank.gif")
                            
        gumb_prvi.configure(text = "", image = slika_karte)
        gumb_prvi.image = slika_karte
                            
        gumb_drugi.configure(text = "", image = slika_karte)
        gumb_drugi.image = slika_karte
                            
        self.prvi_gumb = None
        self.drugi_gumb = None


    def konec(self):
        turtle.hideturtle()
        turtle.pencolor("green")
        turtle.write("ZMAGA!", align="center", font=("Arial", 40))
        


    
        

        
pr = Program()
pr.pozeni()

tk.mainloop()








        
    




