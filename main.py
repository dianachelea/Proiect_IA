##########################################################################
#                                                                        #
#  Copyright:   (c) 2024-2025, Bianca Spiridon, Diana-Maria Chelea       #
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

def forward_checking(grid, cuvinte):
    #se memoreaza multimea curenta de valori permise
    domenii = update(grid, cuvinte)
    #daca nu mai ramane nici un cuvant s-a incheiat algoritmul
    if not cuvinte:
        return True  
    
    #euristica pentru ordonarea variabilelor in ordine crescatoare pentru a accelera cautarea 
    cuvant_curent = cea_mai_constransa_variabila(domenii)
    #daca nu sunt pozitii disponibile va trebui sa stearga si sa se intoarca 
    if not domenii[cuvant_curent]:
        return False  

    for coordonata in domenii[cuvant_curent]:
        temp = []
        if coordonata.directie == "O":
            for litera in range(len(cuvant_curent)):
                #se salveaza un temp in cazul in care cuvantul va duce la imposibilitati si se va relua pozitia initiala
                temp.append(grid[coordonata.linie][coordonata.coloana + litera])  
                grid[coordonata.linie][coordonata.coloana + litera] = cuvant_curent[litera] 
            for r in grid:
                print(" ",r)
            cuvinte_ramase = []
            for cuvant in cuvinte:
                if cuvant != cuvant_curent:
                    cuvinte_ramase.append(cuvant)
            #recursivitate cu noua lista de cuvinte disponibila
            if forward_checking(grid, cuvinte_ramase):
                return True
            #se sterge in cazul in care nu ajungem la solutii
            for litera in range(len(cuvant_curent)):
                grid[coordonata.linie][coordonata.coloana + litera] = temp[litera]            
            for r in grid:
                print(" ", r)
        elif coordonata.directie == "V":
            for litera in range(len(cuvant_curent)):
                temp.append(grid[coordonata.linie + litera][coordonata.coloana])
                grid[coordonata.linie + litera][coordonata.coloana] = cuvant_curent[litera]            
            for r in grid:
                print(" ", r)
            cuvinte_ramase = []
            for cuvant in cuvinte:
                if cuvant != cuvant_curent:
                    cuvinte_ramase.append(cuvant)
            if forward_checking(grid, cuvinte_ramase):
                return True
            for litera in range(len(cuvant_curent)):
                grid[coordonata.linie + litera][coordonata.coloana] = temp[litera]            
            for r in grid:
                print(" ",r)

    return False

def display_result(grid):
    root = tk.Tk()
    root.title("Integrama")

    for i, row in enumerate(grid):
        for j, celula in enumerate(row):
            if celula == "#":
                label = tk.Label(root, text=" ", width=2, height=1, bg="black", relief="solid")
            else:
                label = tk.Label(root, text=celula, width=2, height=1, borderwidth=1, relief="solid", font=("Arial", 14))
            label.grid(row=i, column=j)

    root.mainloop()   

if __name__ == "__main__":
    grid=[]
    cuvinte=[]
    with open("grid_exemplu1.txt", "r") as file:
        for i in file:
            grid.append(list(i.strip().split()))
    
    with open("cuvinte_exemplu1.txt", "r") as file:
        for i in file:
            cuvinte.append(i.strip())

    if forward_checking(grid, cuvinte):
        display_result(grid)
    else:
        print("Nu s-a gasit nici o solutie.")