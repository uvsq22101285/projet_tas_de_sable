#Contributors : GNICHI Rim - BACLE Arnaud - MOBRÉ Eliott - SUZANNE Jean-Alexandre

#PARTIE TKINTER

######################

#Import des librairies
import tkinter as tk
import random as r
from time import sleep

######################
#Fenêtres Affichages

#Constantes

HAUTEUR = 600
LARGEUR = 600

######################
#WIDGET

racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)

#placement des widgets
canvas.grid(column=1, row=0)

racine.mainloop()

#PARTIE CODE 

#création de la grille et répartition du sable
width, height, nbrInit  = 5, 5, 32
grille =  [[0 for i in range(width)] for j in range(height)]
grille[width//2][height//2] = nbrInit
print(grille)

def SandMove():
    
    global grille
    newGrille = [[0 for i in range(width)] for j in range(height)]

    for x in range(width):
        for y in range(height):
            num = grille[x][y]
            if num < 4:
                newGrille[x][y] = grille[x][y]

    for x in range(width):
        for y in range(height):
            num = grille[x][y]
            if num >= 4:
                newGrille[x][y] = grille[x][y] -4
                newGrille[x+1][y] +=1
                newGrille[x-1][y] +=1
                newGrille[x][y+1] +=1
                newGrille[x][y-1] +=1
    grille = newGrille
    print(grille)

for u in range(12):
    SandMove()
    sleep(2)