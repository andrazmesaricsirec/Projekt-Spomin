from program_spomin import Plosca, Karta
import tkinter as tk
from random import shuffle
from functools import partial
import time


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

        
    def pozeni(self):
        self.pripravi_kup_kart()
        self.razdeli_karte()
        self.naredi_gumbe()
        

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
        okno = tk.Tk()
        for i in range(self.p.visina):
            vrstica = []
            for j in range(self.p.sirina):
                k = self.p.karte[i][j]
                action_with_arg = partial(self.prikazi, [i,j])
                gumb = tk.Button(okno, text = "", command = action_with_arg, height = 8, width = 10)
                gumb.grid(row = i, column = j)
                vrstica.append(gumb)
            self.gumbi.append(vrstica)
            
    def prikazi(self, l):
        i = l[0]
        j = l[1]
        gumb = self.gumbi[i][j]
        if gumb is None:
            pass
        else:
            if gumb["text"] == "":
                gumb.configure(text = self.p.karte[i][j])
            else:
                gumb.configure(text = "")


            if self.prvi_gumb is None:
                self.prvi_gumb = gumb
                self.prvi_i = i
                self.prvi_j = j
            else:
                self.drugi_gumb = gumb
                self.drugi_i = i
                self.drugi_j = j
                
                self.enakost(self.prvi_gumb, self.drugi_gumb)

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
                
            else:
                
                prvi.configure(text = "")            
                drugi.configure(text = "")



                
                self.prvi_gumb = None
                self.drugi_gumb = None
        else:
            pass

        
pr = Program()
pr.pozeni()










        
    




