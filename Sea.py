import random
from Shark import Shark
from Zone import Zone
from Predator import Predator

class Sea :
	"""attributes 
	- D depth
	- each zone H*W 
	- some sharks
	- some predators
	"""

	def __init__(self,D,zones,nb_sharks,starting_I,nb_predators) : #zones c'est les limites de chaque zones


		self.D=D #profondeur du milieu
		
		self.zones={} #dico, cle bornes de la zones sous forme de tuple, objet zone
		
		for i in xrange (len(zones)) :
			if (zones[i] == starting_I) : #On initialise en ne mettant des requins que dans la premiere zone
				s = nb_sharks
			else :
				s=0
			self.zones[zones[i]]=Zone(zones[i][0],zones[i][1],s)
			 
    		self.predators=[]
		for i in xrange (nb_predators) :
      
			position=random.uniform(zones[0][0], zones[len(zones)-1][1])

			self.predators.append(Predator(position)) #correspond a un endroit random


	def Evo_population (self,zone) : # calculate how many sharks die or give birth, idem predators
		r0=0.47
		r=r0*(1+self.lateral_bio)^2
		K=600 
		e=0.47
		alpha0=0.4
		alpha=alpha0*(1+self.lateral_bio)/(1+self.ventral_bio)
		m=2
		beta=35
		h=0.1 #pas de temps
		nb_Rn=len(zone.sharks)
		nb_Pn=len(zone.predators)
		for t in range(0,1,1):
				nb_R=nb_Rn+h*r*nb_Rn*(1-nb_Rn/K)-alpha*nb_Rn*nb_Pn/(beta+nb_Rn)
				nb_P=nb_Pn+h*nb_Pn*e*(1-m*nb_Pn/nb_Rn)
				nb_Rn=nb_R
				nb_Pn=nb_P
		diff_R=round(nb_R-len(zone.sharks))
		diff_P=round(nb_P-len(zone.predators))
		return diff_R,diff_P

	def predation(self):
		diff_P_tot=0;
		for z in self.zones.values():
			diff_R,diff_P=Evo_population(z)
			diff_P_tot+=diff_P
			#Population de requin
			if (diff_R<0) :#Cas ou la population diminue
					z.killSharks(diff_R)
			else : #Cas ou la population augmente
					z.newSharks(diff_R)
					
		
		for p in range(abs(diff_P_tot)):
			Z=random.choice(d.values())
			if(diff_P_tot<0): #en pratique il faudrait prendre en compte le cas ou il n'y a pas suffisamment de predateur dans la zone
				Z.killPredator()
			else:
				Z.addPredator(Predator(Z.D))#a verifier en fonction de la definition du predateur.
      #ou alors on place aleatoirement les predateurs dans la mer,
      ### a chaque pas de temps on redistribue notre population totale
      #### et apres on les repartit dans une zone en fonction de la profondeur
        
        
