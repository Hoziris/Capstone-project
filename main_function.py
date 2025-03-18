import math
import matplotlib.pyplot as plt

#import config as c
from prices import catalogue

#def main_function(He, se, ve, d, q, Ai, Tw, Nf, Hf, Hb, Hg, Sj, Sb, YY, Pb, Pe, Db, Hcs, Pr):

def DamageCalculation(flood_type, building_type, exposure, typology, price) :

    if flood_type not in exposure:
        raise ValueError(f"Type of flood '{flood_type}' not recognized.")
    if building_type not in typology:
        raise ValueError(f"Type of building '{building_type}' not recognized.")

    He = exposure[flood_type]["He"]
    se = exposure[flood_type]["se"]
    ve = exposure[flood_type]["ve"]
    d = exposure[flood_type]["d"]
    q = exposure[flood_type]["q"]

    Ai = typology[building_type]["Ai"]
    Tw = typology[building_type]["Tw"]
    Nf = typology[building_type]["Nf"]
    Hf = typology[building_type]["Hf"]
    Hb = typology[building_type]["Hb"]
    Hg = typology[building_type]["Hg"]
    Sj = typology[building_type]["Sj"]
    Sb = typology[building_type]["Sb"]
    YY = typology[building_type]["YY"]
    Pb = typology[building_type]["Pb"]
    Pe = typology[building_type]["Pe"]
    Db = typology[building_type]["Db"]
    Hcs = typology[building_type]["Hcs"]
    Pr = typology[building_type]["Pr"]


    #Building Variables
    Af = Ai / Nf # Area of one floor (m2)
    Ab = 0.5 * Af * Pb # Basement area (m2)
    Pf = 4 * math.sqrt(Af)  # Perimeter of a floor (m)
    Pb =  4 * math.sqrt(Ab)  # Perimeter of basement (m)
    Pw = 2.5 * Pf # Perimeter of external and internal walls (m)
    Aw = Pw * Hf # Area of external and internal walls (m2)
    Lm = 1 - int(YY>=2005)  # Level of maintenance

    #Exposure Variables
    Hi = max(He - Hg, 0) # Internal height of water (m)
    Vu = Af * Hi + Ab * Hb + Af * Hcs
    Nfu = int(Hi>=Hf) + 1 # Number of flooded floors

    print("Af =", Af)
    print("Ab =", Ab)
    print("Vu =", Vu)
    print("Hi =", Hi)
    print("Nfu =", Nfu)

    #Function

    # Cleaning

    # Cost of Pumping
    Ep1 = Af * Hcs + Ab * Hb + Pe * 8
    # need of more info on building structure
    Cp1 = Ep1 * catalogue["Pp1"]

    # Cost of Waste Disposal
    Ep2 = Vu * se * (1 + 0.4 * q)
    # mass of waste, cleaning increased by 40% in case of pollutants
    Cp2 = Ep2 * catalogue["Pp2"]

    # Cost of Cleaning
    Ep3 = (2 * Ab + Hb * Pb + Hi * Pf + 2 * Af * Nfu - Af) * (1 + 0.4 * q)
    Cp3 = Ep3 * catalogue["Pp3"]

    # Cost of dehumidification
    Ep4 = (Ab * Hb + Af * Hf * Nfu) * int(d>=24)
    # Dehumidification needed only if d >= 24h
    Cp4 = Ep4 * catalogue["Pp4"]

    # Components

    # Cost of Pavement
    Ec1 = 0
    Cc1 = Ec1 * catalogue["Pc1"]

    # Cost of screed
    Ec2 = Af * Nfu
    Cc2 = Ec2 * catalogue["Pc2"]

    # Cost of Baseboard
    Ec3 = Pf * Nfu * int(d>=24)
    # Baseboards are replaced if d >= 24h
    Cc3 = Ec3 * catalogue["Pc3"]

    # Cost of Partition Wall
    Ec4 = 0.5 * Pw * Nfu * int(d>=24) * int(He>=1.7)
    # Partition walls are damaged if d >= 24h and He >= 1.7m
    Cc4 = Ec4 * catalogue["Pc4"]

    # Cost of Fake ceiling
    Ec5 = 0.2 * Af * (Nfu - 1 + int(Hi - (Nfu - 1)*Hf) >= Hf - 0.5)
    # Fake ceiling is replaced for every storey where the water height touches it
    Cc5 = Ec5 * catalogue["Pc5"]

    # Cost of Internal Plaster
    Ec6 = Pw * (Hi + 1) * max(int(d>=24), q, Lm)
    # Internal plaster if replaced if d>=24h or q=1 pr Lm=1
    Cc6 = Ec6 * catalogue["Pc6"]

    # Cost of External Plaster
    Ec7 = (Pw/4 + 2*Tw) * 4 * (He + 1) * max(int(d>=24), int(ve>=1.3), Lm)
    # External plaster is replaced if d>=24h or ve>=1.3m/s or Lm=1
    Cc7 = Ec7 * catalogue["Pc7"]

    # Cost of Doors Replacing
    Ec8 = (0.135 * Af * Nfu + 0.034 * Ab) * int(He>=0.6) * max(int(d>=24), int(ve>=1.3))
    # Doors are replaced if He>=0.6m and if d>=24h or ve>=0.9m/s
    Cc8 = Ec8 * catalogue["Pc8"]

    # Cost of Windows replacing
    Ec9 = (0.135 * Af * Nfu) * int(He>=1.5) * max(int(d>=24), int(ve>=0.9))
    # Windows are replaced if He>=1.5 and d>=24h or ve>=0.9m/s
    Cc9 = Ec9 * catalogue["Pc9"]

    # Cost of Boilers
    # If boilers centralized (Db = 0)
    Ec10a = (1-Db) * (Pb + (1-Pb) * int(Hi>=1.6))
    # If there is a basement (Pb=1), boiler is replaced, if not (Pb=0), boilers replaced if Hi>=1.6m
    Cc10a = Ec10a * catalogue["Pc10a"]
    # If boilers distributed (Db = 1)
    Ec10b = Db  * (Nfu - 1 + int(Hi - (Nfu-1)*Hf >= 1.6))
    # Boilers replaced for each storey where water >= 1.6m
    Cc10b = Ec10b * catalogue["Pc10b"]

    # Cost of Internal Painting
    Ec11 = Hi * Pw + Hb * Pb
    Cc11 = Ec11 * catalogue["Pc11"]

    # Cost of External Painting
    Ec12 = He * Pf
    Cc12 = Ec12 * catalogue["Pc12"]

    # Cost of Elevator reparations
    Ec13 = Pe * (int(Hi>=0.2) * 0.2 + int(Hi>=1.5) * 0.6)
    Cc13 = Ec13 * catalogue["Pc13"]

    # Cost of insulation
    Ec14 = 0
    Cc14 = Ec14 * catalogue["Pc14"]

    # Cost of Radiators replacement
    Ec15 = Nfu * Af * 0.2 * Pr
    # Only of electrical radiators (Pr=1)
    Cc15 = Ec15 * catalogue["Pc15"]

    # Cost of Electrical System
    Ec16 = Af * (int(Hi>=0.2) * 0.4 + int(Hi>=1.1) * 0.3 + int(Hi>=1.5) * 0.3)
    Cc16 = Ec16 * catalogue["Pc16"]

    # Cost of Plumbing System
    Ec17 = max(int(se>=0.1), q) * Af * (int(Hi>=0.15) * 0.1 + int(Hi>=0.4) * 0.2 + int(Hi>=0.9) * 0.2)
    # plumbing is changed if se>=0.1 or q=1
    Cc17 = Ec17 * catalogue["Pc17"]

    # Structural Costs

    # Cost of soil consolidation
    Es1 = Af * Nfu * Hi * 0.01 * Sb
    Cs1 = Es1 * catalogue["Ps1"]

    # Cost of Local Repair
    Es2 = Sj * Pf/4 * He * 0.05 * (1+se) * max(int(Sb == 1), int(Sb == 3))
    # Depends on number of sides exposed (Sj) and only if building structure is brick or stone (Sb = 1 or 3)
    Cs2 = Es2 * catalogue["Ps2"]

    # Cost of Pillar repair
    Es3 = Sj * (Pf/4) * He * 0.15 * (1+se) * int(Sb == 2)
    # Depends on number of sides exposed (Sj) and only if building structure is concrete (Sb=2)
    Cs3 = Es3 * catalogue["Ps3"]

    s = Cp1 + Cp2 + Cp3 + Cp4 + Cs1 + Cs2 + Cs3 + Cc1 + Cc2 + Cc3 + Cc4 + Cc5 + Cc6 + Cc7 + Cc8 + Cc9 + Cc10a + Cc10b + Cc11 + Cc12 + Cc13 + Cc14 + Cc15 + Cc16 + Cc1

    costs = {
        "Cp1" : Cp1,
        "Cp2": Cp2,
        "Cp3": Cp3,
        "Cp4": Cp4,
        "Cc1": Cc1,
        "Cc2": Cc2,
        "Cc3": Cc3,
        "Cc4": Cc4,
        "Cc5": Cc5,
        "Cc6": Cc6,
        "Cc7": Cc7,
        "Cc8": Cc8,
        "Cc9": Cc9,
        "Cc10": Cc10a + Cc10b,
        "Cc11": Cc11,
        "Cc12": Cc12,
        "Cc13": Cc13,
        "Cc14": Cc14,
        "Cc15": Cc15,
        "Cc16": Cc16,
        "Cc17": Cc17,
        "Cs1": Cs1,
        'Cs2': Cs2,
        'Cs3': Cs3,
        "total cost": s
    }
    print(costs)
    return costs

def print_camembert(costs):
    labels = [key for key in costs if key != "total cost"]  # we exclude the total cost
    values = [costs[key] for key in labels]

    # Definition of colors according to the family of costs
    colors = [
        "#66b3ff" if key.startswith("Cp") else  # blue for "Cp"
        "#99ff99" if key.startswith("Cc") else  # green for "Cc"
        "#ff9999" if key.startswith("Cs") else  # red for "Cs"
        "#dddddd"  # Default grey
        for key in labels
    ]

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Share of component costs")
    plt.show()



#print("Cc1 =", Cc1)
#print("Cc2 =", Cc2)
#print("Cc3 =", Cc3)
#print("Cc4 =", Cc4)
#print("Cc5 =", Cc5)
#print("Cc6 =", Cc6)
#print("Cc7 =", Cc7)
#print("Cc8 =", Cc8)
#print("Cc9 =", Cc9)
#print("Cc10 =", Cc10a + Cc10b)
#print("Cc11 =", Cc11)
#print("Cc12 =", Cc12)
#print("Cc13 =", Cc13)
#print("Cc14 =", Cc14)
#print("Cc15 =", Cc15)
#print("Cc16 =", Cc16)
#print("Cc17 =", Cc17)
