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
import tkinter as tk
from time import sleep

######################
#Fenêtres Affichages


#variables globales
long = 10
N = 0
grille = []
go = False
T = 0
O =1

def start():
    """lance la simulation"""
    global long, go, O
    #if box.askyesno('Lancement Programme','Lancer la simulation ?') == True:
        #long = int(entry.get())
    go = True
    O = 0

def temporaire():
    """Temporaire pour la fonction de coloration de grille"""
    global T, go
    #if box.askyesno('Lancement Programme','Lancer la simulation ?') == True:
    go = True
    #T = int(entry_temp.get())
def recommencer():
    global N
    if box.askyesno('Recommencer', 'Voulez vous relancez la simulation ?') == True:
        N = 0

while O == 1:
    commande = tk.Tk()
    canvas_temp = tk.Canvas(commande)
    #entry = Entry(commande, text="Tapez la taille du carré")
    #entry_temp = Entry(commande)
    bouton_start = tk.Button(commande, text="Commencer la simulation", command=start)
    #bouton_recommencer = tk.Button(commande, text="Recommencer", command=recommencer)
    #bouton_temporaire = tk.Button(commande, text="temporaire", command=temporaire)
    #entry.grid(row=1)
    #entry_temp.grid(row=2)
    bouton_start.grid(row = 3)
    #bouton_recommencer.grid(row=4)
    #bouton_temporaire.grid(row=5)

    commande.mainloop()


######################
#PARTIE CODE 


#Import des librairies



#Creer Matrice de 0
<<<<<<< HEAD

    
=======
grille =  [[0 for i in range(long)] for j in range(long)]
grille[long//2][long//2] = 25
>>>>>>> fc3bcbe2c37dd99a7832a7ad0e9c38699ad450bc

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

    racine = tk.Tk()
    racine.title("Tas de sable")
    canvas = tk.Canvas(racine, height=450, width=450)
    racine.eval('tk::PlaceWindow %s center' % racine.winfo_toplevel())

<<<<<<< HEAD
    show = []
=======
for o in range(16) :
    bordureFill(grille,long,'#')
>>>>>>> fc3bcbe2c37dd99a7832a7ad0e9c38699ad450bc
    for x in range(long):
        columnShow = []
        for y in range(long):
            columnShow.append(canvas.create_rectangle(450/long*x,450/long*y,50+450/long*x,50+450/long*y,fill=FindColor(x,y,grille),outline="black") )
        show.append(columnShow)



    for o in range(20) :
        bordureFill(grille,long,'#')
        for x in range(long):
            for y in range(long):
                canvas.itemconfig(show[x][y], fill=FindColor(x,y,grille))
                canvas.grid()  

    sleep(1)  
    bordureFill(grille,long,0)
    sandMove(long)

    print(go)

    racine.mainloop()
