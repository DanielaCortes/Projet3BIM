import random
from scipy import misc
from copy import *
import math

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
		self.tab_ventral = tableau_ventral
		self.tab_lateral = tableau_lateral
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
		mute = random.random()
		valeurmodif = 0.01
		if (mute <= self.pmute) : 
			if (random.random() <= 0.5):
				amuter = copy(self.tab_ventral)
				tag = 0
			else:
				amuter = copy(self.tab_lateral)
				tag = 1
			flag = True
			while (flag):
				posx = random.randint(1,len(amuter)-1)
				posy = random.randint(1, len(amuter[0])-1)
				#on considere que les 4 coins peuvent pas muter
				if amuter[posx, posy+1] > 0 or amuter[posx, posy-1] > 0 or amuter[posx+1, posy] > 0 or amuter[posx-1, posy] > 0 :
					flag = False
			r = random.random()
			if (r < 1/3.0):
				modif = +valeurmodif
			elif (r < 2/3.0):
				modif = -valeurmodif
			else:
				modif = 0
			if tag == 0:
				a = self.tab_ventral[posx, posy] + modif
				if a > 0 and a < 1:
					self.tab_ventral[posx, posy] = a
					print "JE MUTE VENTRAL"
			else:
				a = self.tab_lateral[posx, posy] + modif
				if a > 0 and a < 1:
					self.tab_lateral[posx, posy] = a
					print "JE MUTE LATERAL"
			print "JE MUTE RIEN"


	def req_final(self):
		
		
		return 0
