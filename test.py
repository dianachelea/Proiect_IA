
import unittest
from main import *

class TestIntegrama(unittest.TestCase):
    def test1_cea_mai_constransa_variabila(self):
        domenii = {
            "cuvant1": [('O', 0, 0), ('V', 1, 0)],
            "cuvant2": [('V', 0, 1)],
            "cuvant3": [('O', 2, 2), ('O', 3, 3), ('V', 4, 4)]
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, "cuvant2")
    def test2_cea_mai_constransa_variabila_trei_valori(self):
        domenii = {
            "cuvant1": [('O', 0, 0), ('V', 1, 0), ('O', 2, 2)],
            "cuvant2": [('V', 0, 1),('V', 1, 0), ('O', 2, 2)],
            "cuvant3": [('O', 2, 2), ('V', 4, 4),('O', 2, 2)]
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, "cuvant1")
    def test3_cea_mai_constransa_variabila_trei_valori(self):
        domenii = {
            "cuvant1": [],
            "cuvant2": [],
            "cuvant3": []
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, "cuvant1")
    def test1_update_un_singur_cuvant(self):
        grid = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        cuvinte = ["cat"]
        rezultat = update(grid, cuvinte)
        self.assertEqual(len(rezultat["cat"]), 6)
    def test2_update_mai_multe_cuvinte(self):
        grid = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        cuvinte = ["cat", "bat"]
        rezultat = update(grid, cuvinte)
        self.assertEqual(len(rezultat["cat"]), 6)
        self.assertEqual(len(rezultat["bat"]), 6)
    def test3_update_cuvant_in_grid(self):
        grid = [
            ['c', '0', '0'],
            ['a', '0', '0'],
            ['t', '0', '0']
        ]
        cuvinte = ["cat", "bat"]
        rezultat = update(grid, cuvinte)
        self.assertEqual(len(rezultat["cat"]), 4)  
        self.assertEqual(len(rezultat["bat"]), 2)    

    def test4_update_spatiu_insuficient(self):
        grid = [
            ['#', '0', '#'],
            ['#', '0', '#'],
            ['#', '#', '0']
        ]
        cuvinte = ["cat", "bat", "dog"]
        rezultat = update(grid, cuvinte)
        self.assertEqual(len(rezultat["cat"]), 0)
        self.assertEqual(len(rezultat["bat"]), 0)
        self.assertEqual(len(rezultat["dog"]), 0)
    def test5_update_doar_un_cuvant(self):
        grid = [
            ['b', '0', '#'],
            ['a', '0', '#'],
            ['t', '#', '0']
        ]
        cuvinte = ["cat", "bat", "dog"]
        rezultat = update(grid, cuvinte)
        self.assertEqual(len(rezultat["cat"]), 0)
        self.assertEqual(len(rezultat["bat"]), 1)
        self.assertEqual(len(rezultat["dog"]), 0)  
    

    
    #daca o variabila nu are nicio pozitie valida in vectorul de pozitii, va fi returnata de functie, dar apoi va fi invalidata de functia forward_checking
    def test4_cea_mai_constransa_variabila_nicio_pozitie(self):
        domenii = {
            "cuvant1": [('O', 0, 0)],
            "cuvant2": [],
            "cuvant3": [('V', 1, 2)]
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, "cuvant2")

    def test5_cea_mai_constransa_variabila_mai_multe_variante_egale(self):
        #ar trebui sa returneze cuvant5
        domenii = {
            "cuvant1": [('O', 0, 0), ('V', 0, 1)],
            "cuvant2": [('O', 1, 0), ('V', 1, 1)],
            "cuvant3": [('V', 2, 0), ('O', 2, 1)],
            "cuvant4": [('O', 3, 0), ('V', 3, 1)],
            "cuvant5": [('V', 4, 0)],
            "cuvant6": [('O', 5, 0), ('V', 5, 1)],
            "cuvant7": [('V', 6, 0), ('O', 6, 1)],
            "cuvant8": [('O', 7, 0), ('V', 7, 1)],
            "cuvant9": [('V', 8, 0)],
            "cuvant10": [('O', 9, 0), ('V', 9, 1)]
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, "cuvant9")

    def test6_cea_mai_constransa_variabila_domeniu_nul(self):
        #returneaza 0
        domenii = {
        }
        rezultat = cea_mai_constransa_variabila(domenii)
        self.assertEqual(rezultat, 0)

    def test1_forward_checking_cuvant_care_depaseste_grid(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0'],
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0']
        ]
        cuvinte = ["OCEAN", "STAR", "TARS", "TART"]
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, True)
        
    def test2_forward_checking_grid_completat_corect(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0'],
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0']
        ]
        cuvinte = ["RATA", "STAR", "TARS", "TART"]
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, True)

    def test3_forward_checking_grid_invalid(self):
        grid = [
            ['#', '#', '#', '#'],
            ['#', '#', '#', '#'],
            ['#', '#', '#', '#'],
            ['#', '#', '#', '#']
        ]
        cuvinte = ["ANA"]
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, False)

    def test4_forward_checking_cuvinte_null(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0'],
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0']
        ]
        cuvinte = []
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, False)        

    def test5_forward_checking_grid_precompletat(self):
        #obligatoriu doar uppercase sau lowercase
        grid = [
            ['R', 'A', 'T', 'A'],
            ['0', '#', '#', '0'],
            ['0', '0', '0', '0'],
            ['0', '#', '#', '0']
        ]
        cuvinte = ["rars", "arsa", "rocs"]
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, False)   

    def test6_forward_checking_grid_incomplet(self):
        grid = [
            ['0', '0', '0', '0', '0'],
            ['0', '#', '#', '#', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '#', '#', '#', '0'],
            ['0', '0', '0', '0', '0']
        ]
        cuvinte = ["PAS", "STAR", "COS"]
        rezultat = forward_checking(grid, cuvinte)
        self.assertEqual(rezultat, True)
         

if __name__ == "__main__":
    unittest.main()
