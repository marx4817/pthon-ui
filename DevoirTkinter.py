import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo

text = ""
text1 = ""
cadreInfo = 0
cadreAff = 0

def supprimer_cadre():
    global cadre3
    user = text.get()
    password = text1.get()
    
    if(password =="admin" and user=="admin"):
        cadre.destroy()  # Supprimez le cadre
        cadre2 = mainFrame()
        cadre3 = formInfo()
    else:
        record = "username or Password is incorrect"
        showinfo(title='Information', message=''.join(record))
        
def affi():
    global cadreAff
    cadre3.destroy()
    if cadreInfo:
        cadreInfo.destroy()
    if cadreAff:
        cadreAff.destroy()
    cadreAff = afficherInfo()

def entr():
    global cadreInfo
    cadreAff.destroy()
    if cadreInfo:
        cadreInfo.destroy()
    cadreInfo = formInfo()

# Créez une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Supprimer un cadre")
largeur = 400
hauteur = 300
fenetre.geometry(f"{largeur}x{hauteur}")

# Créez un cadre à l'intérieur de la fenêtre principale
def login():
    global text
    global text1
    
    cadre = tk.Frame(fenetre, padx=20, pady=20)
    cadre.grid()

    # Ajoutez des widgets au cadre
    username = tk.Label(cadre, text="username", font=("Helvetica", 14))
    username.grid(row=0, column=0, padx=10)
    text = tk.Entry(cadre, width=30)
    text.grid(row=0, column=1, padx=10)
    
    password = tk.Label(cadre, text="password", font=("Helvetica", 14))
    password.grid(column=0, row=1)
    
    text1 = tk.Entry(cadre, width=30)
    text1.grid(column=1, row=1, columnspan=10)
    
    
    bouton_supprimer = tk.Button(cadre, text="login", command=supprimer_cadre)
    bouton_supprimer.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    return cadre

def saveInfo(data):
    connexion = sqlite3.connect('devoir_tkinter.db')
    
    # Créez un curseur
    curseur = connexion.cursor()

    # Créez une table avec une structure de base
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            lName TEXT,
            phone TEXT,
            address TEXT,
            sexe TEXT,
            year TEXT
        )
    ''')
    
    # Insérez des données dans la table
    curseur.execute("INSERT INTO utilisateurs (name, lName, phone, address, sexe, year)VALUES (?, ?,?, ?,?, ?)",data)

    # Confirmez les modifications dans la base de données
    connexion.commit()
    connexion.close()

def getInfoForm():
    name = first_name_entry.get()
    lName = last_name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    sexe = sexe_entry.get()
    year = year_entry.get()
    
    data = (name,lName, phone, address, sexe, year)
    print(data)
    saveInfo(data)

def formInfo():
    cadre = tk.Frame(fenetre, padx=10, pady=10)
    cadre.grid()
    
    global first_name_entry
    global last_name_entry
    global phone_entry
    global address_entry
    global sexe_entry
    global year_entry

    # Ajoutez des widgets au cadre
    first_name = tk.Label(cadre, text="Enter your first name", font=("Helvetica", 12))
    first_name.grid(row=0, column=0, padx=10)
    first_name_entry = tk.Entry(cadre, width=30)
    first_name_entry.grid(row=0, column=1, padx=10)
    
    last_name = tk.Label(cadre, text="Enter your last name", font=("Helvetica", 12))
    last_name.grid(row=1, column=0, padx=10)
    last_name_entry = tk.Entry(cadre, width=30)
    last_name_entry.grid(row=1, column=1, padx=10)
    
    phone = tk.Label(cadre, text="Enter your phone num", font=("Helvetica", 12))
    phone.grid(row=2, column=0, padx=10)
    phone_entry = tk.Entry(cadre, width=30)
    phone_entry.grid(row=2, column=1, padx=10)
    
    address = tk.Label(cadre, text="Enter your address", font=("Helvetica", 12))
    address.grid(row=3, column=0, padx=10)
    address_entry = tk.Entry(cadre, width=30)
    address_entry.grid(row=3, column=1, padx=10)
    
    sexe = tk.Label(cadre, text="Enter your Sexe", font=("Helvetica", 12))
    sexe.grid(row=4, column=0, padx=10)
    sexe_entry = tk.Entry(cadre, width=30)
    sexe_entry.grid(row=4, column=1, padx=10)
    
    annees = [str(annee) for annee in range(1995, 2003)]
    
    year = tk.Label(cadre, text="Choice year Of B", font=("Helvetica", 12))
    year.grid(row=5, column=0, padx=10)
    year_entry = ttk.Combobox(cadre, values=annees, width=27)
    year_entry.grid(row=5, column=1, padx=10)
    
    bouton_afficher = tk.Button(cadre, text="Submit Informations", command=getInfoForm)
    bouton_afficher.grid(row=6, columnspan=2, padx=10, pady=10)
    
    return cadre

def table(cadre):
    columns = ('id','first_name', 'last_name', 'phone', 'address', 'sexe', 'year')

    tree = ttk.Treeview(cadre, columns=columns, show='headings')

    # define headings
    tree.heading('id', text='ID')
    tree.heading('first_name', text='First Name')
    tree.heading('last_name', text='Last Name')
    tree.heading('phone', text='Phone')
    tree.heading('address', text='Address')
    tree.heading('sexe', text='Sex')
    tree.heading('year', text='Year')
    
    
    return tree

def afficherInfo():
    connexion = sqlite3.connect('devoir_tkinter.db')
    # Créez un curseur
    curseur = connexion.cursor()
    cadre = tk.Frame(fenetre, padx=10, pady=10)
    cadre.grid()
    tab = table(cadre)
    
    # Récupérez des données
    curseur.execute("SELECT * FROM utilisateurs")
    donnees = curseur.fetchall()
    connexion.close()
    contacts= []
    for n in donnees:
        contacts.append(n)

    # add data to the treeview
    for contact in contacts:
        tab.insert('', tk.END, values=contact)
    tab.grid(row=0, column=0, sticky='nsew')
        
    return cadre

def mainFrame():
    cadre = tk.Frame(fenetre, padx=10, pady=10)
    cadre.grid()
    
    bouton_ajouter = tk.Button(cadre, text="Ajouter Information", command=entr)
    bouton_ajouter.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
    bouton_afficher = tk.Button(cadre, text="Afficher les Information", command=affi)
    bouton_afficher.grid(row=0, column=4, columnspan=2, padx=10, pady=10)
    
    return cadre
    
cadre = login()

# Exécutez la boucle principale de tkinter
fenetre.mainloop()
