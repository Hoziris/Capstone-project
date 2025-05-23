#PARAMETERS TO FILL WITH CHARACTERISTICS AND TYPOLOGIES

# EXPOSURE PARAMETERS

exposure = {
    "FloodTest" : {
    "He" : 0.5, # external water depth (m)
    "ve" : 0.5, #velocity (m/s)
    "se" : 0.1, # sediment concentration
    "d" : 48, # flood duration (h)
    "q" : 1 # presence of pollutants (1=oui, 0= non)
    },

    "FloodScenario" : {
        "He" : None, "ve" : 0.2, "se" : 0.05, "d" : None, "q" : 1
    },

    "Runoff" : {
        "He" : 2, "ve" : 1, "se" : 0.1, "d" : 12, "q" : 1
    },

    "Quick Overflowing" : {
        "He" : 1, "ve" : 2, "se" : 0.1, "d" : 3, "q" : 1
    },

    "Slow Overflowing" : {
        "He" : 1, "ve" : 0.2, "se" : 0.05, "d" : 72, "q" : 1
    },

    "Rising Groundwater" : {
        "He" : 0.3, "ve" : 0, "se" : 0, "d" : 100, "q" : 0
    }
}

# BUILDING PARAMETERS

typology = {
    "BuildingTest" : {

    #Geometry
    "Sh" : 0, # Structure of housing (1 for collective housing, 0 for individual housing)
    "Sj" : 2, # Structure juxtaposition (2 when 2 sides exposed in adjoined buildings, 4 when isolated building)
    "Ai" : 100, # Internal Area (m2)
    "Ad" : 100, #Area of one Dwelling (m2)
    "Nf" : 2, # Number of floors (including ground-floor)
    "Hf" : 2.5, # Height of floor (m)
    "Hb" : 0, # Height of basement (m)
    "Hg" : 0, # Height of ground (m)

    # Materials and equipments
    "Sb" : 1,     # Structure of building: 1- Masonry, 2- Reinforced concrete, 3- Stone
    "Sp" : 2, # Structure of Pavement: 1- Wood/Ceramic, 2-Porcelain Stoneware, 3-Marble/Natural Materials
    "YY" : 1960,  # Year of construction
    "YR" : 2000, # Year of last major renovation
    "Tw": 0.4,  # Thickness of walls (m)
    "Db" : 0, #Distribution of boiler : 0- centralized, 1- Distributed
    "Eb" : 0, # Existence of basement : 0- no, 1- yes
    "Ee" : 0, # Existence of elevator : 0- no, 1- yes
    "Er" : 0, # existence of electrical radiators : 0- No, 1- yes
    "Hcs": 0, # Height of crawl space

    },

    "LC1" : {
        "Sh" : 1, "Sj" : 2, "Ai" : 100, "Ad" : 0, "Nf" : 1, "Hf" : 2.5, "Hb" : 2, "Hg" : 0.1,
        "Sb" : 1, "Sp" : 1, "YY" : 1990, "Yr" : 2000, "Tw" : 0.4, "Db" : 1, "Eb" : 1, "Ee" : 0, "Er" : 0, "Hcs" : 0
    }
}