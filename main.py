"""
Main file for the calculator
"""

import logging
from tkinter import *

from src.functions import *
from src.vars import *


def main():
    """ """

    gui = Tk()

    # couleur de fond
    gui.title("Calculatrice")

    # taille de la fenetre
    gui.geometry(geometry)

    # Variable pour stoker le contenu actuel
    equation = StringVar()

    # boite de resultats
    resultat = Label(gui, bg=noir, fg=white, textvariable=equation, height="2")
    resultat.grid(columnspan=4)

    # Boutons

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg=bleu, fg=white, height=4, width=6)

        # Rendre le texte clicable
        b.bind(
            "<Button-1>",
            lambda e, bouton=bouton: appuyer(bouton, expression, equation),
        )

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    b = Label(gui, text="Effacer", bg=rouge, fg=white, height=4, width=26)
    b.bind(
        "<Button-1>",
        lambda e: effacer(expression, equation),
    )
    b.grid(columnspan=4)
    logging.warning("Le script a été exécuté avec succès")
    gui.mainloop()


if __name__ == "__main__":
    main()
