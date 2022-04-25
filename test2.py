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
        print(idUser)
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
        self.Pratiti = StringVar()
        self.id = StringVar()



        #Id Pratitient
        # idPratitient = tk.Label(root, text = "veuillez")
        # idPratitient.pack()
        # listePraticient = ["uedh", "uerfyu", "uiefh"]
        # liste = ttk.Combobox(root, values = listePraticient)
        # liste.current(0)
        # liste.pack()

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
        # liste['values'] = valuesLst
        # liste.current(0)
        # liste.pack()
        # liste.place(x=220, y=150)
        self.listeM = ttk.Combobox(Gestion_Frame, textvariable=self.Pratiti, font=("arial", 20), state="readonly")
        self.listeM['values'] = valuesLst
        self.listeM.place(x=220, y=150, width=250)
        self.listeM.current(0)

        idPratitient = Label(Gestion_Frame, text="Pratitien", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=150)
        




########
        
        idPratitient = Label(Gestion_Frame, text="Pratitien", font=("Arial", 20, "bold"), bg="white", fg="#0685F6").place(x=50, y=150)
        
        idDate = Label(Gestion_Frame, text="Date", font=("arial", 20), bg="cyan")
        idDate.place(x=50, y=200)
        

        id_text = Entry(Gestion_Frame, textvariable=self.DateRapport, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=200)

#####
        idMotifVisite = Label(Gestion_Frame, text="Motif", font=("arial", 20), bg="cyan")
        idMotifVisite.place(x=50, y=300)

        id_text = Entry(Gestion_Frame, textvariable=self.MotifVisite, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=300)

#####
        idid = Label(Gestion_Frame, text="Numéro", font=("arial", 20), bg="cyan")
        idid.place(x=50, y=400)

        id_text = Entry(Gestion_Frame, textvariable=self.id, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=400)

######
        idBilan = Label(Gestion_Frame, text="Bilan", font=("arial", 20), bg="cyan")
        idBilan.place(x=50, y=450)

        id_text = Entry(Gestion_Frame, textvariable=self.Bilan, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=450)

######
        idmedicament = Label(Gestion_Frame, text="Medicament", font=("arial", 20), bg="cyan")
        idmedicament.place(x=50, y=600)

        id_text = Entry(Gestion_Frame, textvariable=self.medicament, font=("arial", 20), bg="cyan")
        id_text.place(x=220, y=600)

# ####


    #Button ajouter
        btn = Button(Gestion_Frame, text = "Valider", cursor="hand2", command=self.creer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=600, y=600, width=120)
        
        btn = Button(Gestion_Frame, text = "Modififier", cursor="hand2", command=self.modifier, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=750, y=600, width=120)
        btn = Button(Gestion_Frame, text = "Supprimer", cursor="hand2", command=self.supprimer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=880, y=600, width=120)
        
        

        self.tabl_result = ttk.Treeview(root, columns= (1,2,3,4,5,6), height=8, show = "headings")

        self.tabl_result.heading(1, text="Numéro")
        self.tabl_result.heading(2, text="Date")
        self.tabl_result.heading(3, text="Motif")
        self.tabl_result.heading(4, text="Bilan")
        self.tabl_result.heading(5, text="Médicament")
        self.tabl_result.heading(6, text="praticien")


        self.tabl_result["show"]="headings"

        self.tabl_result.column(1, width=100)
        self.tabl_result.column(2, width=100)
        self.tabl_result.column(3, width=100)
        self.tabl_result.column(4, width=100)
        self.tabl_result.column(5, width=100)
        self.tabl_result.column(6, width=100)


        self.tabl_result.pack()

        self.tabl_result.bind("<ButtonRelease-1>", self.information)

        self.afficherActuRapport()





        # tree = ttk.Treeview(root, columns= (1,2,3,4,5), height=5, show = "headings")
        # tree.place(x=650, y = 170, width=800, height=175)

        # tree.heading(1, text= "Date")
        # tree.heading(2, text= "Motif")
        # tree.heading(3, text= "Bilan")
        # tree.heading(4, text= "Medicament")
        # tree.heading(5, text= "IdVisiteur")

        # tree.column(1, width=50)
        # tree.column(2, width=50)
        # tree.column(3, width=100)
        # tree.column(4, width=100)
        # tree.column(5, width=50)

        # tree.bind(self.information)







        # conn = i.idBdd
        # cursor = conn.cursor()
        # idVisiteur = idUser
        # cursor.execute('select * from rapport where idVisiteur = {}'.format(idUser))

        
        # rapportlist = cursor.fetchall()



        # for rapport in rapportlist:
        #     self.tabl_result.insert('', END, values= rapport)

        # conn.commit()
     
 


      
    def creer(self):
            if self.Bilan.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('insert into rapport (DateRapport, MotifVisite, Bilan, medicament, idVisiteur, praticien) values(%s, %s, %s, %s, %s, %s)',
                (
                    
                    self.DateRapport.get(),
                    self.MotifVisite.get(),
                    self.Bilan.get(),
                    self.medicament.get(),
                    self.user,
                    self.Pratiti.get(),
                ))
            idUser = self.user
            conn.commit()
            self.afficherActuRapport()
            messagebox.showinfo('succes', "Rapport ajouté !")
            conn.close()


    # def afficherActuRapport(self):
    #     conn = i.idBdd
    #     cursor = conn.cursor()
    #     idUser = self.user
    #     idVisiteur = idUser
    #     cursor.execute('select * from rapport where idVisiteur = {}'.format(idUser))
    #     rapportlist = cursor.fetchall()
    #     for rapport in rapportlist:
    #         self.tabl_result.insert('', END, values= rapport)

    #     conn.commit()


    def afficherActuRapport(self):
        conn = i.idBdd
        cursor = conn.cursor()
        idUser = self.user
        idVisiteur = idUser
        cursor.execute('select * from rapport where idVisiteur = {}'.format(idUser))
        rapportlist = cursor.fetchall()
        if len(rapportlist) != 0:
            self.tabl_result.delete(*self.tabl_result.get_children())
            for rapport in rapportlist:
                self.tabl_result.insert('', END, values= rapport)

        conn.commit()

    def information(self, ev):
        cursors_row = self.tabl_result.focus()
        contents = self.tabl_result.item(cursors_row)
        row = contents["values"]
        self.id.set(row[0]),
        self.Pratiti.set(row[5]),
        self.DateRapport.set(row[1]),
        self.MotifVisite.set(row[2]),
        self.Bilan.set(row[3]),
        self.medicament.set(row[4]),


    def modifier(self):

            
            conn = i.idBdd
            cursor = conn.cursor()
            cursor.execute('update rapport set DateRapport=%s, MotifVisite=%s, Bilan=%s, medicament=%s, praticien=%s where idRapport=%s',  
            (
                
                self.DateRapport.get(),
                self.MotifVisite.get(),
                self.Bilan.get(),
                self.medicament.get(),
                self.Pratiti.get(),
                self.id.get()
            ))
            
            conn.commit()
            self.afficherActuRapport()
            messagebox.showinfo('succes', "Modif ajouté !")
            conn.close()

    def supprimer(self):

            
            conn = i.idBdd
            cursor = conn.cursor()
            cursor.execute('delete from rapport where idRapport={}'.format(self.id.get())) 
  
            conn.commit()
            self.afficherActuRapport()
            messagebox.showinfo('succes', "supprimé ajouté !")
            conn.close()
        

        
        
                

def affichage(user):
    root=Tk()
    ojb = Rapport(root, user)
    root.mainloop()
