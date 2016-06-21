
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone
from Interface import Interface
from Tkinter import *
import matplotlib.pyplot as plt
import copy

###/!\ Ne pas enlever les commentaires sur predation tant que les coeff de lum n'ont pas ete modifies

#CREER ICI LE REQUIN MODELE
req1 = Shark()
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")

S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, 150,req1)


####################BOUCLE_PRINCIPALE##########################
nb_req = []
nb_req1=[]
nb_req2=[]
nb_req3=[]
nb_req4=[]
nb_req5=[]
nb_req6=[]
temps = []
print "----AVANT BOUCLE ----"
for i,Z in S.zones.items():
    print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum
for i in range(100000) : #Temps total a definir
    print (i)
    S.MoveZone()
    S.predation()
    for z in S.zones.values():
        z.updateCoeffLat()    
    nb_req.append(S.nb_sharks)
    nb_req1.append(len(S.zones[(0,199)].sharks))
    nb_req2.append(len(S.zones[(200,399)].sharks))
    nb_req3.append(len(S.zones[(400,599)].sharks))
    nb_req4.append(len(S.zones[(600,799)].sharks))
    nb_req5.append(len(S.zones[(800,999)].sharks))
    nb_req6.append(len(S.zones[(1000,1199)].sharks))
    temps.append(i)
    if i>45000:
        for j,Z in S.zones.items():
           print i,j,len(Z.sharks)  

print "----APRES BOUCLE ----"
for i,Z in S.zones.items():
    print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum   

plt.plot(temps, nb_req)
plt.show()



plt.plot(temps,  nb_req1,label="Zone 0-199")
plt.plot(temps,  nb_req2,label="Zone 200-399")
plt.plot(temps,  nb_req3,label="Zone 400-599")
plt.plot(temps,  nb_req4,label="Zone 600-799")
plt.plot(temps,  nb_req5,label="Zone 800-999")
plt.plot(temps,  nb_req6,label="Zone 1000-1199")


plt.legend()
plt.show()

#~ plt.plot(temps, nb_req1,label="Zone 0-199",temps, nb_req2,label="Zone 200-399",temps, nb_req3,temps, nb_req4,temps, nb_req5,temps, nb_req6 )
#~ plt.show()

#~ compteur = 0
#~ for z in S.zones.values():
    #~ print "Pour la zone de %d a %d : "%(compteur, compteur+200)
    #~ if z.req_final() != 0:
        #~ ventral, lateral = z.req_final()
        #~ plt.imshow(z.sharks[0].tab_memoire_ventral)
        #~ plt.show()
        #~ plt.imshow(a)
        #~ plt.show()
        #~ plt.imshow(z.sharks[0].tab_memoire_lateral)
        #~ plt.show()
        #~ plt.imshow(b)
        #~ plt.show()
    #~ compteur += 200




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
