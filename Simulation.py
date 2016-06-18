
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone


#CREER ICI LE REQUIN MODELE

#CREATION MER
S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, (800,999), 150)

####################BOUCLE_PRINCIPALE##########################
#for i in range(100000) : #Temps total à définir
#    	S.MoveZone()
#     S.predation()
     
####################MUTATION################
req1 = Shark([800, 999])
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")

print req1.pap
print "\n pos : "
print req1.position_ideale

#mutations d'un seul requin (100 fois)
for i in range (10000000):
  req1.toMute()
#Pour afficher le requin avant, apres et la difference entre les deux
req1.req_final()
req1.calculProfondeur()
req1.updateBiolum()
print req1.lateral_bio
print req1.ventral_bio

print (S.zones[(800,999)]).coeff_lat_lum
S.zones[(800,999)].updateCoeffLat()
print S.zones[(800,999)].coeff_lat_lum


######################PREDATOR###############
#print len(S.zones[(800,999)].sharks)
#S.predation()
#print len(S.zones[(800,999)].sharks)


######################MOUVEMENT###############
#~ #ICI on fait bouger les requins sur une zone !!!
#~ for i in range(10): 
	#~ S.zones[(800,999)].moveShark()

#ICI on fait bouger les requin sur tout l ocean !!! 
#on compare avant apres et on voit bien qu ils ont bouge
print "\n Avant de move \n" 
for i,Z in S.zones.items():
	print i,len(Z.sharks)
for i in range(1000):
	S.MoveZone()
print "\n Apres move \n" 	
for i,Z in S.zones.items():
	print i,len(Z.sharks)
	
