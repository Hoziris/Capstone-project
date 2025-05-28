import math
import matplotlib.pyplot as plt

from prices import catalogue
from config import exposure as exp, adapt

def DamageCalculation(flood_type, user, adaptation) :

    if flood_type not in exp:
        raise ValueError(f"Type of flood '{flood_type}' not recognized.")

    if adaptation not in adapt:
        raise ValueError(f"Adaptation Package '{adaptation}' not recognized.")

    He, se, ve, d, q = exp[flood_type]["He"], exp[flood_type]["se"], exp[flood_type]["ve"], exp[flood_type]["d"], exp[flood_type]["q"]
    Ai, Ad, Tw, Nf, Yc, Yr = user["Ai"], user["Ad"], user["Tw"], user["Nf"], user["Yc"], user["Yr"]
    Hf, Hb, Hg, Hcs = user["Hf"], user["Hb"], user["Hg"], user["Hcs"]
    Sh, Sj, Sb, Sp, Db = user["Sh"], user["Sj"], user["Sb"], user["Sp"],user["Db"]
    Eb, Ee, Er = user["Eb"], user["Ee"], user["Er"]

    Qc = user["Qc"] # Coefficient of quality, "low", "medium" or "high"
    Qm = user["Qm"] # Coefficient of maintenance, 0 - low, 1 - high
    if Qm is None :
        Qm = int(Yr>=2005)
    s = 0

    #Building Variables
    Af = Ai / Nf # Area of one floor (m2)
    Ab = 0.5 * Af * Eb # Basement area (m2)
    Pf = 4 * math.sqrt(Af)  # Perimeter of a floor (m)
    Pb =  4 * math.sqrt(Ab)  # Perimeter of basement (m)
    Pw = 2.5 * Pf # Perimeter of external and internal walls (m)
    Ad = int(Sh == 0) * Ai + int(Sh == 1) * (int(Ad > Af) * Af + int(Ad <= Af)) * Ad
    # for individual housing, Ad = Ai, for collective housing, if Ad overestimated, replaced by Af
    Nd = round(Ai / Ad) * Sh + (1 - Sh)  # Number of dwellings (unit)
    Ndf =  round (Nd/Nf) # Number of dwellings per floor (unit)

    #Exposure Variables
    if He <= 0 :
        return s, {"Cp1" : 0, "Cp2": 0, "Cp3": 0, "Cp4": 0, "Cc1": 0, "Cc2": 0, "Cc3": 0, "Cc4": 0, "Cc5": 0, "Cc6": 0, "Cc7": 0, "Cc8": 0, "Cc9": 0, "Cc10": 0, "Cc11": 0, "Cc12": 0, "Cc13": 0, "Cc14": 0, "Cc15": 0, "Cc16": 0, "Cc17": 0, "Cs1" : 0, "Cs2" : 0, "Cs3" : 0, "total cost": s}

    Hi = max(He - Hg, 0) # Internal height of water (m)

    # If Hi inferior to height of adaptation measures, water can't penetrate inside building
    if adaptation == ("Basic" or "Medium") :
        Hi = int(Hi>0.8) * Hi
    if adaptation == ("Advanced" or "Pro"):
        Hi = int(Hi>1) * Hi

    Vu = Af * Hi + Ab * Hb + Af * Hcs
    Nfu = (int(Hi/Hf) + 1) # Number of flooded floors
    Ndfu = Nfu * Ndf # Number of dwellings per floor underwater


    # FUNCTIONS

    # Preliminary Measures

    # Cost of Pumping
    Ep1 = (Af * Hcs + Ab * Hb + Ee * 8) * int(adaptation=="None")
    # Water needs to be pumped in the crawl space, basement and elevator
    # In case of adaptation measures, residents have their own pump and thus no cost of pumping
    Cp1 = Ep1 * catalogue["Pp1"]

    # Cost of Waste Disposal
    Ep2 = (Vu/1000 * (20 * int(se=="high") + 5 * int(se=="medium") + int(se=="low")) * (1 + 0.4 * q)) * (int(adaptation=="None") + 0.5 * int(adaptation!="None"))
    # mass of waste, cleaning increased by 40% in case of pollutants
    # In case of adaptation measures, active pumping decreases cost of preliminary measures
    Cp2 = Ep2 * catalogue["Pp2"]


    # Cost of Cleaning
    Ep3 = ((2 * Ab + Hb * Pb + (Hi * Pw + 2 * Af * Nfu - Af) * int(Hi>0) ) * (1 + 0.4 * q)) * (int(adaptation=="None") + 0.5 * int(adaptation!="None"))
    # Cleaning on all surfaces (floor, walls, ceilings, basement) with water, increased by 40% in case of pollutants
    # In case of adaptation measures, active pumping decreases cost of preliminary measures
    Cp3 = Ep3 * catalogue["Pp3"]


    # Cost of dehumidification
    Ep4 = ((Ab * Hb + Af * Hf * Nfu * int(Hi>0)) * (0.2 * int(d>=12) + 0.8 * int(d>=24) + 0.2 * int(d>=48))) * (int(adaptation=="None") + 0.5 * int(adaptation!="None"))
    # Dehumidification needed increases with duration
    # In case of adaptation measures, active pumping decreases cost of preliminary measures
    Cp4 = Ep4 * catalogue["Pp4"]

    # Components

    # Cost of Pavement
    # If pavement is wood or ceramic
    Ec1a = int(Sp==1) * int(d>24) * (Af * Nfu * int(Hi>0))
    Cc1a = Ec1a * catalogue["Pc1a"][Qc]
    #If pavement is porcelain stoneware
    Ec1b = int(Sp==2) * ( int(Yc<1990) * (0.2 + int(d>24) * 0.4) + int(Yc>1990) * int(d>48) * 0.2 ) * (Af * Nfu * int(Hi>0))
    Cc1b = Ec1b * catalogue["Pc1b"][Qc]
    # If pavement is marble or natural materials
    Ec1c = int(Sp==3) * (q * 0.2 * Af * Nfu * int(Hi>0)) * int(d>=72)
    Cc1c = Ec1c * catalogue["Pc1c"][Qc]
    Cc1 = (Cc1a + Cc1b + Cc1c) * (1 - int(adaptation=="Advanced") - int(adaptation=="Pro"))
    # In case of Advanced and Pro adaptation, no cost of pavement

    # Cost of screed
    Ec2 = Af * Nfu * int(Hi>0) * int(d>=12) * (1-Qm)
    # Screed is replaced if low level of maintenance and d>=12h
    Cc2 = Ec2 * catalogue["Pc2"][Qc]

    # Cost of Baseboard
    Ec3 = Pw * Nfu * int(d>=24) * int(Hi>0) * (1-int(Sp==1))
    # Baseboards are replaced if d >= 24h
    # If pavement is wood, cost of baseboard replacement is already taken into account in the pavement replacement
    Cc3 = Ec3 * catalogue["Pc3"][Qc]

    # Cost of Partition Wall
    Ec4 = 0.5 * Pw * Hf * Nfu * (int(d>=48)*0.5 + int(d>=72)*0.5)  * int(Hi>=1.6)
    # Partition walls are damaged if Hi >= 1m at 50% if d >= 48h and at 100% if d>=72h
    # Partition walls represent 50% of Pw
    Cc4 = (Ec4 * catalogue["Pc4"][Qc]) * int(adaptation != "Pro")

    # Cost of Fake ceiling
    Ec5 = 0.2 * Af * (Nfu - 1 + int(Hi - (Nfu - 1)*Hf) >= Hf - 0.5) * int(Hi>0) * int(d>=12)
    # Fake ceiling is replaced for every storey where the water height touches it
    # Fake ceiling assumed to represent 20% of total ceiling area
    Cc5 = Ec5 * catalogue["Pc5"][Qc]

    # Cost of Internal Plaster and Insulation
    Ec6 = Pw * (Hi + 0.2) * max(int(d>=36), q, Qm) * int(Hi>0.1)
    # Internal plaster and insulation are replaced if d>=24h or q=1 or Lm=1
    Cc6 = Ec6 * catalogue["Pc6"][Qc] * int(adaptation != "Pro")

    # Cost of External Plaster
    Ec7 = (Pw/4 + 2*Tw) * 4 * (He + 0.2) * max(int(d>=72), int(ve>=1.3), Qm)
    # External plaster is replaced if d>=24h or ve>=1.3m/s or Lm=1
    Cc7 = Ec7 * catalogue["Pc7"][Qc]

    # Cost of Doors Replacing
    # Cost of inside doors
    Ec8a = round((0.09 * Af * Nfu * int(Hi>=0.1) + 0.02 * Ab ) * max(int(d>=48), int(ve>=1.3)))
    # Doors are replaced if Hi>=0.1m and if d>=24h or ve>=1.3m/s
    # We assume 9 doors/100 meters, and 2 doors/100 meters in basement
    Cc8a = Ec8a * catalogue["Pc8a"][Qc]
    # Cost of main door
    Ec8b = max(int(He>=1.2), int(ve>=1.3), Qm) * (1 + Ndfu * Sh) * int(Hi>0)
    # Main door is replaced if He>=1.2m or vE>=2
    # In individual housing, there is only one entrance door, if collective housing, there are Nd + 1 entrance doors
    Cc8b = Ec8b * catalogue["Pc8b"][Qc]
    # Locker main door
    Ec8c = (1-int(Cc8b>0)) * int(Hi>=1.2) * (int(se=="high")+int(se=="medium")) * (1 + Ndfu * Sh) * int(Hi>0)
    # Locker is replaced if Hi>=1.2 and se>=0.05, if entrance doors are not changed
    Cc8c = Ec8c * catalogue["Pc8c"][Qc]
    Cc8 = (Cc8a + Cc8b + Cc8c) * int(adaptation != "Pro")

    # Cost of Windows replacing
    # Cost of traditional windows
    Ec9a = round(0.09 * Af * Nf * (Nfu - 1 + int((Hi - (Nfu-1)*Hf) >=1.5)) * max(int(d>=48), int(ve>=0.9))) * int(Hi>0)
    # Windows are replaced if the water level is >=1.5 and d>=24h or ve>=0.9m/s
    Cc9a = Ec9a * catalogue["Pc9a"][Qc]
    # Cost of Window bay
    Ec9b = (Sh == 0) * int(He>=1) * int(ve>=0.7) * (int(Qc=="medium") + int(Qc=="high")) * int(Hi>0)
    # The window bay is replaced if He>=1m and ve>=0.7m/s
    # We assume there is one window bay in every individual housing of medium or high quality
    Cc9b = Ec9b * catalogue["Pc9b"][Qc]
    Cc9 = (Cc9a + Cc9b) * int(adaptation != "Pro")

    # Cost of Boilers
    # If boilers centralized (Db = 0)
    Ec10a = (1-Db) * (Eb + (1-Eb) * int(Hi>=1.6))
    # If there is a basement (Eb=1), boiler is assumed to be there and replaced, if not (Eb=0), boiler is assumed to be on ground-floor and replaced if Hi>=1.6m
    Cc10a = Ec10a * catalogue["Pc10a"]
    # If boilers distributed (Db = 1)
    Ec10b = Db  * Ndf * (Nfu - 1 + int(Hi - (Nfu-1)*Hf >= 1.6)) * int(Hi>0)
    # Boilers replaced for each storey where water >= 1.6m, with one boiler per dwelling
    Cc10b = Ec10b * catalogue["Pc10b"]
    Cc10 = (Cc10a + Cc10b) * int(adaptation == "None")

    # Cost of Internal Painting
    Ec11 = (Hf * Nfu * Pw + Af * (Nfu-1)) * int(Hi>0.1)
    # Internal painting is needed for every wall and ceiling partially reached by water
    Cc11 = Ec11 * catalogue["Pc11"][Qc] * int(adaptation != "Pro")

    # Cost of External Painting
    Ec12 = He * Pf
    Cc12 = Ec12 * catalogue["Pc12"][Qc]

    # Cost of Elevator reparations
    Ec13 = Ee * (int(Hi>=0.2) * 0.2 + int(Hi>=1.5) * 0.8)
    # We assume 20% of damages if Hi>=0.2m and total damage if Hi>=1.5m
    Cc13 = Ec13 * catalogue["Pc13"][Qc]

    # Cost of Radiators replacement
    # Cost of electrical radiators
    Ec14a = round(Er * 0.09 * (Nfu - 1 + int(Hi - (Nfu-1)*Hf)>= 0.2)) * int(Hi>0)
    # Only of electrical radiators (Er=1), to be changed if water >=0.2m
    Cc14a = Ec14a * catalogue["Pc14a"] * (1 - int(adaptation == "Pro") - int(adaptation == "Advanced"))
    # Cost of purging for nonelectrical radiators
    Ec14b = round((1-Er) * 0.09 * (Nfu - 1 + int(Hi - (Nfu-1)*Hf)>= 0.3) *  (1-int(se=="no")) * int(Hi>0))
    # Only of non-electrical radiators (Er=0), to be purged if water >=0.3m
    Cc14b = Ec14b * catalogue["Pc14b"]
    # Cost of pulling out mud for nonelectrical radiators
    Ec14c = (1-Er) * int(se=="high") * int(Hi>=0.6)
    # Only of non-electrical radiators (Er=0), if se>0.1 and Hi>=0.6m
    Cc14c = Ec14c * catalogue["Pc14c"]
    Cc14 = (Cc14a + Cc14b + Cc14c) * (0.5 * int(adaptation != "None") + int(adaptation == "None")) * (1-int(adaptation=="Pro"))

    # Cost of Electrical System
    Ec15a = Af * (int(Hi>=0.2) * 0.2 + int(Hi>=1.1) * 0.3 + int(Hi>=1.6) * 0.5)
    # Electrical systems have 20% damages if Hi>=0.2m, 50% if Hi>=1.1m, 100% f Hi>=1.6
    Cc15a = Ec15a * catalogue["Pc15a"]
    # Cost of alarm system
    Ec15b = int(Hi>=2) * Qm
    # Alarm system is damaged is Hi>=2m
    # We assume there is alarm system in high maintained housing
    Cc15b = Ec15b * catalogue["Pc15b"][Qc]
    Cc15 = (Cc15a + Cc15b) * (int(adaptation == "None") + int(adaptation == "Basic"))

    # Cost of Plumbing System
    Ec16 = int(se=="high") * Af * (int(Hi>=0.15) * 0.1 + int(Hi>=0.4) * 0.2 + int(Hi>=0.9) * 0.2)
    # Plumbing is damaged if se>=0.1, with 10% of damages if Hi>=0.15, 30% if Hi>=0.4, 50% if Hi>=0.9
    Cc16 = Ec16 * catalogue["Pc16"] * int(adaptation != "None")
    # Structural Costs

    # Cost of soil consolidation
    Es1 = Af * Nfu * Hi * 0.03 * ( int(Sb==1) + int(Sb==3) )
    # Depends on Hi and only if building structure is brick or stone (Sb = 1 or 3)
    Cs1 = Es1 * catalogue["Ps1"]

    # Cost of Local Repair
    Es2 = Sj * Pf/4 * He * 0.05 * (1+int(se=="high")+int(se=="medium")) * max(int(Sb == 1), int(Sb == 3))  * int(ve>=2)
    # Depends on number of sides exposed (Sj) and only if building structure is brick or stone (Sb = 1 or 3) and ve>=2m/s
    Cs2 = Es2 * catalogue["Ps2"]

    # Cost of Pillar repair
    Es3 = Sj * (Pf/4) * He * 0.05 * (1+int(se=="high")+int(se=="medium")) * int(Sb == 2) * int(ve>=2)
    # Depends on number of sides exposed (Sj) and only if building structure is concrete (Sb=2) and ve>=2 m/s
    Cs3 = Es3 * catalogue["Ps3"]


    s = round(0.9 * (Cp1 + Cp2 + Cp3 + Cp4 + Cs1 + Cs2 + Cs3 + Cc1 + Cc2 + Cc3 + Cc4 + Cc5 + Cc6 + Cc7 + Cc8 + Cc9 + Cc10 + Cc11 + Cc12 + Cc13 + Cc14 + Cc15 + Cc16))
    # 10% of economies of scale

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
        "Cs1": Cs1,
        'Cs2': Cs2,
        'Cs3': Cs3,
        "total cost": s
    }


    #print(costs_adapt)
    #print(type(s))
    #print("Total costs =", s)
    return s, costs

def print_camembert(costs, flood_type):
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
    title = f"Cost Repartition\n\n Total cost: {costs["total cost"]}€"
    subtitle = f"Flood type: {flood_type}"
    plt.title(title)
    plt.suptitle(subtitle)
    plt.show()



    #print("Cp1 =", Cp1)
    #print("Cp2 =", Cp2)
    #print("Cp3 =", Cp3)
    #print("Cp4 =", Cp4)
    #print("Cc1 =", Cc1)
    #print("Cc2 =", Cc2)
    #print("Cc3 =", Cc3)
    #"print("Cc4 =", Cc4)
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
    #print("Cs1 =", Cs1)
    #print("Cs2 =", Cs2)
    #print("Cs3 =", Cs3)



