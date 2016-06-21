import random
from scipy import misc
from copy import *
import math
import matplotlib.pyplot as plt

class Shark : 
    """ attributes :
    - depth
    - counter-illumination 
    - size
    - reproduction
    """
    
    def __init__(self, zone) :
        self.position = 900 #self.calculProfondeur() #profondeur exacte
        self.zone = zone
        self.pmute = 0.008   # muting rate, 0.8 par million d annee
        self.size=200 # len(requin), je sais pas si on en a besoin en fait 
        self.lateral_bio=0 # the intraspecific recognition one
        self.ventral_bio=0 # camouflage one
        self.tab_ventral = []
        self.tab_lateral = []
        self.pap = 0 #Definition : Proportion de photophores
        self.position_ideale = 0
        self.tab_memoire_lateral = []
        self.tab_memoire_ventral = []
        self.fit_position = 0 #Plus ce coeff est proche de 0, mieu c'est pour la survie du requin en gros il se fait pas remarquer et survi
        self.fit_reproduction = 0 #Plus ce coeff est grand, mieu c'est pour la reproduction du requin 
        self.has_rep = False # pour savoir si le requin s est deja reproduit
        #je rajoute plein d'attributs pour me faciliter la vie pour les calculs:
        self.coef_biolum_ventral = 0
        self.coef_biolum_lateral = 0
        self.cases_biolum_ventral = 0
        self.cases_biolum_lateral = 0
        


    def ventral_lateralBio(self, file_name1, file_name2):
        if "lateral" in file_name1:
            temp = file_name1
            file_name1 = file_name2
            file_name2 = temp
        j1 = misc.imread(file_name1, flatten = True)
        j2 = misc.imread(file_name2, flatten = True)
        new_im = copy(j1)
        new_im2 = copy(j2)
        images = [(j1, new_im), (j2, new_im2)]
        tableaux = []
        for im in images :
            for x in range (len(im[1])):
                for y in range (len(im[1][0])):
                    im[1][x][y] = im[0][x][y] / 255
                    if (im[0][x][y] < 42.) and (im[0][x][y] > 0.) :
                        im[1][x][y] = 0
            tableaux.append((im[0], copy(im[1])))
        for tab in tableaux:
            for x in range (len(tab[0])):
                flag = True
                for y in range (len(tab[0][0])):
                    if (tab[1][x][y] > 0) :
                        flag = False
                    if (tab[1][x][y] == 0)and(flag): 
                        tab[1][x][y] = -1
            x = len(tab[0]) - 1
            while (x > 0):
                flag = True
                y = len(tab[0][0]) - 1
                while (y > 0):
                    if (tab[1][x][y] == 0)and(flag == True): 
                        tab[1][x][y] = -1
                    if (tab[1][x][y] > 0) :
                        flag = False
                    y = y - 1
                x -= 1 
        for x in range (len(tableaux[0][0][0])):
            flag = True
            for y in range (len(tableaux[0][0])):
                if (tableaux[0][1][y][x] > 0) :
                    flag = False
                if (tableaux[0][1][y][x] == 0)and(flag): 
                    tableaux[0][1][y][x] = -1
        x = len(tableaux[1][0][0]) - 1
        while (x > 0):
            flag = True
            y = len(tableaux[1][0]) - 1
            while (y > 0):
                if (tableaux[1][1][y][x] == 0)and(flag == True): 
                    tableaux[1][1][y][x] = -1
                if (tableaux[1][1][y][x] > 0) :
                    flag = False
                y = y - 1
            x -= 1 
        tableau_ventral, tableau_lateral = tableaux[0][1], tableaux[1][1]
        cases_biolum=0
        size_temp = 0
        coef_lum = 0
        for i in range (len(tableau_lateral)):
            for j in range (len(tableau_lateral[0])):
                if tableau_lateral[i][j] > 0.1:
                  cases_biolum += 1
                if tableau_lateral[i][j] >=0:
                  size_temp +=1
                  coef_lum += tableau_lateral[i][j]
        self.size += size_temp * 2
        self.coef_biolum_lateral = coef_lum
        self.cases_biolum_lateral = cases_biolum
        self.lateral_bio = (coef_lum/cases_biolum)
        cases_biolum = 0
        size_temp = 0
        coef_lum = 0
        for i in range (len(tableau_ventral)):
            for j in range (len(tableau_ventral[0])):
                if tableau_ventral[i][j] > 0.1:
                  cases_biolum += 1
                if tableau_ventral[i][j] >=0:
                  size_temp += 1
                  coef_lum += tableau_ventral[i][j]
        self.size += size_temp
        self.coef_biolum_ventral = coef_lum
        self.cases_biolum_ventral = cases_biolum
        self.ventral_bio = (coef_lum/cases_biolum)
        self.tab_ventral = deepcopy(tableau_ventral)
        self.tab_lateral = deepcopy(tableau_lateral)
        self.tab_memoire_lateral = deepcopy(self.tab_lateral)
        self.tab_memoire_ventral = deepcopy(self.tab_ventral)
        self.updateBiolum()
        self.calculProfondeur()
        self.updateFitPosition()
        self.updateFitReproduction()


    def updateBiolum(self) : 
        self.pap = (self.cases_biolum_ventral + self.cases_biolum_lateral)/float(self.size) *100
        

    def calculProfondeur(self) : #donne la profondeur ideale en fonction de la proportion de requin recouvert par les photophores
        self.position_ideale = 500 * math.exp(-0.564*math.log(self.pap)+2.31) 

    def initProfondeur(self) : 
        self.position= self.position_ideale #donne la position initiale du requin

    def toMute (self) : #On considere que ventral independant de lateral
        #et que 50% de chance de muter l'un ou l'autre
        #on considere qu'une case peut muter que si elle est a cote d'une case 
        #biolum ou elle meme biolum
        #on considere qu'il y a 1/3 de chance que la mutation enleve de la biolum
        # et 1/3 de chance qu'elle en rajoute et 1/3 de chance qu'elle fasse rien
        if (random.random() <= self.pmute) : #il y a mutation ?
            if (random.random() <= 0.5):  # je mute quoi ?
                amuter = copy(self.tab_lateral)
                tag = 0
                nombre = random.randint(1, self.cases_biolum_lateral)
            else:
                amuter = copy(self.tab_ventral)
                tag = 1
                nombre = random.randint(1, self.cases_biolum_ventral)
            for x in range (nombre):
                modif = random.randint(-165, 165) #je mute de combien ?
                modif /= 1000.0
                if modif!=0:
                    flag = True
                    while (flag):
                        posx = random.randint(2, len(amuter)-2)
                        posy = random.randint(2, len(amuter[0])-2)
                        #on considere que les 4 coins peuvent pas muter (des -1 dans tt les cas)
                        if amuter[posx][posy] > 0:
                            flag = False
                        if amuter[posx][posy+1] > 0 or amuter[posx][posy-1] > 0 or amuter[posx+1][posy] > 0 or amuter[posx-1][posy] > 0:
                            flag = False
                    if tag:
                        a = self.tab_ventral[posx][posy] + modif
                        if a > 0 and a <= 1.0:
                            self.tab_ventral[posx][posy] += modif
                            self.coef_biolum_ventral += modif
                        elif a <= 0:
                            self.coef_biolum_ventral -= self.tab_ventral[posx][posy]
                            self.cases_biolum_ventral -= 1
                            self.tab_ventral[posx][posy] = 0.
                        self.ventral_bio = self.coef_biolum_ventral / self.cases_biolum_ventral
                    else:
                        a = self.tab_lateral[posx][posy] + modif
                        if a > 0 and a <= 1.0:
                            self.tab_lateral[posx][posy] += modif
                            self.coef_biolum_lateral += modif
                        elif a <= 0 and a != -1:
                            self.coef_biolum_lateral -= self.tab_lateral[posx][posy]
                            self.cases_biolum_lateral -= 1
                            self.tab_lateral[posx][posy] = 0.
                        self.lateral_bio = self.coef_biolum_lateral / self.cases_biolum_lateral
        self.updateBiolum()
        self.calculProfondeur()
        self.updateFitPosition()
        self.updateFitReproduction()

    def req_final(self):
        x=0
        for i in range (len(self.tab_lateral)):
            for j in range (len(self.tab_lateral[0])):
                if self.tab_lateral[i][j] < 0:
                    self.tab_lateral[i][j] = 0
                if self.tab_memoire_lateral[i][j] < 0:
                    self.tab_memoire_lateral[i][j] = 0
                self.tab_lateral[i][j] *= 255
                self.tab_memoire_lateral[i][j] *=255
                x+=(self.tab_lateral[i][j] - self.tab_memoire_lateral[i][j])
        print "difference de bioluminescence lateral = %f"%(x/255)
        plt.imshow(self.tab_memoire_lateral)
        plt.show()
        plt.imshow(self.tab_lateral)
        plt.show()
        plt.imshow(self.tab_lateral-self.tab_memoire_lateral)
        plt.show()
        x=0
        for i in range (len(self.tab_ventral)):
            for j in range (len(self.tab_ventral[0])):
                if self.tab_ventral[i][j] < 0:
                    self.tab_ventral[i][j] = 0
                if self.tab_memoire_ventral[i][j] < 0:
                    self.tab_memoire_ventral[i][j] = 0
                self.tab_ventral[i][j] *= 255
                self.tab_memoire_ventral[i][j] *=255
                x+=(self.tab_ventral[i][j] - self.tab_memoire_ventral[i][j])
        print "difference de bioluminescence ventral = %f"%(x/255)
        plt.imshow(self.tab_memoire_ventral)
        plt.show()
        plt.imshow(self.tab_ventral)
        plt.show()
        plt.imshow(self.tab_ventral-self.tab_memoire_ventral)
        plt.show()
        
    def updateFitPosition(self):
        self.fit_position = abs(self.position - self.position_ideale)

    def updateFitReproduction(self): #met a jours la fitness de reproduction mieu quand coeff lateral eleve 
        self.fit_reproduction = self.lateral_bio/self.ventral_bio

    def has_Reproduce (self) :
        self.has_rep = True
    
    def reset_Rep (self) :
        self.has_rep = False
    
    def mise_jour_attributs(self):
        self.updateFitPosition()
        self.updateFitReproduction()
        self.updateBiolum()
            
