import math
import matplotlib.pyplot as plt

from prices import catalogue
from config import exposure as exp, typology as typ

def DamageCalculation(flood_type, building_type) :

    if flood_type not in exp:
        raise ValueError(f"Type of flood '{flood_type}' not recognized.")
    if building_type not in typ:
        raise ValueError(f"Type of building '{building_type}' not recognized.")

    He, se, ve, d, q = exp[flood_type]["He"], exp[flood_type]["se"], exp[flood_type]["ve"], exp[flood_type]["d"], exp[flood_type]["q"]

    Ai, Tw, Nf, YY = typ[building_type]["Ai"], typ[building_type]["Tw"], typ[building_type]["Nf"], typ[building_type]["YY"]
    Hf, Hb, Hg, Hcs = typ[building_type]["Hf"], typ[building_type]["Hb"], typ[building_type]["Hg"], typ[building_type]["Hcs"]
    Sh, Sj, Sb, Db = typ[building_type]["Sh"], typ[building_type]["Sj"], typ[building_type]["Sb"], typ[building_type]["Db"]
    Eb, Ee, Er = typ[building_type]["Eb"], typ[building_type]["Ee"], typ[building_type]["Er"]

    s = 0

    #Building Variables
    Af = Ai / Nf # Area of one floor (m2)
    Ab = 0.5 * Af * Eb # Basement area (m2)
    Pf = 4 * math.sqrt(Af)  # Perimeter of a floor (m)
    Pb =  4 * math.sqrt(Ab)  # Perimeter of basement (m)
    Pw = 2.5 * Pf # Perimeter of external and internal walls (m)
    #Aw = Pw * Hf # Area of external and internal walls (m2)
    Lm = 1 - int(YY>=2005)  # Level of maintenance

    #Exposure Variables
    if He == 0:
        return s, {"Cp1" : 0, "Cp2": 0, "Cp3": 0, "Cp4": 0, "Cc1": 0, "Cc2": 0, "Cc3": 0, "Cc4": 0, "Cc5": 0, "Cc6": 0, "Cc7": 0, "Cc8": 0, "Cc9": 0, "Cc10": 0, "Cc11": 0, "Cc12": 0, "Cc13": 0, "Cc14": 0, "Cc15": 0, "Cc16": 0, "Cc17": 0, "Cs1" : 0, "Cs2" : 0, "Cs3" : 0, "total cost": s}
    Hi = max(He - Hg, 0) # Internal height of water (m)
    print("Hi =", Hi)
    Vu = Af * Hi + Ab * Hb + Af * Hcs
    print("Vu =", Vu)
    Nfu = (int(Hi/Hf) + 1) # Number of flooded floors
    print("Nfu =", Nfu)

    #print("Af =", Af)
    #print("Ab =", Ab)
    #print("Vu =", Vu)
    #print("Hi =", Hi)
    #print("Nfu =", Nfu)

    #Function

    # Cleaning

    # Cost of Pumping
    Ep1 = Af * Hcs + Ab * Hb + Ee * 8
    # need of more info on building structure
    Cp1 = Ep1 * catalogue["Pp1"]

    # Cost of Waste Disposal
    Ep2 = Vu * se * (1 + 0.4 * q)
    # mass of waste, cleaning increased by 40% in case of pollutants
    Cp2 = Ep2 * catalogue["Pp2"]

    # Cost of Cleaning
    Ep3 = (2 * Ab + Hb * Pb + (Hi + 1) * Pw + 2 * Af * Nfu * int(Hi>0) - Af) * (1 + 0.4 * q)
    Cp3 = Ep3 * catalogue["Pp3"]

    # Cost of dehumidification
    Ep4 = (Ab * Hb + Af * Hf * Nfu * int(Hi>0)) * (0.2 * int(d>=12) + 0.8 * int(d>=24) + 0.2 * int(d>=48))
    # Dehumidification needed only if d >= 24h
    Cp4 = Ep4 * catalogue["Pp4"]

    # Components

    # Cost of Pavement
    Ec1 = 0
    Cc1 = Ec1 * catalogue["Pc1"]

    # Cost of screed
    Ec2 = Af * Nfu * int(Hi>0)
    Cc2 = Ec2 * catalogue["Pc2"]

    # Cost of Baseboard
    Ec3 = Pw * Nfu * int(d>=24) * int(Hi>0)
    # Baseboards are replaced if d >= 24h
    Cc3 = Ec3 * catalogue["Pc3"]

    # Cost of Partition Wall
    Ec4 = 0.5 * Pw * Hf * Nfu * int(d>=24) * int(Hi>=1)
    # Partition walls are damaged if d >= 24h and Hi >= 1m
    Cc4 = Ec4 * catalogue["Pc4"]

    # Cost of Fake ceiling
    Ec5 = 0.2 * Af * (Nfu - 1 + int(Hi - (Nfu - 1)*Hf) >= Hf - 0.5) * int(Hi>0)
    # Fake ceiling is replaced for every storey where the water height touches it
    Cc5 = Ec5 * catalogue["Pc5"]

    # Cost of Internal Plaster
    Ec6 = Pw * (Hi + 1) * max(int(d>=24), q, Lm) * int(Hi>0)
    # Internal plaster if replaced if d>=24h or q=1 pr Lm=1
    Cc6 = Ec6 * catalogue["Pc6"]

    # Cost of External Plaster
    Ec7 = (Pw/4 + 2*Tw) * 4 * (He + 1) * max(int(d>=24), int(ve>=1.3), Lm)
    # External plaster is replaced if d>=24h or ve>=1.3m/s or Lm=1
    Cc7 = Ec7 * catalogue["Pc7"]

    # Cost of Doors Replacing
    # Cost of inside doors
    Ec8a = round((0.09 * Af * Nfu + 0.02 * Ab) * int(Hi>=0.1) * max(int(d>=24), int(ve>=1.3)) * int(Hi>0) +0.9)
    # Doors are replaced if He>=0.6m and if d>=24h or ve>=0.9m/s
    Cc8a = Ec8a * catalogue["Pc8a"]
    # Cost of main door
    Ec8b = max(int(He>=1.2), int(ve>=2), Lm) * int(Hi>0)
    Cc8b = Ec8b * catalogue["Pc8b"]
    # Locker main door
    Ec8c = int(Hi>=1.2) * int(se>=0.05)
    Cc8c = Ec8c * catalogue["Pc8c"]
    Cc8 = Cc8a + Cc8b + Cc8c

    # Cost of Windows replacing
    # Cost of traditional windows
    Ec9a = round((0.09 * Af * Nfu) * int(He>=1.5) * max(int(d>=24), int(ve>=0.9)) * int(Hi>0) + 0.9)
    # Windows are replaced if He>=1.5 and d>=24h or ve>=0.9m/s
    Cc9a = Ec9a * catalogue["Pc9a"]
    # Cost of Window bay
    Ec9b = (Sh == 0) * int(He>=1) * int(ve>=0.7) * int(Hi>0)
    Cc9b = Ec9b * catalogue["Pc9b"]
    Cc9 = Cc9a + Cc9b

    # Cost of Boilers
    # If boilers centralized (Db = 0)
    Ec10a = (1-Db) * (Eb + (1-Eb) * int(Hi>=1.6))
    # If there is a basement (Pb=1), boiler is replaced, if not (Pb=0), boilers replaced if Hi>=1.6m
    Cc10a = Ec10a * catalogue["Pc10a"]
    # If boilers distributed (Db = 1)
    Ec10b = Db  * (Nfu - 1 + int(Hi - (Nfu-1)*Hf >= 1.6)) * int(Hi>0)
    # Boilers replaced for each storey where water >= 1.6m
    Cc10b = Ec10b * catalogue["Pc10b"]
    Cc10 = Cc10a + Cc10b

    # Cost of Internal Painting
    Ec11 = (Hf * Nfu * Pw + Af * (Nfu-1)) * int(Hi>0)
    Cc11 = Ec11 * catalogue["Pc11"]

    # Cost of External Painting
    Ec12 = He * Pf
    Cc12 = Ec12 * catalogue["Pc12"]

    # Cost of Elevator reparations
    Ec13 = Ee * (int(Hi>=0.2) * 0.2 + int(Hi>=1.5) * 0.8)
    Cc13 = Ec13 * catalogue["Pc13"]

    # Cost of insulation
    Ec14 = Pw * (Hi + 1) * int(d>=24) * int(Hi>0)
    Cc14 = Ec14 * catalogue["Pc14"]

    # Cost of Radiators replacement
    # Cost of electrical radiators
    Ec15a = round(Er * 0.09 * (Nfu - 1 + int(Hi - (Nfu-1)*Hf)>= 0.2) * int(Hi>0) + 0.9)
    # Only of electrical radiators (Pr=1)
    Cc15a = Ec15a * catalogue["Pc15a"]
    # Cost of purging for nonelectrical radiators
    Ec15b = (1-Er) * 0.09 * (Nfu - 1 + int(Hi - (Nfu-1)*Hf)>= 0.5) * int(Hi>0)
    Cc15b = Ec15b * catalogue["Pc15b"]
    Cc15 = Cc15a + Cc15b

    # Cost of Electrical System
    Ec16a = Af * (int(Hi>=0.2) * 0.4 + int(Hi>=1.1) * 0.3 + int(Hi>=1.5) * 0.3)
    Cc16a = Ec16a * catalogue["Pc16a"]
    Ec16b = int(Hi>=2) * Lm
    Cc16b = Ec16b * catalogue["Pc16b"]
    Cc16 = Cc16a + Cc16b
    print("Cc16b =", Cc16b)

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

    s = round(Cp1 + Cp2 + Cp3 + Cp4 + Cs1 + Cs2 + Cs3 + Cc1 + Cc2 + Cc3 + Cc4 + Cc5 + Cc6 + Cc7 + Cc8 + Cc9 + Cc10 + Cc11 + Cc12 + Cc13 + Cc14 + Cc15 + Cc16 + Cc17)

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
        "Cc10": Cc10,
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
    #print(costs)
    #print(type(s))
    #print("Total costs =", s)
    return s, costs

def print_camembert(costs):
    labels = [key for key in costs if key != "total cost"]  # Excluding total cost
    values = [costs[key] for key in labels]

    colors = [
        "#66b3ff" if key.startswith("Cp") else  # Blue for "Cp"
        "#99ff99" if key.startswith("Cc") else  # Green for "Cc"
        "#ff9999" if key.startswith("Cs") else  # Red for "Cs"
        "#dddddd"  # Grey for default
        for key in labels
    ]

    plt.figure(figsize=(9,9))
    plt.pie(
        values,
        labels=[f"{label} ({costs[label]}€)" for label in labels],  # Labels with prices
        autopct='%1.1f%%',
        startangle=140,
        colors=colors
    )
    plt.title("Cost repartition")
    plt.suptitle(costs["total cost"])
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
#print("Cc16c =", Cc16c)
#print("Cc17 =", Cc17)
