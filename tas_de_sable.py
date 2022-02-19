#Contributors : GNICHI Rim - BACLE Arnaud - MOBRÉ Eliott - SUZANNE Jean-Alexandre


#########################################
# groupe MPCI 04
# Rim GNICHI
# Arnaud BACLE
# Eliott MOBRE
# Jean-Alexandre SUZANNE
# https://github.com/uvsq22101285/projet_tas_de_sable
#########################################

#PARTIE TKINTER

######################

#Import des librairies
import tkinter as tk
import random as r
from time import sleep
######################
#Fenêtres Affichages

#variables globales



######################
#PARTIE CODE 


#Import des librairies
import tkinter as tk
from time import sleep
long = 25

#Creer Matrice de 0
grille =  [[0 for i in range(long)] for j in range(long)]
grille[long//2][long//2] = 260

def FindColor(x,y,g):
    if g[x][y] == '#':
        return("blue")
    if g[x][y]<1:
        return("white")
    if g[x][y]<4:
        return("yellow")
    if g[x][y]<8:
        return("orange")
    return("red")

#ajout des bordures
def bordureFill(g,l,b):
    for i in range(l):
        for j in range(l):
            g[i][0] = b
            g[i][-1] = b
            g[0][j] = b
            g[-1][j] = b
    return g

def sandMove(l):
    global grille

    newGrille = [[0 for i in range(l)] for j in range(l)]
    for x in range(l):
        for y in range(l):
            num = grille[x][y]
            if num < 4  :
                newGrille[x][y] = grille[x][y]

    for x in range(long):
        for y in range(long):
            num = grille[x][y]
            if num >= 4 :
                newGrille[x][y] += num -4
                newGrille[x-1][y] +=1
                newGrille[x+1][y] +=1
                newGrille[x][y-1] +=1
                newGrille[x][y+1] +=1
    grille = newGrille

#WIDGET
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, height=450, width=450)

#affiche la grille
show = []
for x in range(long):
    columnShow = []
    for y in range(long):
        columnShow.append(canvas.create_rectangle(450/long*x,450/long*y,50+450/long*x,50+450/long*y,fill=FindColor(x,y,grille),outline="black") )
    show.append(columnShow)


for o in range(120) :
    bordureFill(grille,long,'#')
    for x in range(long):
        for y in range(long):
            canvas.itemconfig(show[x][y], fill=FindColor(x,y,grille))
            canvas.grid()   
    bordureFill(grille,long,0)
    sandMove(long)


racine.mainloop()