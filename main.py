# Installer tkinter avec "pip3 install tkinter"

# Couleur -
# noir: #101419
# bleu: #476C9B
# rouge: #984447
"""
#789*
#456-
#123+
#0,/=
"""
from tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return
    
    global expression
    expression += str (touche)
    equation.set(expression)

def calculer():
    try:
        global expression
        total = str(eval(expression))
        
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def effacer():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    #couleur de fond
    gui.title("Calculatrice")

    #taille de la fenetre
    gui.geometry("235x385")

    # Variable pour stoker le contenu actuel
    equation = StringVar()
    
    #boite de resultats 
    resultat = Label(gui, bg="#101419", fg="#ffffff", textvariable=equation, height="2")
    resultat.grid(columnspan=4)
    
    #Boutons
    boutons = [7, 8, 9, "+", 4, 5, 6, "-", 1, 2, 3, "*", 0, "/", ".", "="]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B", fg="#ffffff", height=4, width=6)
        # Rendre le texte clicable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    b = Label(gui, text="Effacer", bg="#984447", fg="#ffffff", height=4, width=26)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4)
    print("Le script a été exécuté avec succès.")
    gui.mainloop()


    
