from calendar import TextCalendar
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
        self.root.title("Compte-rendu")
        self.root.geometry("1920x1080")

        #formualaire
        Gestion_Frame = Frame(self.root, bd=5, bg="white")
        Gestion_Frame.place(x=50, y=50, width=1500, height=700)

        Gestion_title = Label(Gestion_Frame, text="Saisie Compte-rendu", font=("Arial", 20, "bold"), bg="#0685F6", fg="white").place(x=50, y=50)
        Gestion_title = Label(Gestion_Frame, text="Compte-rendu(s) des visiteurs", font=("Arial", 20, "bold")).place(x=800, y=50)
        Gestion_title = Label(Gestion_Frame, text="Espace Manager", font=("Arial", 20, "bold")).place(x=0, y=0)

        #Variable
        self.DateRapport = StringVar()
        self.MotifVisite = StringVar()
        self.Bilan = StringVar()
        self.Prescription = StringVar()
        self.medicament = StringVar()
        self.nbrMedicament = StringVar()
        self.Pratiti = StringVar()
        self.id = StringVar()

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
        
        self.listeM = ttk.Combobox(Gestion_Frame, textvariable=self.Pratiti, font=("arial", 12), state="readonly")
        self.listeM['values'] = valuesLst
        self.listeM.place(x=220, y=150, width=250)
        self.listeM.current(0)

        idPraticien = Label(Gestion_Frame, text="Praticien", font=("Arial", 12, "bold"), bg="white", fg="#0685F6").place(x=50, y=150)
        
########
        
        idPraticien = Label(Gestion_Frame, text="Praticien", font=("Arial", 12, "bold"), bg="white", fg="#0685F6").place(x=50, y=150)
        
        idDate = Label(Gestion_Frame, text="Date", font=("arial", 12, "bold"), bg="white", fg="#0685F6")
        idDate.place(x=50, y=200)
        

        id_text = Entry(Gestion_Frame, textvariable=self.DateRapport, font=("arial", 12), bg="white")
        id_text.place(x=220, y=200)

#####
        idMotifVisite = Label(Gestion_Frame, text="Motif", font=("arial", 12, "bold"), bg="white", fg="#0685F6")
        idMotifVisite.place(x=50, y=250)

        id_text = Entry(Gestion_Frame, textvariable=self.MotifVisite, font=("arial", 12), bg="white")
        id_text.place(x=220, y=250)

#####
        # idid = Label(Gestion_Frame, text="Numéro", font=("arial", 20), bg="white", fg="#0685F6")
        # idid.place(x=50, y=400)

        id_text = Entry(Gestion_Frame, textvariable=self.id, font=("arial", 12), bg="white")
        id_text.place(x=250, y=90, width=30)

######
        idBilan = Label(Gestion_Frame, text="Bilan", font=("arial", 12, "bold"), bg="white", fg="#0685F6")
        idBilan.place(x=50, y=300)

        self.bilan_text = Text(Gestion_Frame, font=("arial", 12), bg="white")
        self.bilan_text.place(x=220, y=300,width=350, height=100)

######
        idmedicament = Label(Gestion_Frame, text="Médicament", font=("arial", 12, "bold"), bg="white", fg="#0685F6")
        idmedicament.place(x=50, y=430)

        id_text = Entry(Gestion_Frame, textvariable=self.medicament, font=("arial", 12), bg="white")
        id_text.place(x=220, y=430)

# ####
        idmedicamentNb = Label(Gestion_Frame, text="Quantitée", font=("arial", 12, "bold"), bg="white", fg="#0685F6")
        idmedicamentNb.place(x=220, y=500)

        id_text = Entry(Gestion_Frame, textvariable=self.nbrMedicament, font=("arial", 12), bg="white")
        id_text.place(x=390, y=500)


    #Button ajouter
       
        btn = Button(Gestion_Frame, text = "Modifier", cursor="hand2", command=self.modifier, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=200, y=600, width=120)
        
        btn = Button(Gestion_Frame, text = "Supprimer", cursor="hand2", command=self.supprimer, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=350, y=600, width=120)
        
        
#recherche
        

        result_Frame = Frame(Gestion_Frame, bd = 5, bg="#0685F6")
        result_Frame.place(x=600, y=110, width=850, height=300)

        #####affichage

        scroll_x = Scrollbar(result_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Frame, orient=VERTICAL)

        self.tabl_result = ttk.Treeview(result_Frame, columns= (1,2,3,4,5,6,7), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tabl_result.heading(1, text="Numéro")
        self.tabl_result.heading(2, text="Date")
        self.tabl_result.heading(3, text="Motif")
        self.tabl_result.heading(4, text="Bilan")
        self.tabl_result.heading(5, text="Médicament")
        self.tabl_result.heading(6, text="Quantitée")
        self.tabl_result.heading(7, text="Praticien")


        self.tabl_result["show"]="headings"

        self.tabl_result.column(1, width=100)
        self.tabl_result.column(2, width=100)
        self.tabl_result.column(3, width=100)
        self.tabl_result.column(4, width=200)
        self.tabl_result.column(5, width=100)
        self.tabl_result.column(6, width=100)
        self.tabl_result.column(7, width=100)


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
            if self.Pratiti.get()=="":
                messagebox.showerror("erreur", "remplir les champs", parent=self.root)
            else:
            
                conn = i.idBdd
                cursor = conn.cursor()
                cursor.execute('insert into rapport (DateRapport, MotifVisite, Bilan, medicament, idVisiteur, praticien) values(%s, %s, %s, %s, %s, %s)',
                (
                    
                    self.DateRapport.get(),
                    self.MotifVisite.get(),
                    self.bilan_text.get("1.0", END),
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
        cursor.execute('select * from rapport')
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
        self.Pratiti.set(row[6]),
        self.DateRapport.set(row[1]),
        self.MotifVisite.set(row[2]),

        self.bilan_text.delete("1.0", END),
        self.bilan_text.insert(END, row[3]),



        self.medicament.set(row[4]),
        self.nbrMedicament.set(row[5]),


    def modifier(self):

            
            conn = i.idBdd
            cursor = conn.cursor()
            cursor.execute('update rapport set DateRapport=%s, MotifVisite=%s, Bilan=%s, medicament=%s, nombre=%s, praticien=%s where idRapport=%s',  
            (
                
                self.DateRapport.get(),
                self.MotifVisite.get(),
                self.bilan_text.get("1.0", END),
                self.medicament.get(),
                self.nbrMedicament.get(),
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