import random

class Shark : 
	""" attributes :
	- depth
	- counter-illumination 
	- size
	- reproduction
	"""
	
	def __init__(self, file_name, zone) :
		self.position = zone # zone dans laquelle il se trouve #Ajouter une fonction qui determine a partir bioluminescence ou il se trouve ?
		self.coef_bio = 300 # son coefficient de biolum, valeur a modifier, c est juste une valeur random pour l instant !!!!!
		self.zone=[0,0] ###est-ce que cet attribut est important? pas redondant avec position???
		self.pmute = 0.08   # muting rate, 0.8 par million d annee
		self.diffentesZones=[[0,100],[100,200]]#...    
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
  
	def zone(self) : 
		for z in self.diffentesZones :
			if(self.position>=z[0] and self.position<z[1]) : 
 				self.zone= z
        
    
  
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
