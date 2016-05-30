
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
		self.zone=[0,0]
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
		
	def killPredator (self) :
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


	def Evo_population (self,zone) : # calculate how many sharks die or give birth, idem predators
		 #peut-etre definir les params du modele comme des attributs??
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
		nb_Pn=len(zone.predateurs)
		for t in range(0,1,1):
				nb_R=nb_Rn+h*r*nb_Rn*(1-nb_Rn/K)-alpha*nb_Rn*nb_Pn/(beta+nb_Rn)
				nb_P=nb_Pn+h*nb_Pn*e*(1-m*nb_Pn/nb_Rn)
				nb_Rn=nb_R
				nb_Pn=nb_P
		diff_R=round(nb_R-len(zone.sharks))
		diff_P=round(nb_P-len(zone.predateurs))
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
        
        
			
    
    
  	

		
		

S= Sea(500,[(0,250),(251,500)],400, (0,250), 100)


