from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import back
from tkinter import ttk
import mysql.connector as mysql


fen_princ = Tk()
fen_princ.title("Gestion des comptes-rendus")
fen_princ.geometry("1300x700")
zoneMenu = Frame(fen_princ, borderwidth=3)

zoneMenu.grid(row=0,column=0)

menuFichier = Menubutton(zoneMenu, text='Comptes-rendus', width='20', borderwidth=2, bg='steelblue', activebackground='#66A3D3', relief = RAISED)

menuFichier.grid(row=0,column=0)

menuEdit = Menubutton(zoneMenu, text='Visiteurs', width='20', borderwidth=2, bg='steelblue', activebackground='#66A3D3', relief = RAISED)

menuEdit.grid(row=0,column=1)

menuFormat = Menubutton(zoneMenu, text='Praticiens', width='20', borderwidth=2, bg='steelblue', activebackground='#66A3D3', relief = RAISED)

menuFormat.grid(row=0,column=2)

menuFormat = Menubutton(zoneMenu, text='Médicaments', width='20', borderwidth=2, bg='steelblue', activebackground='#66A3D3', relief = RAISED)

menuFormat.grid(row=0,column=3)

menuFormat = Menubutton(zoneMenu, text='Quitter', width='20', borderwidth=2, bg='steelblue', activebackground='#66A3D3', relief = RAISED)

menuFormat.grid(row=0,column=4)

fen_princ.mainloop()



