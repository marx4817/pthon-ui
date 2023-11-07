from tkinter import*
mainFrame = Tk()

text =""


def logout(mFrame):
    username = Label(mFrame, text="username", font=("Helvetica", 14))
    username.grid(column=0, row=0)


def mn():
    global cadre1
    a = text.get()
    cadre1.destroy()
    #text.grid_forget()
    if(a =="max"):
        
        cadre2 = Frame(mainFrame, padx=20, pady=20)
        print("all")
    
def login():
    cadre1 = Frame(mainFrame, padx=20, pady=20)
    username = Label(cadre1, text="username", font=("Helvetica", 14))
    username.grid(column=0, row=0)
    global text
    text = Entry(width=30)
    text.grid(column=4, row=0, columnspan=10)
        
    password = Label(cadre1, text="password", font=("Helvetica", 14))
    password.grid(column=0, row=1)
    
    text1 = Entry(width=30)
    text1.grid(column=1, row=1, columnspan=10)
    
    bouton = Button(cadre1, text="Afficher les valeurs", command=mn)
    bouton.grid(row=2, column=4, pady=10)
    
    return True

b = login()
largeur = 400
hauteur = 300
mainFrame.geometry(f"{largeur}x{hauteur}")

mainFrame.mainloop()



    