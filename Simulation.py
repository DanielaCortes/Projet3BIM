
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone
from Predator import Predator


S = Sea(1200,[(0,199),(200,399),(400,599),(600,799),(800,999),(1000,1199)],400, (800,999), 1500)
#req1 = Shark([800, 999])
#req1.ventral_lateralBio("requin_lateral.jpg", "requin_lateral.jpg")


print len(S.zones[(800,999)].sharks)
pred=0
print "--PREDATORS--"
for z in S.zones.values():
    pred+=z.predators
    print z.predators
print pred


S.predation()
S.predation()
S.predation()
S.predation()
 
print len(S.zones[(800,999)].sharks)
pred=0
print "--PREDATORS--"
for z in S.zones.values():
    pred+=z.predators
print pred

#initialiser un requin a partir des fichiers images
#generaliser la population -> sinon trop long
#tour de boucle :
#
#
#
#
#
#

####Problemes a resoudre - Questions

#P1 : Beaucoup trop long pour initialiser un requin #generaliser la population -> sinon trop long

#Q1 : Est-ce qu'on garde le fait que les predateurs sont creer aleatoirement? Possibilite qu'il y ait un nb faible de predateur dans la zone.
## >> Possibilite de mettre les predateurs proportionnellement au nb de proie dans chaque zone
## >> si 100% des proies dans la premiere zone, mettre 100% des predateurs
## >>> Si c'est le cas, modifier predation, partie ajout(suppression?) de predateurs

#Q2 : Est-ce qu'il est important d'avoir un attribut zone dans la classe Shark?
## >> Si oui, quel est son type? pas possible d'etre de classe zone car import shark dans zone et import zone dans shark pose probleme
## >> Doit etre de type tupple?

#P2 : Revoir newshark
## >> quel est la condition pour ajouter des requins dans candidate (pour l'instant en commentaire, tous les requins sont candidats)
## >> ancienne methode rajoutait autant de requins qu'il y avait de candidats. il ne faut en rajouter que nb_s : normalement corriger

#P3 : Eventuellement penser a prendre en compte dans kill shark le cas ou le nb de requin a tuer passer en parametre est superieur au nb de requin present. 
## >> dans ce cas, tuer toute la population direct sans autre calcul
## >> + verifier conditions

####Commentaires

# J'ai ajouter un parametre pour initialiser la classe zone (nb de requins total dans la mer) pr pouvoir calculer percent directement dans l'init

# Remettre a 0.0 les coeff de biolum dans l'init de zone (modifier pour tester predation)
# Remettre a 0.0 les coeff de biolum et size dans l'init de shark



