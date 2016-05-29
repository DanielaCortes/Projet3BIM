
import random

class Shark : 
	""" attributes :
	- depth
	- counter-illumination 
	- size
	- reproduction
	"""
	
	def __init__(self, file_name, zone) :
		self.position = zone # zone dans laquelle il se trouve #Ajouter une fonction qui détermine à partir bioluminescence où il se trouve ?
		self.coef_bio = 300 # son coefficient de biolum, valeur a modifier, c est juste une valeur random pour l instant !!!!!
		
		self.pmute = 0.08   # muting rate, 0.8 par million d annee
		    
		self.size=0 # len(requin), je sais pas si on en a besoin en fait 
		self.lateral_bio=0 # the intraspecific recognition one
		self.ventral_bio=0 # camouflage one
    
    #Lecture du ventre du requin 
		with open(file_name, 'r') as f:
			self.body = f.readlines() # rectangle, 
		for a in self.body :
			for b in a : 
				if (b != '-1') : 
					self.size +=1
					"""if ( int(b) <= #?  ) :
						self.lateral_bio +=1
					elif ( int(b) > # ?) :
						self.ventral_bio +=1"""
            
		self.bioluminescence = self.updateBiolum()
            
	def lateralBio(self) : 
		return self.lateral_bio*self.coef_bio

	def ventralBio(self) : 
		return self.ventral_bio*self.coef_bio
	      
	def updateBiolum(self) : 
		return self.lateralBio() + self.ventralBio()
  
  
  
  def initZone(self) : #donne la profondeur initiale en fonction de la proportion de requin recouvert par les photophores
    self.position=exp(2.31)*(self.ventralBio/self.size)^(-0.564)  
    
      
	def toMute (self) : # mute fluorescent parts ( plus de cas de figures genre mutation non fluorescentes ou alors une fluorescence au profit de l'autre ?
		mute = random.uniform()
		if (mute <= self.pmute) : 
			if (mute <= self.pmute/2) :
				self.lateral_bio +=1 #comment varie la bioluminsecence quand on mute ? On ajoute juste 1
			elif(mute > self.pmute/2) :
				self.ventral_bio +=1
				
	def toRep(self) : #cree une copie du requin self
		s = Shark("test.txt", self.position)
		s.size=self.size
		s.lateral_bio=self.lateral_bio
		s.ventral_bio = self.ventral_bio
		s.updateBiolum()
		return s
			
		
class Predator :
	
	def __init__(self,position) :
		self.position=position	

class Zone : 
	
	def __init__(self, prof_min, prof_max, nb_sharks) :
		
		#limites zones
		self.prof_min = prof_min  #0 m
		self.prof_max = prof_max # 1200 m (cf article )
		self.sharks=[]
    
		if (nb_sharks > 0) :
		
			for i in xrange (nb_sharks) :
        			I =random.randint(prof_min,prof_max) # se situe aleatoirement dans la zone consideree
        			self.sharks.append(Shark( "test.txt", I ))
			
		self.predateurs=[]
		
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
					break 

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
			self.sharks.append(a.toRep())
    
	def addPredator (self, p) : #pour les predateur on fournit direct le predateur a ajouter
		self.predateurs.append(p)
		
	def killPredator (self,p) :
		self.predateurs.remove(self.predateurs[0])

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
			if (zones[i] == starting_I) :
				s = nb_sharks
			else :
				s=0
			self.zones[zones[i]]=Zone(zones[i][0],zones[i][1],s)
			 
    		self.predators=[]
		for i in xrange (nb_predators) :
      
			position=random.uniform(zones[0][1], zones[len(zones)-1][1])

			self.predators.append(Predator(position)) #correspond a un endroit random

	#pour l'instant predation prend une zone comme argument mais en fait la fonction peut parcourir toutes les zones ?
	def predation (self,zone) : # calculate how many sharks die or give birth, idem predators
		
		
		#une fois le nombre de morts et le nombre de naissance utiliser 
		#zone.killSharks()
		#zone.newSharks ()
		
		#repartir les predateurs aleatoirement
		
		return 0
		
		

S= Sea(500,[(0,250),(251,500)],400, (0,250), 100)


