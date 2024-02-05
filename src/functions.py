"""
Ce fichier contient les fonctions qui seront utilisées dans le fichier main.py
"""

import logging


def calculer(expression, equation):
    """makes the calculation and updates the result label"""

    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception as e:
        logging.error(e)
        equation.set("error")
        expression = ""

    return equation, expression


def appuyer(touche, expression, equation):
    """manage the button press event and updates the expression label"""

    if touche == "=":
        calculer(expression, equation)
    else:
        expression += str(touche)
        equation.set(expression)

    return expression, equation


def effacer(expression, equation):
    """manage the clear button press event and updates the expression label"""

    expression = ""
    equation.set("")

    return expression, equation
