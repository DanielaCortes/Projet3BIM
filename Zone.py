import random
from Shark import Shark
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
		self.coeff_lat_lum=0 
		self.coeff_vent_lum=0
		self.predators=0 #en fait on a pas vraiment besoin de stocker un predateur, juste le nombre. 
		if (nb_sharks > 0) :
			for i in xrange (nb_sharks) :
        			I = random.randint(prof_min, prof_max) # se situe aleatoirement dans la zone consideree
        			self.sharks.append(Shark((self.prof_min,self.prof_max))) #Append copie de requin1
              			if (i == 0) :
                			I = random.randint(prof_min, prof_max) # se situe aleatoirement dans la zone consideree
                			self.sharks.append(Shark((self.prof_min,self.prof_max)))
              			else :
               				self.sharks.append(copy.copy(self.sharks[0]))
		self.percent_shark=0.0 #pourcentage du nb de requins presents dans la zone
		self.newPercent(nb_sharks_tot)  # Mise a jour du pourcentage de requins dans la zone        

	#celui qu'on doit utiliser doit etre la moyenne de tous les requins qui sont dans la zone 
	def updateCoeffLat (self):
		slat=0
		sven=0
		if(len(self.sharks) !=0):
			for i,a in enumerate (self.sharks) :
				slat=slat+a.lateral_bio
				sven=sven+a.ventral_bio
			self.coeff_lat_lum=slat/len(self.sharks)
			self.coeff_vent_lum=sven/len(self.sharks)		
			

#Kill Sharks v1	: par rapport a la biolum
	"""def killSharks (self, nb_s) :  #on fournit le nombre de requins a tuer
		if (nb_s >= len(self.sharks)) : 
			self.sharks=[]
		else :
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
				self.sharks.remove(death_candidates[i])"""
  #KillSharksv2 : par rapport a la position et a bio lateral
	def killSharks (self, nb_s) :  #on fournit le nombre de requins a tuer
		if (nb_s >= len(self.sharks)) : #on tue tout le monde sans calculs si pas assez de requins
			self.sharks=[]
		else :
			fitness=[] #pour pouvoir comparer les fitness des requins
			for i,a in enumerate (self.sharks) :
				fitness.append(a.fit_position * a.lateral_bio) 
			for i in xrange (int(nb_s)) :
				fmax=max(fitness)
				death_candidats=[] #leur indice
				for j,a in enumerate (self.sharks) :
					if (a.fit_position == fmax) : 
						death_candidats.append(j)
				random.shuffle(death_candidates) # on tue aleatoirement un des requins qui a la fitness position max
				fitness.pop(death_candidates[0])
				self.sharks.pop(death_candidates[0])   
            

			
      
      
  #New Sharks v1 : par rapport a la biolum    
	"""def newSharks (self, nb_s) :  #requins a naitre
		new_candidates=[]
		for i, a in enumerate (self.sharks) :
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
			if (i<nb_s) :
				self.sharks.append(copy.copy(a))
		for i in xrange(nb_s):
			self.sharks.append(copy.copy(self.sharks[0]))"""
        
  #newSharks v2 : par rapport a fitness rep
	def newSharks (self, nb_s) :  #requins a naitre
		if (nb_s >= len(self.sharks)) :
			for i,a in enumerate (self.sharks) :
				self.sharks.append(copy.copy(a))
		else :
			fitness =[] #pour pouvoir comparer les fitness des requins
			for i,a in enumerate (self.sharks) :
				fitness.append(a.fit_reproduction)
			for i in xrange (int(nb_s)) :
				fmax = max(fitness)
				new_candidates =[] #leur indice
				for j,a in enumerate (self.sharks) :
					if (a.fit_reproduction == fmax and a.has_rep == False) : 
						new_candidates.append(j)
					random.shuffle(new_candidates) # on reproduit aleatoirement un des requins qui a la fitness position max
					fitness[new_candidates[0]] = -1
					self.sharks[new_candidates[0]].has_Reproduce()
					self.sharks.append(copy.copy(self.sharks[new_candidates[0]]))

    
    
    
	def addPredator (self) : 
		self.predators+=1
		
    
    
	def killPredator (self) :
		self.predators-=1



	def newPercent(self,nStot): #nStot : nb total of shark
		self.percent_shark=len(self.sharks)/nStot
		
