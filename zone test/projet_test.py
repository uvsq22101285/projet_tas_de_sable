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
from tkinter import font
from turtle import bgcolor
import tkinter as tk
from time import sleep

######################
#Fenêtres Affichages

#variables globales
long = 9
#Fonction lié aux WIDGETS

def recommencer():
    "pas le temps"
    global grille, long
    long = int(input())


#WIDGET
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, height=450, width=450)
bouton = tk.Button(racine, text="Recommencer", command=recommencer)





######################
#PARTIE CODE 


#Import des librairies


#Creer Matrice de 0
grille =  [[0 for i in range(long)] for j in range(long)]
grille[long//2][long//2] = 16

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
                newGrille[x][y] = grille[x][y] -4
                newGrille[x-1][y] +=1
                newGrille[x+1][y] +=1
                newGrille[x][y-1] +=1
                newGrille[x][y+1] +=1
    grille = newGrille



#affiche la grille
show = []
for x in range(long):
    colonnes = []
    for y in range(long):
        colonnes.append(canvas.create_rectangle(50*x,50*y,50+50*x,50+50*y,fill=FindColor(x,y,grille),outline="black") )
    show.append(colonnes)


for o in range(1) :
    bordureFill(grille,long,'#')
    for x in range(long):
        for y in range(long):
            canvas.itemconfig(show[x][y], fill=FindColor(x,y,grille))
            canvas.grid()  
    sleep(1)  
    bordureFill(grille,long,0)
    sandMove(long)



#Placement WIDGET

canvas.grid()
bouton.grid(row=1)
racine.mainloop()

