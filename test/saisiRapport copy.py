from tkinter import *
from tkinter import ttk, messagebox
from turtle import bgcolor, width
import mysql.connector as mysql

class Etudiant:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080")

        #formualaire
        Gestion_Frame = Frame(self.root, bd=5, bg="black")
        Gestion_Frame.place(x=50, y=50, width=600, height=700)

        Gestion_title = Label(Gestion_Frame, text="Compte rendu", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=50, y=50)

        #Id Visiteur
        idVisiteur = Label(Gestion_Frame, text="ID Visiteur", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=50, y=150)
        id_txt = Entry(Gestion_Frame, font=("Arial", 20, "bold"), bg="white", fg="black").place(x=220, y=150)

        #Nom Visiteur
        idNom = Label(Gestion_Frame, text="Nom", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=50, y=210)
        nom_txt = Entry(Gestion_Frame, font=("Arial", 20, "bold"), bg="white", fg="black").place(x=220, y=210)

        #Bilan Visiteur
        idBilan = Label(Gestion_Frame, text="Bilan", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=50, y=270)
        bilan_txt = Text(Gestion_Frame, font=("Arial", 20, "bold"), bg="white", fg="black").place(x=220, y=270, width=300,height=300)

        #Button ajouter
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=10, y=600, width=120)

        #Button modifier
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=150, y= 600, width=120)

        #Button supprimer
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=300, y= 600, width=120)

        #Button réinitialiser
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=450, y= 600, width=120)
        
        #recherche
        Details_Frame = Frame(self.root, bd=5, bg="black").place(x=700, y=50, width=1100, height=700)

        Affiche_resultat = Label(Details_Frame, text="Rechercher par", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=50, y=50)

        # recherche = ttk.Combobox(Details_Frame, font=("Arial", 20), state="readonly").place(x=350, y=55, width=180,height=40)
        # recherche["values"]=("id", "nom", "contact")

        # recherche_text = Entry(Details_Frame, font=("Arial", 20).place(x=550, y=55, height=40))

        # btn_recherche = Button(Details_Frame, text = "Rechercher", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=810, y=55, width=120, height=40)

        # btn_recherche = Button(Details_Frame, text = "Tout afficher", cursor="hand2", font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=940, y=55, width=135, height=40)
        


root=Tk()
obj = Etudiant(root)
root.mainloop()