import random
from scipy import misc
from copy import *
import math
import matplotlib.pyplot as plt

class Shark : 
	""" attributes :
	- depth
	- counter-illumination 
	- size
	- reproduction
	"""
	
	def __init__(self, zone) :
		self.position = 0 #profondeur exacte
		self.coef_bio = 300 # son coefficient de biolum, valeur a modifier, c est juste une valeur random pour l instant !!!!!
		self.zone = zone
		#zone = [prof_min de la zone, prof_max de la zone]
		self.pmute = 0.08   # muting rate, 0.8 par million d annee
		self.size=200 # len(requin), je sais pas si on en a besoin en fait 
		self.lateral_bio=50 # the intraspecific recognition one
		self.ventral_bio=50 # camouflage one
		self.tab_ventral = []
		self.tab_lateral = []
		self.pap = 0 #Definition? Yasmina
		self.position_ideale = 0
		self.tab_memoire_lateral = []
		self.tab_memoire_ventral = []
            
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
		temp = 0
		for i in range (len(tableau_lateral)):
			for j in range (len(tableau_lateral[0])):
				if tableau_lateral[i][j] > 0:
					temp += 1
					self.lateral_bio += tableau_lateral[i][j]
		self.size += temp * 2
		for i in range (len(tableau_ventral)):
			for j in range (len(tableau_ventral[0])):
				if tableau_ventral[i][j] > 0:
					self.size += 1
					self.ventral_bio += tableau_ventral[i][j]
		self.lateral_bio *= 2
		self.tab_ventral = copy(tableau_ventral)
		self.tab_lateral = copy(tableau_lateral)
		self.tab_memoire_lateral = copy(tableau_lateral)
		self.tab_memoire_ventral = copy(tableau_ventral)
		self.pap = (self.lateral_bio + self.ventral_bio)/self.size


	def updateBiolum(self) : 
		self.pap = (self.lateral_bio + self.ventral_bio)/self.size *100
  
    
  
	def calculProfondeur(self) : #donne la profondeur initiale en fonction de la proportion de requin recouvert par les photophores
		self.position_ideale = 500 * math.exp(-0.564*math.log(self.pap)+2.31) 
    
      
	def toMute (self) : #On considere que ventral independant de lateral
		#et que 50% de chance de muter l'un ou l'autre
		#on considere qu'une case peut muter que si elle est a cote d'une case 
		#biolum ou elle meme biolum
		#on considere qu'il y a 1/3 de chance que la mutation enleve de la biolum
		# et 1/3 de chance qu'elle en rajoute et 1/3 de chance qu'elle fasse rien
		if (random.random() <= self.pmute) : #il y a mutation ?
			if (random.random() <= 0.5):  # je mute quoi ?
				amuter = copy(self.tab_lateral)
				tag = 0
			else:
				amuter = copy(self.tab_ventral)
				tag = 1
			modif = random.choice([-0.05, 0.05, 0.0]) # je mute de combien ?
			if modif!=0:
				flag = True
				while (flag):
					posx = random.randint(2, len(amuter)-2)
					posy = random.randint(2, len(amuter[0])-2)
					#on considere que les 4 coins peuvent pas muter (des -1 dans tt les cas)
					if amuter[posx][posy] > 0:
						flag = False
					if amuter[posx][posy+1] > 0 or amuter[posx][posy-1] > 0 or amuter[posx+1][posy] > 0 or amuter[posx-1][posy] > 0:
						flag = False
				if tag:
					a = self.tab_ventral[posx][posy] + modif
					if a >= 0.165 and a <= 1.0:
						self.tab_ventral[posx][posy] += modif
				else:
					a = self.tab_lateral[posx][posy] + modif
					if a >= 0.165 and a <= 1.0:
						self.tab_lateral[posx][posy] += modif


	def req_final(self):
		x=0
		for i in range (len(self.tab_lateral)):
			for j in range (len(self.tab_lateral[0])):
				if self.tab_lateral[i][j] < 0:
					self.tab_lateral[i][j] = 0
					self.tab_memoire_lateral[i][j] = 0
				self.tab_lateral[i][j] *= 255
				self.tab_memoire_lateral[i][j] *=255
				x+=(self.tab_lateral[i][j] - self.tab_memoire_lateral[i][j])
		print "difference de bioluminescence lateral = %f"%(x/255)
		plt.imshow(self.tab_memoire_lateral)
		plt.show()
		plt.imshow(self.tab_lateral)
		plt.show()
		plt.imshow(self.tab_lateral-self.tab_memoire_lateral)
		plt.show()
		x=0
		for i in range (len(self.tab_ventral)):
			for j in range (len(self.tab_ventral[0])):
				if self.tab_ventral[i][j] < 0:
					self.tab_ventral[i][j] = 0
					self.tab_memoire_ventral[i][j] = 0
				self.tab_ventral[i][j] *= 255
				self.tab_memoire_ventral[i][j] *=255
				x+=(self.tab_ventral[i][j] - self.tab_memoire_ventral[i][j])
		print "difference de bioluminescence ventral = %f"%(x/255)
		plt.imshow(self.tab_memoire_ventral)
		plt.show()
		plt.imshow(self.tab_ventral)
		plt.show()
		plt.imshow(self.tab_ventral-self.tab_memoire_ventral)
		plt.show()
