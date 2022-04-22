from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import font
from turtle import bgcolor, width
import mysql.connector as mysql

import sys
sys.path.append("connect")
import connect as i

class Rapport:
    def __init__(self, root, idUser):
        self.root = root
        self.user = idUser
        self.root.title("Formulaire")
        self.root.geometry("1920x1080")

        #formualaire
        Gestion_Frame = Frame(self.root, bd=5, bg="white")
        Gestion_Frame.place(x=50, y=50, width=1200, height=700)

        Gestion_title = Label(Gestion_Frame, text="Compte-rendu", font=("Arial", 20, "bold"), bg="#0685F6", fg="white").place(x=50, y=50)


        #Variable
        self.DateRapport = StringVar()
        self.MotifVisite = StringVar()
        self.Bilan = StringVar()
        self.Prescription = StringVar()
        self.medicament = StringVar()
        self.nbrMedicament = StringVar()



        #Id Pratitient
        # idPratitient = tk.Label(root, text = "veuillez")
        # idPratitient.pack()
        # listePraticient = ["uedh", "uerfyu", "uiefh"]
        # liste = ttk.Combobox(root, values = listePraticient)
        # liste.current(0)
        # liste.pack()


        
        idPratitient = Label(Gestion_Frame, text="Pratitien", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=150)
        
        idDate = Label(Gestion_Frame, text="Bilan", font=("arial", 20), bg="cyan")
        idDate.place(x=50, y=150)

        id_text = Entry(Gestion_Frame, textvariable=self.DateRapport, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=150)

#####
        idMotifVisite = Label(Gestion_Frame, text="Bilan", font=("arial", 20), bg="cyan")
        idMotifVisite.place(x=50, y=300)

        id_text = Entry(Gestion_Frame, textvariable=self.MotifVisite, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=300)

######
        idBilan = Label(Gestion_Frame, text="Bilan", font=("arial", 20), bg="cyan")
        idBilan.place(x=50, y=450)

        id_text = Entry(Gestion_Frame, textvariable=self.Bilan, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=450)

######
        idmedicament = Label(Gestion_Frame, text="Bilan", font=("arial", 20), bg="cyan")
        idmedicament.place(x=50, y=600)

        id_text = Entry(Gestion_Frame, textvariable=self.medicament, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=600)

    #Button ajouter
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", command=self.creer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=600, y=600, width=120)
        

 


    def creer(self):
            if self.Bilan.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('insert into rapport (DateRapport, MotifVisite, Bilan, medicament, idVisiteur) values(%s, %s, %s, %s, %s)',
                (
                    self.DateRapport.get(),
                    self.MotifVisite.get(),
                    self.Bilan.get(),
                    self.medicament.get(),
                    self.user
                ))

            conn.commit()
            messagebox.showinfo('succes', "Rapport ajouté !")
            conn.close()
                

def affichage(user):
    root=Tk()
    ojb = Rapport(root, user)
    root.mainloop()
