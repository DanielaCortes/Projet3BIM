import random
from Shark import Shark
from Predator import Predator
import copy


class Zone : 
	"""attributes 
	- Depth max
	- Depth min
	- some sharks 
	- percent of sharks of the sea
	- coeff biolum lateral
	- coeff biolum ventral
	- nb of predator in the zone
	"""
	
	
	def __init__(self, prof_min, prof_max, nb_sharks) :
		#limites zones
		self.prof_min = prof_min  #0 m
		self.prof_max = prof_max # 1200 m (cf article )
		self.sharks=[]
		self.coeff_lat_lum=0 
		self.coeff_vent_lum=0 
		self.percent_shark=0.0 #pourcentage du nb de requins presents dans la zone
		self.predators=0 #en fait on a pas vraiment besoin de stocker un predateur, juste le nombre. 
		if (nb_sharks > 0) :
			for i in xrange (nb_sharks) :
        			I = random.randint(prof_min, prof_max) # se situe aleatoirement dans la zone consideree
        			#self.sharks.append(Shark( "test.txt", I )) # a mettre a jour non adapte a l'init de shark


		
	def killSharks (self, nb_s) :  #on fournit le nombre de requins a tuer
		death_candidates=[]
		for i,a in enumerate (self.sharks) :
			if (a.updateBiolum()> self.prof_max or a.updateBiolum() <self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
				death_candidates.append(a) 
		random.shuffle(death_candidates) #pas de biais
		if (len(death_candidates)<nb_s): #si pas assez de mort, on tue les requins bien adaptes
			copie = self.sharks
			random.shuffle(copie)
			for i, a in enumerate (copie) :
				if (a.updateBiolum()< self.prof_max or a.updateBiolum() >self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
					death_candidates.append(a)
				if (len(death_candidates) == nb_s) :
					break; 
		for i in xrange(nb_s) :
			self.sharks.remove(death_candidates[i])
			
      
      
      
	def newSharks (self, nb_s) :  #requins a naitre
		new_candidates=[]
		for i, a in enumerate (self.sharks) :
			if (a.updateBiolum()< self.prof_max or a.updateBiolum() >self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
				new_candidates.append(a) 
		random.shuffle(new_candidates)
		if (len(new_candidates)<nb_s): #si pas assez de mort, on tue les requins bien adaptes
			copie = self.sharks
			random.shuffle(copie)
			for i, a in enumerate (copie) :
				if (a.updateBiolum()> self.prof_max or a.updateBiolum() <self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
					new_candidates.append(a)
				if (len(new_candidates) == nb_s) :
					break 
		for i,a in enumerate(new_candidates) :
			self.sharks.append(copy.copy(a))
    
    
    
	def addPredator (self) : 
		self.predators+=1
		
    
    
	def killPredator (self) :
		self.predators-=1



	def newPercent(self,nStot): #nStot : nb total of shark
		self.percent_shark=len(self.sharks)/nStot
		
