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

       

        #valider le formulaire
        btn1 = Button(frame1, text = "Comptes-rendus", font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 100, width=250)
        btn1 = Button(frame1, text = "Visiteurs", font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 150, width=250)
        btn1 = Button(frame1, text = "Praticiens",  font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 200, width=250)
        btn1 = Button(frame1, text = "Médicaments", font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 250, width=250)
    
        btn1 = Button(frame1, text = "Quitter", command=self.quit, font = ("Arial", 15, "bold"),bg = "darkblue", fg = "yellow").place(x=250, y= 300, width=250)
    
    def quit(self):
       self.root.destroy()

    

root=Tk()
obj = Formulaire(root)
root.mainloop()