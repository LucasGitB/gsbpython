from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import font
from turtle import bgcolor, heading, width
import mysql.connector as mysql

import sys
sys.path.append("connect")
import connect as i

class Rapport:
    def __init__(self, root, idUser):
        print(idUser)
        self.affiche()
        self.root = root
        self.user = idUser
        self.root.title("Formulaire")
        self.root.geometry("1920x1080")

      #recherche
        Details_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Details_Frame.place(x=700, y=150, width=1100, height=700)

        


        #affichage 

        result_Frame = Frame(Details_Frame, bd = 5, bg="cyan")
        result_Frame.place(x=10, y=110, width=1070, height=570)

        scroll_x = Scrollbar(result_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Frame, orient=VERTICAL)
        self.tabl_result = ttk.Treeview(result_Frame, columns=("a", "a", "a", "a", "a"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tabl_result.heading("a", text="a")
        self.tabl_result.heading("a", text="a")
        self.tabl_result.heading("a", text="a")
        self.tabl_result.heading("a", text="a")
        self.tabl_result.heading("a", text="a")

        self.tabl_result["show"]="headings"

        self.tabl_result.column("a", width=100)
        self.tabl_result.column("a", width=100)
        self.tabl_result.column("a", width=100)
        self.tabl_result.column("a", width=100)
        self.tabl_result.column("a", width=100)

        self.tabl_result.pack()

        self.tabl_result.bind("<ButtonRelease-1")

        


    def affiche(self):
            conn = i.idBdd
            cursor = conn.cursor()
            cursor.execute('select * from rapport')
            rows = cursor.fetchall()
            if len(rows)!= 0:
                self.tabl_resul.delete(*self.tabl_result.get_children())
                for row in rows:
                    self.tabl_result.insert("", END, values=row)
            conn.commit()
            conn.close()


                

def affichage(user):
    root=Tk()
    ojb = Rapport(root, user)
    root.mainloop()
