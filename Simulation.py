
import random
from Sea import Sea
from Shark import Shark
from Zone import Zone
from Predator import Predator


S= Sea(500,[(0,250),(251,500)],400, (0,250), 100)

req = Shark(1);
req.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")
print req.lateral_bio
print req.size
print req.ventral_bio
