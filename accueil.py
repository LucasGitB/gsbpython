from cgitb import grey
from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import back, title
from tkinter import ttk
import mysql.connector as mysql

class Accueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Accueil")
        self.root.geometry("1920x1080")


        #champs du accueil
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=0, y=0, width=300, height=1080)


        #valider le accueil
        btn1 = Button(frame1, text = "Comptes-rendus", command=self.rapport, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=25, y=50, width=250)
        btn1 = Button(frame1, text = "Visiteurs", font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=25, y=100, width=250)
        btn1 = Button(frame1, text = "Praticiens",  font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=25, y=150, width=250)
        btn1 = Button(frame1, text = "Médicaments", font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=25, y=200, width=250)
        btn1 = Button(frame1, text = "Quitter", command=self.quit, font = ("Arial", 15, "bold"),bg = "#0685F6", fg = "white").place(x=25, y=250, width=250)
    
    def quit(self):
       self.root.destroy()

    def rapport(self):
        self.root.destroy()
        import saisiRapport


root=Tk()
obj = Accueil(root)
root.mainloop()