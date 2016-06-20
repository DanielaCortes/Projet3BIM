
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone
from Interface import Interface
from Tkinter import *
import copy

###/!\ Ne pas enlever les commentaires sur predation tant que les coeff de lum n'ont pas ete modifies

#CREER ICI LE REQUIN MODELE
req1 = Shark([800, 999])
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")

S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, (800,999), 150,req1)


####################BOUCLE_PRINCIPALE##########################
print "----AVANT BOUCLE ----"
for i,Z in S.zones.items():
    print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum
for i in range(10000) : #Temps total a definir
    S.MoveZone()
    S.predation()
    for z in S.zones.values():
        z.updateCoeffLat()
print "----APRES BOUCLE ----"
for i,Z in S.zones.items():
	print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum   




########INTERFACE GRAPHIQUE#######
#~ fen = Tk()
#~ interface = Interface(fen)
#~ interface.mainloop()
#~ interface.destroy()

#req1 = Shark([800, 999])
#req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")
#
#print req1.pap
#print "\n pos : "
#print req1.position_ideale
#
#
##mutations d'un seul requin (100 fois)
#for i in range (10000000):
#  req1.toMute()
##Pour afficher le requin avant, apres et la difference entre les deux
#req1.req_final()
#req1.calculProfondeur()
#req1.updateBiolum()
#print req1.lateral_bio
#print req1.ventral_bio

#~ print (S.zones[(800,999)]).coeff_lat_lum
#~ S.zones[(800,999)].updateCoeffLat()
#~ print S.zones[(800,999)].coeff_lat_lum


######################PREDATOR###############
#for i,Z in S.zones.items():
# print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum
#for i in range(1):
#    S.predation()
#    for z in S.zones.values():
#        z.updateCoeffLat()
#for i,Z in S.zones.items():
# print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum


######################MOUVEMENT###############
#~ #ICI on fait bouger les requins sur une zone !!!
#~ for i in range(10): 
  #~ S.zones[(800,999)].moveShark()

#ICI on fait bouger les requin sur tout l ocean !!! 
#on compare avant apres et on voit bien qu ils ont bouge
#print "\n Avant de move \n" 
#for i,Z in S.zones.items():
# print i,len(Z.sharks)
#for i in range(1000):
# S.MoveZone()
#print "\n Apres move \n"   
#for i,Z in S.zones.items():
# print i,len(Z.sharks)
# 
