
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone
from Predator import Predator


S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, (800,999), 1500)
req1 = Shark([800, 999])
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")


####################MUTATION################

print req1.pap
print req1.tab_memoire_lateral[10][10]
#mutations d'un seul requin (100 fois)
for i in range (10000000):
  req1.toMute()
#Pour afficher le requin avant, apres et la difference entre les deux
req1.req_final()
req1.calculProfondeur()
req1.updateBiolum()
print req1.lateral_bio
print req1.ventral_bio

#~ print req1.pap
#~ print "\n pos : "
#~ print req1.position_ideale
#~ #mutations d'un seul requin (100 fois)
#~ for i in range (10000000):
  #~ req1.toMute()
#~ req1.calculProfondeur()
#~ print req1.pap
#~ #Pour afficher le requin avant, apres et la difference entre les deux
#~ req1.req_final()
#~ print "\n pos : "
#~ print req1.position_ideale



#######################PREDATOR###############
#~ print len(S.zones[(800,999)].sharks)
#~ pred=0
#~ print "--PREDATORS--"
#~ for z in S.zones.values():
    #~ pred+=z.predators
    #~ print z.predators
#~ print pred
print (S.zones[(800,999)]).coeff_lat_lum
S.zones[(800,999)].updateCoeffLat()
print S.zones[(800,999)].coeff_lat_lum

#~ S.predation()
#~ S.predation()
#~ S.predation()
#~ S.predation()
 
#~ print len(S.zones[(800,999)].sharks)
#~ pred=0
#~ print "--PREDATORS--"
#~ for z in S.zones.values():
    #~ pred+=z.predators
#~ print pred








#initialiser un requin a partir des fichiers images
#generaliser la population -> sinon trop long
#tour de boucle :
#
#
#
#
#
#

