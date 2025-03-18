#PARAMETERS TO FILL WITH CHARACTERISTICS AND TYPOLOGIES

# EXPOSURE PARAMETERS

exposure = {
    "FloodTest" : {
    "He" : 1, # external water depth (m)
    "ve" : 0.5, # velocity (m/s)
    "se" : 0.05, # sediment concentration
    "d" : 24, # flood duration (h)
    "q" : 1 # presence of pollutants (1=oui, 0= non)
    }
}

# BUILDING PARAMETERS

typology = {
    "BuildingTest" : {
    # Geometry
    "Ai" : 100, # Internal Area (m2)
    "Tw" : 0.4, # Thickness of walls (m)
    "Nf" : 2, # Number of floors (including ground-floor)
    "Hf" : 3, # Height of floor (m)
    "Hb" : 2.8, # Height of basement (m)
    "Hg" : 0.1, # Height of ground (m)
    "Sj" : 2, # Structure juxtaposition (2 when 2 sides exposed in adjoined buildings, 4 when isolated building=

    # Materials and equipments
    "Sb" : 2,     # Structure of building: 1- Masonry, 2- Reinforced concrete, 3- Stone
    "YY" : 1994,  # Year of construction
    "YR" : 1994, # Year of last major renovation
    "Pb" : 1, # Presence of basement : 0- no, 1- yes
    "Pe" : 1, # Presence of elevator : 0- no, 1- yes
    "Db" : 1, #Distribution of boiler : 0- centralized, 1- Distributed
    "Hcs" : 0.2, # Height of crawl space
    "Pr" : 1 # presence of electrical radiators : 0- No, 1- yes

    }
}