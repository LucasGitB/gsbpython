from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as mysql

class Etudiant:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1200x720")



        #champs du formulaire
        frame1 = Frame(self.root, bg="grey")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="créer un compte", font=("Arial", 20, "bold"), bg="grey", fg="orange").place(x=50, y=30)

        #prenom et nom

        aff_prenom = Label(frame1, text="Bilan", font=("arial", 15, "bold"), bg="grey", fg="black").place(x=50, y=100)
        self.ecri_prenom = Entry(frame1, font=("arial", 15, "bold"), bg="lightgrey")
        self.ecri_prenom.place(x=50, y=130, width=250)


        btn = Button(frame1, text = "Valider", cursor="hand2", command=self.ajout, font = ("Arial", 15, "bold"),bg = "white", fg = "#0685F6").place(x=250, y= 430, width=250)
    
    def ajout(self):
            if self.ecri_prenom.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = mysql.connect(host="localhost", user="root", password='', database='info')
                cursor = conn.cursor()
                cursor.execute('insert into rapport (bilan) values(%s)',
                (
                    self.ecri_prenom.get(),
                ))

            conn.commit()
            messagebox.showinfo('succes', "user ajouté")
            conn.close()





root=Tk()
obj = Etudiant(root)
root.mainloop()