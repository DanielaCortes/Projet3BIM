
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
temps = []
print "----AVANT BOUCLE ----"
for i,Z in S.zones.items():
    print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum
<<<<<<< HEAD
for i in range(100000) : #Temps total a definir
    print (i)
    S.MoveZone()
=======
for i in range(10000) : #Temps total a definir
    S.MoveZone()
    print i
>>>>>>> d6f2f490c103b327d9a1d8c45a379fc310eba988
    S.predation()
    for z in S.zones.values():
        z.updateCoeffLat()
    nb_req.append(S.nb_sharks)
    temps.append(i)
    if i>45000:
        for j,Z in S.zones.items():
           print i,j,len(Z.sharks)  

print "----APRES BOUCLE ----"
for i,Z in S.zones.items():
    print i,len(Z.sharks),Z.coeff_lat_lum,Z.coeff_vent_lum   

plt.plot(temps, nb_req)
plt.show()
