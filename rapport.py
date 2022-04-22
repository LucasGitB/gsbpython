from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import font
from turtle import bgcolor, width
import mysql.connector as mysql

import sys
sys.path.append("connect")
import connect as i

class Etudiant:
    def __init__(self, root):
        self.root = root
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
        
        liste = ttk.Combobox(Gestion_Frame, font=("Arial", 13, "bold"), state='readonly')

        conn = i.idBdd
        cursor = conn.cursor()
        cursor.execute('select nom, prenom from praticien')
        row=cursor.fetchall()
        print(row)


        lstVal = ""
        for praticien in row: 
            lstVal += "{0} {1}," .format(praticien[0], praticien[1])

        # print(lstVal)
        valuesLst = lstVal.split(',')
        
        print(valuesLst)
        liste['values'] = valuesLst
        liste.current(0)
        liste.pack()
        liste.place(x=220, y=150)
   

        #Id Date
        iddate = Label(Gestion_Frame,  text="Date visite", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=210)
        id_txt = Entry(Gestion_Frame, textvariable=self.DateRapport, font=("Arial", 13, "bold"), bg="white", fg="black").place(x=220, y=210)

        #Nom motif visite
        idMotif = Label(Gestion_Frame,  text="Motif visite", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=270)
        nom_txt = Entry(Gestion_Frame, textvariable=self.MotifVisite, font=("Arial", 13, "bold"), bg="white", fg="black").place(x=220, y=270)

        #Bilan 
        idBilan = Label(Gestion_Frame,  text="Bilan", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=330)
        bilan_txt = Text(Gestion_Frame, textvariable=self.Bilan, font=("Arial", 13, "bold"), bg="white", fg="black").place(x=220, y=330, width=300,height=300)

        #medicaments
        idMedicament = Label(Gestion_Frame,  text="Médicaments", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=550, y=150)
        medicament_txt = Text(Gestion_Frame, textvariable=self.medicament, font=("Arial", 13, "bold"), bg="white", fg="black").place(x=780, y=150, width=300,height=300)

        #Button ajouter
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", command=self.creer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=600, y=600, width=120)
        #Retour accueil 
        btn = Button(Gestion_Frame, text = "Accueil", cursor="hand2", command=self.accueil, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=900, y=600, width=120)



    def creer(self):
            if self.DateRapport.get()=="" or self.MotifVisite.get()=="" or self.Bilan.get()=="" or self.medicament.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('insert into rapport (DateRapport, MotifVisite, Bilan, medicament) values(%s ,%s, %s, %s)',
                (
                    self.DateRapport.get(),
                    self.MotifVisite.get(),
                    self.Bilan.get(),
                    self.medicament.get(),
                ))

            conn.commit()
            messagebox.showinfo('succes', "visiteur ajouté")
            conn.close()
                

    def accueil(self):
        self.root.destroy()
        import accueil



root=Tk()
obj = Etudiant(root)
root.mainloop()