from cgitb import grey
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import back, title
from tkinter import ttk
import mysql.connector as mysql

import sys
sys.path.append("connect")
import connect as i

class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Inscription")
        self.root.geometry("1920x1080+0+0")


        #champs du formulaire
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="Inscription", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=30)

        #prenom et nom

        aff_prenom = Label(frame1, text="Prénom", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=50, y=100)
        self.ecri_prenom = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_prenom.place(x=50, y=130, width=250)

        aff_nom = Label(frame1, text="Nom", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=370, y=100)
        self.ecri_nom = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_nom.place(x=370, y=130, width=250)


        aff_email = Label(frame1, text="Email", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=50, y=170)
        self.ecri_email = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_email.place(x=50, y=200, width=250)

        aff_mdp = Label(frame1, text="Mot de passe", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=370, y=170)
        self.ecri_mdp = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey", show="•")
        self.ecri_mdp.place(x=370, y=200, width=250)

        aff_r = Label(frame1, text="Rôle", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=50, y=240)
        self.ecri_r = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_r.place(x=50, y=270, width=250)

        #valider le formulaire
        btn = Button(frame1, text = "S'inscrire", cursor="hand2", command=self.creer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=250, y=340, width=250)
        btn = Button(frame1, text = "Se connecter", cursor="hand2", command=self.login, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=250, y=410, width=250)
        
    def creer(self):
            if self.ecri_prenom.get()=="" or self.ecri_email.get()=="" or self.ecri_nom.get()=="" or self.ecri_mdp.get()=="":
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('insert into utilisateur (nom, prenom, Mail, Password, role) values(%s, %s, %s, MD5(%s), %s)',
                (
                    self.ecri_nom.get(),
                    self.ecri_prenom.get(),
                    self.ecri_email.get(),
                    self.ecri_mdp.get(),
                    self.ecri_r.get()
                ))

            conn.commit()
            messagebox.showinfo('Succès', "Visiteur ajouté")
            conn.close()


    def login(self):
        self.root.destroy()
        import login


root=Tk()
obj = Formulaire(root)
root.mainloop()