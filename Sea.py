import random
import math

from Shark import Shark
from Zone import Zone
from Predator import Predator

class Sea :
	"""attributes 
	- D depth
	- zones with sharks 
	- some predators
	- nb of shark in the Sea
	"""
	def __init__(self,D,zone_,nb_sharks_,starting_I,nb_predators) : #zone_ c'est les limites de chaque zones
		self.D=D #profondeur du milieu
		self.zones={} #dico, cle bornes de la zones sous forme de tuple, objet zone
		self.nb_sharks=nb_sharks_
		for i in xrange (len(zone_)) :
			if (zone_[i] == starting_I) : #On initialise en ne mettant des requins que dans la premiere zone
				s = nb_sharks_
			else :
				s=0
			self.zones[zone_[i]]=Zone(zone_[i][0],zone_[i][1],s,nb_sharks_)
		self.predators=[]
		for i in xrange (nb_predators) :
				position=random.uniform(zone_[0][0], zone_[len(zone_)-1][1])
				self.predators.append(Predator(int(position))) #correspond a un endroit random
				for i in xrange (len(zone_)) : #on ajoute les predateurs dans les zones en fonction de la position
					if (int(position)>=zone_[i][0] and int(position)<=zone_[i][1]):
							self.zones[zone_[i]].addPredator()
							break;




	def Evo_population (self,zone) : # calculate how many sharks die or give birth, idem predators
		if (zone.percent_shark>0):
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
			print (diff_R,diff_P)
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
					z.killSharks(diff_R)
			elif (diff_R>0): #Cas ou la population augmente
					z.newSharks(diff_R)
		self.adaptNbShark() #met a jour le nb de requin total 

		#Population de predateurs
		if (diff_P_tot<0): #La population global de predateur diminue
			if (len(self.predators)+diff_P_tot>0): #il y a plus de predateurs que de predateurs a tuer
				pred_candidate=random.choice(self.predators)
				self.predators.remove(pred_candidate)
				for z in self.zones.keys():
						if (pred_candidate.position<z[1] and pred_candidate.position>z[0]):
							self.zones[z].killPredator()
			else: # il y a moins de predateurs que de predateurs a tuer : on les tue tous
				self.predators=[]
				for z in self.zones.keys():
						while (self.zones[z].predators>0):
							self.zones[z].killPredator()
		elif (diff_P_tot>0): #La population global de predateur augmente
			for i in range(int(diff_P_tot)):
				position=int(random.uniform(min(self.zones.keys())[0],max(self.zones.keys())[1])) 
				self.predators.append(Predator(position)) 
				for z in self.zones.keys():
					if (position<z[1] and position>z[0]):
						self.zones[z].addPredator()				
			
      
      
      
	def adaptNbShark(self):
		self.nb_sharks=0
		for z in self.zones.values():
			 self.nb_sharks+=len(z.sharks)
		for z in self.zones.values(): #mise a jour des pourcentages de requin dans chaque classe
			 z.newPercent(self.nb_sharks)




	def zone(self) : 
		for z in self.diffentesZones :
			if(self.position>=z[0] and self.position<=z[1]) : 
 				self.zone= z
