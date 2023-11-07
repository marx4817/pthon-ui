from tkinter import*

fp=Tk()
N = Label ( fp , text="Nom")
N.pack()
chanNom = Entry ( fp )
chanNom.pack()
p = Label ( fp , text 
="Prenom")
p.pack()
chanPNom = Entry ( fp )
chanPNom.pack()
t = Label ( fp , text 
="Telephone")
t.pack()
t = Entry ( fp )
t.pack()
a = Label ( fp , text 
="Adresse")
a.pack()
a = Entry ( fp )
a.pack()
s = Label ( fp , text 
="Sexe")
s.pack()
s0 = Checkbutton (fp, text = "Feminin", variable = 'v0')
s0.pack()
s1 = Checkbutton (fp, text = "Masculin", variable = 'v1')
s1.pack()
d = Label ( fp , text 
="Date de naissance")
d.pack()
d = Entry ( fp )
d.pack()
bouton=Button(fp,text='Submit')
bouton.pack()
fp.mainloop()

# from tkinter import *
# import pickle

# def enregistrer_donnees():
#     # Récupérez les données du formulaire
#     nom = chanNom.get()
#     prenom = chanPNom.get()
#     telephone = t.get()
#     adresse = a.get()
#     sexe = "Feminin" if v0.get() else "Masculin"
#     date_naissance = d.get()

#     # Créez un dictionnaire avec les données
#     donnees = {
#         "Nom": nom,
#         "Prenom": prenom,
#         "Telephone": telephone,
#         "Adresse": adresse,
#         "Sexe": sexe,
#         "Date de naissance": date_naissance
#     }

#     # Enregistrez les données dans un fichier pickle
#     with open('donnees.pickle', 'wb') as fichier_pickle:
#         pickle.dump(donnees, fichier_pickle)
    
#     print("Données enregistrées avec succès dans le fichier 'donnees.pickle'.")

# fp = Tk()
# # ... (votre code pour les étiquettes, les champs de saisie, les boutons, etc.)

# # Ajoutez un bouton pour enregistrer les données
# bouton = Button(fp, text='Submit', command=enregistrer_donnees)
# bouton.pack()

# # Variables pour les cases à cocher
# v0 = BooleanVar()
# v1 = BooleanVar()

# # ... (la suite de votre code pour les cases à cocher, les étiquettes, les champs de saisie, etc.)

fp.mainloop()
