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
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="Connexion", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=30)

        #prenom et nom

        aff_email= Label(frame1, text="Email", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=50, y=100)
        self.ecri_email = Entry(frame1, font=("arial", 15), bg="white")
        self.ecri_email.place(x=50, y=130, width=250)

        aff_mdp = Label(frame1, text="Mot de passe", font=("arial", 15, "bold"), bg="white", fg="#0685F6").place(x=50, y=170)
        self.ecri_mdp = Entry(frame1, font=("arial", 15), bg="white")
        self.ecri_mdp.place(x=50, y=200, width=250)

        #valider le formulaire
        btn = Button(frame1, text = "connexion", cursor="hand2", command=self.connexion, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=200, y=430, width=120)
        btn = Button(frame1, text = "inscription", cursor="hand2", command=self.inscription, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=350, y=430 , width=120)


    def connexion(self):
            if self.ecri_email.get()=="" or self.ecri_mdp.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = mysql.connect(host="192.168.56.104", user="gsbpython", password='gsbgsbgsb', database='gsbpython')
                cursor = conn.cursor()
                cursor.execute('select * from visiteur where Mail=%s and Password=%s',
                (
                    self.ecri_email.get(),
                    self.ecri_mdp.get()
                ))
                row=cursor.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "identifiants incorrects", parent=self.root)
                else:
                    messagebox.showinfo("Succes", "Bienvenu")
                    self.root.destroy()
                    import saisiRapport
                    conn.close()


    def inscription(self):
        self.root.destroy()
        import inscription



root=Tk()
obj = Formulaire(root)
root.mainloop()