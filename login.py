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



class Connexion:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")
        self.root.geometry("1920x1080+0+0")


        #champs du connexion
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

        #valider la connexion
        btn = Button(frame1, text = "Connexion", cursor="hand2", command=self.connexion, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=200, y=430, width=120)
        btn = Button(frame1, text = "Inscription", cursor="hand2", command=self.inscription, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=350, y=430 , width=120)
    
    # def checkrole(num):
    #     switch={
    #         1: 1,
    #         2:2
    #     }
    #     return switch.get(num,"Invalid input")


        # conn = i.idBdd
        # cursor = conn.cursor()
        # cursor.execute('select * from rapport')
        # rapportlist = cursor.fetchall()

        # for rapport in rapportlist:
        #     print('Bilan : {}'.format(rapport[3]))
            
        # conn.commit()
        # conn.close()

    def connexion(self):
            if self.ecri_email.get()=="" or self.ecri_mdp.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('select * from utilisateur where Mail=%s and Password=MD5(%s)',
                (
                    self.ecri_email.get(),
                    self.ecri_mdp.get()
                ))
                row=cursor.fetchone()

                if row == None:
                    messagebox.showerror("Erreur", "Identifiants incorrects", parent=self.root)
                    
                else:
                    messagebox.showinfo("Connecté", "Bienvenue !")
                    self.root.destroy()
                    if row[5] == 1:
                        # import accueil
                        # accueil.affichage(row[0])
                        import VisiteurRapport
                        VisiteurRapport.affichage(row[0])

            
                    elif row[5] == 2:
                        import ManagerRapport
                        ManagerRapport.affichage(row[0])
                        
                    conn.close()



    def inscription(self):
        self.root.destroy()
        import inscription

    


root=Tk()
obj = Connexion(root)
root.mainloop()