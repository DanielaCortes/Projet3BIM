import random
from scipy import misc
from copy import *


class Shark : 
	""" attributes :
	- depth
	- counter-illumination 
	- size
	- reproduction
	"""
	
	def __init__(self, zone) :
		self.position = zone # zone dans laquelle il se trouve #Ajouter une fonction qui determine a partir bioluminescence ou il se trouve ?
		self.coef_bio = 300 # son coefficient de biolum, valeur a modifier, c est juste une valeur random pour l instant !!!!!
		self.zone=[0,0] ###est-ce que cet attribut est important? pas redondant avec position???
		self.pmute = 0.08   # muting rate, 0.8 par million d annee
		self.diffentesZones=[[0,100],[100,200]]#...    
		self.size=0 # len(requin), je sais pas si on en a besoin en fait 
		self.lateral_bio=0 # the intraspecific recognition one
		self.ventral_bio=0 # camouflage one
    
    #Lecture du ventre du requin 
            
		self.bioluminescence = self.updateBiolum()
            
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
		for i in range (len(tableau_lateral)):
			for j in range (len(tableau_lateral[0])):
				if tableau_lateral[i][j] > 0:
					self.size += 1
					self.lateral_bio += tableau_lateral[i][j]
		for i in range (len(tableau_ventral)):
			for j in range (len(tableau_ventral[0])):
				if tableau_ventral[i][j] > 0:
					self.size += 1
					self.ventral_bio += tableau_ventral[i][j]




	def updateBiolum(self) : 
		return self.lateral_bio*self.coef_bio + self.ventral_bio*self.coef_bio
  
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
