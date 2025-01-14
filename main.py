##########################################################################
#                                                                        #
#  Copyright:   (c) 2024-2025, Bianca Spiridon, Diana-Maria Chelea   #
#  E-mail:      bianca.spiridon@student.tuiasi.ro                        #
#               diana-maria.chelea@student.tuiasi.ro                     #
#  Description: Rezolvarea integramelor folosind algoritmul              #
#               Forward Checking                                         #
#                                                                        #
#  This code and information is provided "as is" without warranty of     #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################



import tkinter as tk

#coordonata pentru pozitie (orizontal/vertical , plasare pe harta(linie,coloana))
class Coordonata:
    def __init__(self, directie, linie, coloana):
        self.directie = directie
        self.linie = linie
        self.coloana = coloana

    def __repr__(self):
        return f"({self.directie}, {self.linie}, {self.coloana})"
   

# alegere variabila cu cele mai putine valori permise
def cea_mai_constransa_variabila(domenii):
    #numarul de valori permise pentru variabila, consistente cu solutia partiala
    lungime_minima = float('inf')
    for variabila in domenii:
        contor = len(domenii[variabila])
        if contor < lungime_minima:
            cmcv = variabila
            lungime_minima = contor
    #returneaza variabila cu numarul minim de valori posibile ramase
    return cmcv


def update(grid, cuvinte):
    # initializam pozitiile pe care le poate lua fiecare cuvant
    domeniu = {}
    for cuvant in cuvinte:
        pozitii = []
        #verificam atat pe verticala cat si pe orizontala locurile disponibile
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j + len(cuvant) <= len(grid[i]):  
                    pozitie_libera = True
                    for litera in range(len(cuvant)):
                        #daca o litera este deja ocupata si e diferita de litera cuvantului curent-> pozitie indisponibila
                        if grid[i][j + litera] != '0' and grid[i][j + litera] != cuvant[litera]:
                            pozitie_libera = False
                            break
                    if pozitie_libera:
                        pozitii.append(Coordonata("O", i, j))

                if i + len(cuvant) <= len(grid):  
                    pozitie_libera = True
                    for litera in range(len(cuvant)):
                        if grid[i + litera][j] != '0' and grid[i + litera][j] != cuvant[litera]:
                            pozitie_libera = False
                            break
                    if pozitie_libera:
                        pozitii.append(Coordonata("V", i, j))

        domeniu[cuvant] = pozitii
        #print(cuvant)
        #print(pozitii)
    return domeniu