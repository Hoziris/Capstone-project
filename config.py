#PARAMETERS TO FILL WITH CHARACTERISTICS AND TYPOLOGIES

# USER'S ANSWER FOR BUILDING CHARACTERISTICS

user = {
    # Mandatory questions for typologies
    "Sh": 0,  # Structure of housing (1 for collective housing, 0 for individual housing)
    "Yc": 1960,  # Year of construction
    "Nf": 2,  # Number of floors (including ground-floor)
    "Sj": 2,  # Structure juxtaposition (2 when 2 sides exposed in adjoined buildings, 4 when isolated building)
    "Db": 0,  # Distribution of boiler : 0- centralized, 1- Distributed
    "Eb": 1,  # Existence of basement : 0- no, 1- yes
    "Ai": 200,  # Internal Area (m2)

    # Non mandatory questions
    "Ad": 150,  # Area of one Dwelling (m2)
    "Hf": 2.5,  # Height of floor (m)
    "Hb": 2,  # Height of basement (m)
    "Hg": 0.1,  # Height of ground (m)
    "Sb": 1,  # Structure of building: 1- Masonry, 2- Reinforced concrete, 3- Stone
    "Sp": 2,  # Structure of Pavement: 1- Wood/Ceramic, 2-Porcelain Stoneware, 3-Marble/Natural Materials
    "Yr": 2000,  # Year of last major renovation
    "Tw": 0.4,  # Thickness of walls (m)
    "Ee": 0,  # Existence of elevator : 0- no, 1- yes
    "Er": 0,  # existence of electrical radiators : 0- No, 1- yes
    "Hcs": 0,  # Height of crawl space

    # Quality Questions
    "Qc": "medium",  # Quality of Construction
    "Qm": None,  # Quality of maintenance
    "Price": None  # Price of building
}


# EXPOSURE PARAMETERS FOR CHOSEN TYPE OF FLOOD

exposure = {
    "FloodTest" : {
    "He" : 2, # external water depth (m)
    "ve" : 1, #velocity (m/s)
    "se" : "high", # sediment concentration (qualitative) ("high", "medium", "low", "no")
    "d" : 49, # flood duration (h)
    "q" : 1 # presence of pollutants (1=oui, 0= non)
    },

    "FloodScenario" : {
        "He" : None, "ve" : 0.2, "se" : "low", "d" : None, "q" : 1
    },

    "Runoff" : {
        "He" : 2, "ve" : 1, "se" : "high", "d" : 12, "q" : 1
    },

    "Quick Overflowing" : {
        "He" : 1, "ve" : 2, "se" : "high", "d" : 3, "q" : 1
    },

    "Slow Overflowing" : {
        "He" : 1, "ve" : 0.2, "se" : "low", "d" : 72, "q" : 1
    },

    "Rising Groundwater" : {
        "He" : 0.3, "ve" : 0, "se" : "no", "d" : 100, "q" : 0
    }
}



adapt = {
    "None" : {
        "Pumping" : 0,
        "Barriers" : 0,
        "Wall impermeability" : 0,
        "Electricity and heating protection" : 0,
        "Advanced electrical system protection" : 0,
        "Plumbing system" : 0,
        "Secondary work" : 0,
        "Pavement" : 0,
        "Floating objects" : 0
    },

    "Basic" : {
        "Pumping" : 1,
        "Barriers" : 1,
        "Wall impermeability" : 1,
        "Electricity and heating protection" : 0,
        "Advanced electrical system protection" : 0,
        "Plumbing system" : 1,
        "Secondary work" : 0,
        "Pavement" : 0,
        "Floating objects" : 1
    },

    "Medium": {
        "Pumping": 1,
        "Barriers": 1,
        "Wall impermeability": 1,
        "Electricity and heating protection": 1,
        "Advanced electrical system protection": 0,
        "Plumbing system": 1,
        "Secondary work": 0,
        "Pavement": 0,
        "Floating objects": 1
    },

    "Advanced": {
        "Pumping": 1,
        "Barriers": 1,
        "Wall impermeability": 1,
        "Electricity and heating protection": 1,
        "Advanced electrical system protection": 1,
        "Plumbing system": 1,
        "Secondary work": 0,
        "Pavement": 1,
        "Floating objects": 1
    },

    "Pro": {
        "Pumping": 1,
        "Barriers": 1,
        "Wall impermeability": 1,
        "Electricity and heating protection": 1,
        "Advanced electrical system protection": 1,
        "Plumbing system": 1,
        "Secondary work": 1,
        "Pavement": 1,
        "Floating objects": 1
    }

}