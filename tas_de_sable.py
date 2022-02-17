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

######################
#Fenêtres Affichages

#variables globales
col = 0


#coordonnées du rectangle
x1,y1 = 150, 150
x2,y2 = 350, 350

#variable qui dit si on continue de changer les couleurs
continuer = True 

def recommencer():
    """On verra"""
    global col, continuer
    col = 0
    continuer = True
    canvas.itemconfigure(rectangle, fill="red")

def gestion_clic(event):
    """On verra"""
    global col, continuer
    if continuer == False:
        return 

    liste_col= ["blue","pink"]

    #Si on clique dans le rectangle
    if x1 < event.x < x2 and y1 < event.y < y2:
        col = 1 - col
        canvas.itemconfigure(rectangle, fill=liste_col[col])
    else:
        continuer = False 

#création des widgets
racine = tk.Tk()
racine.title("Lugras est Moregros")
canvas = tk.Canvas(racine, bg="black", heigh=500, width=500)
bouton = tk.Button(racine, text="Recommencer", command=recommencer)


#création du rectangle
rectangle = canvas.create_rectangle((x1,y1),(x2,y2), fill="red")

#liaison de l'événement 
canvas.bind('<Button-1>', gestion_clic)



#positionnement des widgets
canvas.grid()
bouton.grid(row=1)
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