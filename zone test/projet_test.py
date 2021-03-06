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
from tkinter import messagebox as box
from tkinter import Entry 
from tkinter import Label

######################
#Fenêtres Affichages


#variables globales
long = 0
N = 0
grille = []
go = False
T = 1

############
#Fonctions Widget
def start():
    """lance la simulation"""
    global long, go, T
    if box.askyesno('Lancement Programme','Lancer la simulation ?') == True:
        long = int(entry.get())
        #T = int(entry_temp.get())
    go = True
    T = 0
    #commande.destroy()


def temporaire():
    """Temporaire pour la fonction de coloration de grille"""
    global T, go
    #if box.askyesno('Lancement Programme','Lancer la simulation ?') == True:
    go = True
    #T = int(entry_temp.get())

def stop():
    global T
    commande.destroy()
    T = 0

def reload():
    global T
    #racine.destroy()
    T = 1
    

######################
#PARTIE CODE 


#Import des librairies



#Creer Matrice de 0

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


#affiche la grille

if go == True:
    grille =  [[0 for i in range(long)] for j in range(long)]
    grille[long//2][long//2] = 16

    #racine = tk.Tk()
    #commande.title("Tas de sable")
    #bouton_reload = tk.Button(racine, text="Redémarrer la simulation", command=reload)
    #canvas = tk.Canvas(racine, height=450, width=450)
    #commande.eval('tk::PlaceWindow %s center' % commande.winfo_toplevel())
    #bouton_reload.grid(row = 1)

if T == 1:
    commande = tk.Tk()
    canvas = tk.Canvas(commande, height=500, width=500)
    entry = Entry(commande, text="Tapez la taille du carré")
    #entry_temp = Entry(commande)
    bouton_start = tk.Button(commande, text="Commencer la simulation", command=start)
    bouton_stop = tk.Button(commande, text="Stop", command=stop)
    #bouton_temporaire = tk.Button(commande, text="temporaire", command=temporaire)
    canvas.grid(column=2, row=2)
    carree = Label(commande, text="Choisir la taille du carré :")
    entry.grid(column=1,row=0)
    carree.grid(column=0, row=0)
    #entry_temp.grid(row=2)
    bouton_start.grid(column=0,row = 1)
    bouton_stop.grid(column=1,row=1)
    #bouton_temporaire.grid(row=5)

if go == True:
    show = []
    for x in range(long):
        columnShow = []
        for y in range(long):
            rectangle = canvas.create_rectangle(450/long*x,450/long*y,50+450/long*x,50+450/long*y,fill=FindColor(x,y,grille),outline="black")
            columnShow.append(rectangle)
        show.append(columnShow)

    for o in range(10) :
        bordureFill(grille,long,'#')
        for x in range(long):
            for y in range(long):
                canvas.grid(column=2)  
                canvas.itemconfig(show[x][y], fill=FindColor(x,y,grille))
                



commande.mainloop()

sleep(1)  
bordureFill(grille,long,0)
sandMove(long)

    #racine.mainloop()

