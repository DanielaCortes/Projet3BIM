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
  
  
  def __init__(self, prof_min, prof_max, nb_sharks,nb_sharks_tot,ori_shark) :
    #limites zones
    self.prof_min = prof_min  #0 m
    self.prof_max = prof_max # 1200 m (cf article)
    self.sharks=[]
    self.coeff_lat_lum=0 
    self.coeff_vent_lum=0
    self.predators=0 #en fait on a pas vraiment besoin de stocker un predateur, juste le nombre.
    if (nb_sharks > 0) :
      #print "position de ORi"
      #print ori_shark.position
      #print "position ori ideale"
      #print ori_shark.position_ideale     
      for i in xrange (nb_sharks) :
        self.sharks.append(copy.copy(ori_shark))
    self.percent_shark=0.0 #pourcentage du nb de requins presents dans la zone
    self.newPercent(nb_sharks_tot)  # Mise a jour du pourcentage de requins dans la zone        
    self.updateCoeffLat()
          

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
        death_candidates=[] #leur indice
        for j,a in enumerate (self.sharks) :
          if (a.fit_position * a.lateral_bio == fmax) : 
            death_candidates.append(j)
        random.shuffle(death_candidates) # on tue aleatoirement un des requins qui a la fitness position max
        fitness.pop(death_candidates[0])
        self.sharks.pop(death_candidates[0])   
            

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
        self.sharks[-1].toMute()
    for i,a in enumerate (self.sharks) :
      a.reset_Rep();

    
    
    
  def addPredator (self) : 
    self.predators+=1
    
    
    
  def killPredator (self) :
    self.predators-=1


  def newPercent(self,nStot): #nStot : nb total of shark
    if nStot != 0:
      self.percent_shark=len(self.sharks)/float(nStot)
    else:
      self.percent_shark=0.0
    
    
  def moveShark(self):
    zdessous=[]#requins a mettre dans zone dessous
    zdessus=[] #requins a mettre au dessus
    indices=[] #indices requins a eliminer
    for i,a in enumerate (self.sharks):
      r=random.randint(-10, 10)
      if a.fit_position>60: #60 -> on verra
          pmove=0.8
      else :
          pmove=0.1
      ptest=random.uniform(0,1)
      if ptest<pmove :
        if(a.position+r>0  and a.position+r<1200 ): 
          a.position+=r
          a.updateFitPosition()  
          if( a.position<self.prof_min ):
            indices.append(i)
            zdessous.append(a)
          if(a.position>self.prof_max): 
            indices.append(i)
            zdessus.append(a) 
    for i,j in enumerate(indices) :
      del self.sharks[j-i] #permet a chaque fois quon suprime element decale l indice a supprimer
    return ([zdessous,  zdessus])

