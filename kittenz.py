#!usr/bin/python
from tkinter import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# On crée une fenêtre, racine de notre interface
fenetre = Tk("Miaou")

#zone de texte
text = Text(fenetre)
text.pack()

#on tente une image wesh, on veut un FUCKING CHATON TROP MIGNON 
imgpil = Image.open("kitten.png")
# anciennement np.asarray
img = np.array(imgpil) # Transformation de l'image en tableau numpy
plt.imshow(img)
plt.show()

#couleur du texte
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

var_choix.get()

#le bouton quitter
quit = Button(fenetre, text="abandonner les bébés chats sur une aire d'autoroute", command=fenetre.quit)
quit.pack()

fenetre.mainloop()
