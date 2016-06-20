import random
import math
from copy import *
from Shark import Shark
from Zone import Zone

class Sea :
    """attributes
    - D depth
    - zones with sharks
    - some predators
    - nb of shark in the Sea
    """
    def __init__(self,D,zone_,nb_sharks_,starting_I,nb_predators_,ori_shark) : #zone_ c'est les limites de chaque zones, ori_shark c est notre requin modele de base
        self.D=D #profondeur du milieu
        self.zones={} #dico, cle bornes de la zones sous forme de tuple, objet zone
        self.nb_sharks=nb_sharks_
        ori_shark.updateBiolum()
        ori_shark.calculProfondeur()
        ori_shark.initProfondeur()
        for key in zone_:
            if(ori_shark.position>key[0] and ori_shark.position < key[1]):
                s = nb_sharks_
            else :
                s=0
            self.zones[key]=Zone(key[0],key[1],s,nb_sharks_,ori_shark)
        self.predators=nb_predators_
        self.adaptNbPred();

    def Evo_population (self,zone) : # calculate how many sharks die or give birth, idem predators
        if (zone.percent_shark>0) and (len(zone.sharks)>0):
            r0=0.47
            r=r0*math.pow(1+zone.coeff_lat_lum,2)
            K=600*zone.percent_shark #on pondere la capacite d'accueil en fonction de la profondeur et du pourcentage de requins qui s'y trouvent
            e=0.47
            alpha0=0.4
            alpha=alpha0*(1+zone.coeff_lat_lum)/(1+zone.coeff_vent_lum)
            m=2
            beta=35
            h=0.1 #pas de temps
            #Valeur initiale
            nb_Rn=len(zone.sharks)
            nb_Pn=zone.predators
            #Calcul au temps n+1
            nb_R=nb_Rn+h*(r*nb_Rn*(1-nb_Rn/K)-alpha*nb_Rn*nb_Pn/(beta+nb_Rn))
            nb_P=nb_Pn+h*nb_Pn*e*(1-m*nb_Pn/nb_Rn)
            #Difference sur un pas de temps
            diff_R=round(nb_R-nb_Rn)
            diff_P=round(nb_P-nb_Pn)
            return diff_R,diff_P
        else :
            return 0,0




    def predation(self):
        diff_P_tot=0;
        for z in self.zones.values():
            diff_R,diff_P=self.Evo_population(z)
            diff_P_tot+=diff_P

            #Population de requin
            if (diff_R<0) :#Cas ou la population diminue
                z.killSharks(int(-diff_R))
            elif (diff_R>0): #Cas ou la population augmente
                z.newSharks(int(diff_R))
        self.adaptNbShark() #met a jour le nb de requin total

        #Population de predateur
        self.predators+=+diff_P_tot
        if(self.predators<0):
            self.predators=0
        self.adaptNbPred() #met a jour le nb de predateur par zone

    def adaptNbShark(self):
        self.nb_sharks=0
        for z in self.zones.values():
             self.nb_sharks+=len(z.sharks)
        for z in self.zones.values(): #mise a jour des pourcentages de requin dans chaque classe
            z.newPercent(self.nb_sharks)

    def adaptNbPred(self):
        for z in self.zones.values() :
            z.predators=0 #remise a zero du nombre de predateurs
            for j in xrange (int(z.percent_shark*self.predators)):
                z.addPredator()


    def MoveZone(self):
        for cleZ, Z in self.zones.items():
            [zdessous,zdessus]=Z.moveShark();
            if(cleZ!=(0,199) and cleZ!=(1000,1199)):
                self.zones[(cleZ[0]-200,cleZ[1]-200)].sharks.extend(zdessous)
                self.zones[(cleZ[0]+200,cleZ[1]+200)].sharks.extend(zdessus)
            if(cleZ==(0,199)):
                self.zones[(cleZ[0]+200,cleZ[1]+200)].sharks.extend(zdessus)
            if(cleZ==(1000,1199)):	
                self.zones[(cleZ[0]-200,cleZ[1]-200)].sharks.extend(zdessous)
            

    def zone(self) : 
        for z in self.diffentesZones :
            if(self.position>=z[0] and self.position<=z[1]) :
                 self.zone= z


    def comptage(self):
        req1_ventral = []
        req1_lateral = []
        compteur_req1 = []
        for i in range (len(self.zones)):
            mean_sharks_ventral = [[0 for i in range (len(self.zones[i].sharks[j].tab_ventral))] for j in range (len(self.zones[i].sharks[j].tab_ventral[0]))]
            mean_sharks_lateral = [[0 for i in range (len(self.zones[i].sharks[j].tab_lateral))] for j in range (len(self.zones[i].sharks[j].tab_lateral[0]))]
            for j in range (len(self.zones.sharks)):
                mean_sharks_ventral += self.zones[i].sharks[j].tab_ventral
                mean_sharks_lateral += self.zones[i].sharks[j].tab_lateral
            mean_sharks_ventral /= float(len(self.zones[i].sharks))
            mean_sharks_lateral /= float(len(self.zones[i].sharks))
            compteur_req1.apppend(len(self.zones[i].sharks))
            req1_ventral.append(mean_sharks_ventral)
            req1_lateral.append(mean_sharks_lateral)














