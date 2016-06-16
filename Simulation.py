
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone


S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, (800,999), 150)
#req1 = Shark([800, 999])
#req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")


####################MUTATION################
#print req1.pap
##mutations d'un seul requin (100 fois)
#for i in range (10000000):
#    req1.toMute()
#
#print req1.pap
##Pour afficher le requin avant, apres et la difference entre les deux
#req1.req_final()


######################PREDATOR###############
#print len(S.zones[(800,999)].sharks)


#S.predation()

 
#print len(S.zones[(800,999)].sharks)



