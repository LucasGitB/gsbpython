from cgitb import grey
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import back, title
from tkinter import ttk
import mysql.connector as mysql

class Formulaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")


        #champs du formulaire
        frame1 = Frame(self.root, bg="grey")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="créer un compte", font=("Arial", 20, "bold"), bg="grey", fg="orange").place(x=50, y=30)

        #prenom et nom

        aff_prenom = Label(frame1, text="prenom", font=("arial", 15, "bold"), bg="grey", fg="black").place(x=50, y=100)
        self.ecri_prenom = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_prenom.place(x=50, y=130, width=250)

        aff_nom = Label(frame1, text="prenom", font=("arial", 15, "bold"), bg="grey", fg="black").place(x=370, y=100)
        self.ecri_nom = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_nom.place(x=370, y=130, width=250)


        aff_email = Label(frame1, text="email", font=("arial", 15, "bold"), bg="grey", fg="black").place(x=50, y=200)
        self.ecri_email = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_email.place(x=50, y=230, width=250)

        aff_mdp = Label(frame1, text="mot de passe", font=("arial", 15, "bold"), bg="grey", fg="black").place(x=370, y=200)
        self.ecri_mdp = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_mdp.place(x=370, y=230, width=250)

        #valider le formulaire
        btn = Button(frame1, text = "Créer", cursor="hand2", command=self.creer, font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 430, width=250)
        btn = Button(frame1, text = "login", cursor="hand2", command=self.login, font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 330, width=250)
        
    def creer(self):
            if self.ecri_prenom.get()=="" or self.ecri_email.get()=="" or self.ecri_nom.get()=="" or self.ecri_mdp.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = mysql.connect(host="192.168.56.104", user="gsbpython", password='gsbgsbgsb', database='gsbpython')
                cursor = conn.cursor()
                cursor.execute('insert into visiteur (nom, prenom, Mail, Password) values(%s, %s, %s, %s)',
                (
                    self.ecri_nom.get(),
                    self.ecri_prenom.get(),
                    self.ecri_email.get(),
                    self.ecri_mdp.get()
                ))

            conn.commit()
            messagebox.showinfo('succes', "visiteur ajouté")
            conn.close()


    def login(self):
        self.root.destroy()
        import login


root=Tk()
obj = Formulaire(root)
root.mainloop()