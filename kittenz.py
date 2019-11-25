# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

#Miaou !
champ_label = Label(fenetre, text="Miaou !")
champ_label.pack()

#zone de texte
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=200)
ligne_texte.pack()

#le bouton quitter
quit = Button(fenetre, text="abandonner les bébés chats sur une aire d'autoroute", command=fenetre.quit)
quit.pack()

fenetre.mainloop()
