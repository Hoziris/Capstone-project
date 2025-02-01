import math

import config as c

#Building Variables
IA = (math.sqrt(c.FA) - 2*c.WT)**2  # Internal area (m2)
BA = 0.5 * c.FA  # Basement area (m2)
EP = 40  # External Perimeter (m)
FL = 1.2  # Finishing level coefficient: High 1.2, Medium 1, Low 0.8
LM = 1.1   # Level of maintenance coefficient: High 1.1, Medium 1, Low 0.9

#Exposure Variables
hi = c.he - c.GL # Internal height of water (m)
Vf = IA * hi + BA * c.BH
Nff = int(hi/c.IH) + 1 # Number of flooded floors


#Function

