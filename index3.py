from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import back
from tkinter import ttk
import mysql.connector as mysql


def update():
    nom = e_nom.get()

    if(nom==""):
        messagebox.showinfo('Insertion', "formulaire incomplet")
    else:
        conn = mysql.connect(host="localhost", user="root", password='', database='info')
        cursor = conn.cursor()
    
  
        
        cursor.execute("update user set nom = %s where id =%s", (

        e_nom.get(),
        1
        ))
        conn.commit()
        messagebox.showinfo('succes', "modif ajouter")
        conn.close()


def insert():
    nom = e_nom.get()

    if(nom==""):
        messagebox.showinfo('Insertion', "formulaire incomplet")
    else:
        conn = mysql.connect(host="localhost", user="root", password='', database='info')
        cursor = conn.cursor()
   

        #req = 'insert into user(nom) values(nom)'
        query = "insert into user (nom) values (%s)"
        data = (nom, )
        # val = (cursor.lastrowid, nomxx)
        cursor.execute(query, data)
        conn.commit()
        
        messagebox.showinfo('succes', "Patient ajouté")
        conn.close()


root = Tk()
root.title("Gestion des patient ")
root.geometry("1300x700")

nom = Label(root, text = "Praticien", font = ("Arial", 16), bg = "white", fg="#0685F6")
nom.place(x=0,y=30,width=200)

date = Label(root, text = "Date Rapport", font = ("Arial", 16), bg = "white", fg="#0685F6")
date.place(x=0,y=70,width=200)

motif = Label(root, text = "Motif visite", font = ("Arial", 16), bg = "white", fg="#0685F6")
motif.place(x=0,y=110,width=200)

bilan = Label(root, text = "Bilan", font = ("Arial", 16), bg = "white", fg="#0685F6")
bilan.place(x=0,y=150,width=200)

e_nom = Entry()
e_nom.place(x=200,y=30,width=200,height=30)

e_date = Entry()
e_date.place(x=200,y=70,width=200,height=30)

e_motif = Entry()
e_motif.place(x=200,y=110,width=200,height=30)

e_bilan = Text()
e_bilan.pack()
e_bilan.place(x=200,y=150,width=200,height=70)


insert = Button(root, text = "Enregistrer", font = ("San Francisco", 16),bg = "darkblue", fg = "yellow", command = insert)
insert.place(x=20, y= 320, width=200)

update = Button(root, text = "modif", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = update)
update.place(x=250, y= 320, width=200)


#Table
table = ttk.Treeview(root, columns = (1, 2), height = 5, show = "headings")
table.place(x = 500,y = 30, width = 400, height = 200)

#Entete
table.heading(1 , text = "Médicaments")
table.heading(2 , text = "Quantité")


#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)


root.mainloop()



