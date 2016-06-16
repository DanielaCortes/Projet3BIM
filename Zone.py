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
	
	
	def __init__(self, prof_min, prof_max, nb_sharks,nb_sharks_tot) :
		#limites zones
		self.prof_min = prof_min  #0 m
		self.prof_max = prof_max # 1200 m (cf article )
		self.sharks=[]
		self.coeff_lat_lum=0.5 
		self.coeff_vent_lum=0.9
		self.predators=0 #en fait on a pas vraiment besoin de stocker un predateur, juste le nombre. 
		if (nb_sharks > 0) :
			for i in xrange (nb_sharks) :
        			I = random.randint(prof_min, prof_max) # se situe aleatoirement dans la zone consideree
        			self.sharks.append(Shark((self.prof_min,self.prof_max)))
		self.percent_shark=0.0 #pourcentage du nb de requins presents dans la zone
		self.newPercent(nb_sharks_tot)  # Mise a jour du pourcentage de requins dans la zone        

	
	#celui qu'on doit utiliser doit etre la moyenne de tous les requins qui sont dans la zone 
	def updateCoeffLat (self):
		slat=0
		sven=0
		if(len(self.sharks) !=0):
			for i in enumerate (self.sharks) :
				slat=slat+i.lateral_bio
				sven=sven+i.ventral_bio
			self.coeff_lat_lum=slat/len(self.sharks)
			self.coeff_vent_lum=sven/len(self.sharks)		
			
		
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
			#if (a.updateBiolum()< self.prof_max or a.updateBiolum() >self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
				new_candidates.append(a) 
		random.shuffle(new_candidates)
		if (len(new_candidates)<nb_s): #si pas assez de vivant, on fait quoi?
			copie = self.sharks
			random.shuffle(copie)
			for i, a in enumerate (copie) :
				if (a.updateBiolum()> self.prof_max or a.updateBiolum() <self.prof_min) : # a modifier, c est plutot I < a la lumiere de la zone
					new_candidates.append(a)
				if (len(new_candidates) == nb_s) :
					break 
        #peut-etre remelanger new_candidates Ici???
		for i,a in enumerate(new_candidates) : #ne fonctionne pas, ne rajoute pas un nombre limite de requins.
			if i<nb_s :
				self.sharks.append(copy.copy(a))
    
    
    
	def addPredator (self) : 
		self.predators+=1
		
    
    
	def killPredator (self) :
		self.predators-=1



	def newPercent(self,nStot): #nStot : nb total of shark
		self.percent_shark=len(self.sharks)/nStot
		
