#PARAMETERS TO FILL WITH CHARACTERISTICS AND TYPOLOGIES

# EXPOSURE PARAMETERS

exposure = {
    "FloodTest" : {
    "He" : 1.5, # external water depth (m)
    "ve" : 5, #velocity (m/s)
    "se" : 0.1, # sediment concentration
    "d" : 24, # flood duration (h)
    "q" : 1 # presence of pollutants (1=oui, 0= non)
    },

    "FloodScenario" : {
        "He" : None, "ve" : 3, "se" : 0.2, "d" : None, "q" : 1
    },

    "Ruissellement" : {
        "He" : 2.5, "ve" : 3, "se" : 0.2, "d" : 12, "q" : 1
    },

    "Débordement" : {
        "He" : 1, "ve" : 0.5, "se" : 0.05, "d" : 24, "q" : 1
    },

    "Remontée de nappes" : {
        "He" : 0.5, "ve" : 0, "se" : 0, "d" : 100, "q" : 0
    }
}

# BUILDING PARAMETERS

typology = {
    "BuildingTest" : {
    # Geometry
    "Sh" : 1, # Structure of housing (1 for collective housing, 0 for individual housing)
    "Ai" : 50, # Internal Area (m2)
    "Tw" : 0.4, # Thickness of walls (m)
    "Nf" : 1, # Number of floors (including ground-floor)
    "Hf" : 2.5, # Height of floor (m)
    "Hb" : 0, # Height of basement (m)
    "Hg" : 1.5, # Height of ground (m)
    "Sj" : 2, # Structure juxtaposition (2 when 2 sides exposed in adjoined buildings, 4 when isolated building)

    # Materials and equipments
    "Sb" : 1,     # Structure of building: 1- Masonry, 2- Reinforced concrete, 3- Stone
    "YY" : 1960,  # Year of construction
    "YR" : 2000, # Year of last major renovation
    "Eb" : 0, # Existence of basement : 0- no, 1- yes
    "Ee" : 0, # Existence of elevator : 0- no, 1- yes
    "Db" : 0, #Distribution of boiler : 0- centralized, 1- Distributed
    "Hcs" : 0, # Height of crawl space
    "Er" : 0 # existence of electrical radiators : 0- No, 1- yes

    }
}