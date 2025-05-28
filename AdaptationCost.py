adaptation_catalogue = {
    # PUMPING
    "PA1": 700, # Having a pump [€/unit]
    # BARRIERS
    "PA2": 900,  # Installation of one flood door [€/unit]
    "PA3": 3000,  # Installation of one flood window bay [€/unit]
    "PA4": 1000,  # Protection of boiler [€/unit]
    # Wall impermeability
    "PA5": 480,  # Covering of low vents [€/100m2]
    "PA6": 400,  # Reparation of external cracks [€/100m2]
    # Electricity and heating protection
    "PA7": 600,  # sealing of empty spaces in electrical systems [€/100m2]
    "PA8": 1500,  # Raising of electrical board [€/100m2]
    "PA9": 1200,  # Raising of switches [€/100m2]
    "PA10": 1200,  # Raising of plugs [€/100m2]
    "PA11": 1500,  # Raising of boiler [€/100m2]
    #Advanced electrical system protection
    "PA12": 1200,  # Raising of convectors [€/100m2]
    "PA13": 3000,  # Creation of descending electrical system [€/100m2]
    # Plumbing System
    "PA14": 1000,  # Installation of non-return valves on sewerage system [€/unit]
    "PA15": 600,  # Securing underground pipes [€/unit]
    # Pavement
    "PA16": 109, # Replacing ground pavement by impermeable one [€/m2]
    # Secondary work
    "PA17": 90, # Changing protective coating [€/m2]
    "PA18": 200, # Changing doors [€/unit]
    "PA19": 689, # Changing windows [€/unit]
    "PA20": 2300, # Changing entrance door [€/unit]
    "PA21": 90, # Changing partition walls [€/m2]
    # Floating objects
    "PA22": 200, # Anchoring of floating or dangerous equipments [€/100m2]

}

def adaptation_cost(user, adapt_package):

    Af = user["Ai"] / user["Nf"]

    CA1 = adaptation_catalogue["PA1"] * int(adapt_package != "None")
    CA2 = adaptation_catalogue["PA2"] * 0.02 * Af * int(adapt_package != "None")
    CA3 = adaptation_catalogue["PA3"] * int(adapt_package != "None")
    CA4 = adaptation_catalogue["PA4"] * int(adapt_package != "None")
    CA5 = adaptation_catalogue["PA5"] * Af/100 * int(adapt_package != "None")
    CA6 = adaptation_catalogue["PA6"] * Af/100 * int(adapt_package != "None")
    CA7 = adaptation_catalogue["PA7"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic")
    CA8 = adaptation_catalogue["PA8"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic")
    CA9 = adaptation_catalogue["PA9"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic")
    CA10 = adaptation_catalogue["PA10"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic")
    CA11 = adaptation_catalogue["PA11"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic")
    CA12 = adaptation_catalogue["PA12"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic") * int(adapt_package != "Medium")
    CA13 = adaptation_catalogue["PA13"] * Af/100 * int(adapt_package != "None") * int(adapt_package != "Basic") * int(adapt_package != "Medium")
    CA14 = adaptation_catalogue["PA14"] * int(adapt_package != "None")
    CA15 = adaptation_catalogue["PA15"] * int(adapt_package != "None")
    CA16 = adaptation_catalogue["PA16"] * Af/100 * (int(adapt_package == "Advanced") + int(adapt_package == "Pro"))
    CA17 = adaptation_catalogue["PA17"] * Af/100 * int(adapt_package == "Pro")
    CA18 = adaptation_catalogue["PA18"] * 0.09 * Af * int(adapt_package == "Pro")
    CA19 = adaptation_catalogue["PA19"] * 0.09 * Af * int(adapt_package == "Pro")
    CA20 = adaptation_catalogue["PA20"] * 0.02 * Af * int(adapt_package == "Pro")
    CA21 = adaptation_catalogue["PA21"] * user["Hf"] * Af/100 * int(adapt_package == "Pro")
    CA22 = adaptation_catalogue["PA22"] * Af/100 * int(adapt_package != "None")

    print("CA1", CA1)
    print("CA2", CA2)
    print("CA3", CA3)
    print("CA4", CA4)
    print("CA5", CA5)
    print("CA6", CA6)
    print("CA7", CA7)
    print("CA8", CA8)
    print("CA9", CA9)
    print("CA10", CA10)
    print("CA11", CA11)
    print("CA12", CA12)
    print("CA13", CA13)
    print("CA14", CA14)
    print("CA15", CA15)
    print("CA16", CA16)
    print("CA17", CA17)
    print("CA18", CA18)
    print("CA19", CA19)
    print("CA20", CA20)
    print("CA21", CA21)
    print("CA22", CA22)



    pa = round(CA1 + CA2 + CA3 + CA4 + CA5 + CA6 + CA7 + CA8 + CA9 + CA10 + CA11 + CA12 + CA13 + CA14 + CA15 + CA16 + CA17 + CA18 + CA19 + CA20 + CA21 + CA22)
    return pa