from config import user

catalogue = {
    "Pp1" : 5, # pumping [€/m3]
    "Pp2" : 200, # waste disposal [€/m3]
    "Pp3" : 8, # cleaning [€/m2] 3 ?
    "Pp4" : 18, # dehumidification [€/m3]

    "Pc1a" : {"low" : 99, "medium" : 99, "high" : 141}, # wood pavement [€/m2]
    "Pc1b" : {"low" : 109, "medium" : 109, "high" : 0}, # porcelain stoneware pavement [€/m2]
    # High quality porcelain stoneware is not damaged in case of flood
    "Pc1c" : {"low" : 111, "medium" : 111, "high" : 200}, # natural materials pavement [€/m2]
    "Pc2" : {"low" : 25, "medium" : 25, "high" : 25}, # screed [€/m2]
    "Pc3" : {"low" : 12, "medium" : 12, "high" : 12}, # baseboard [€/ml]
    "Pc4" : {"low" : 128, "medium" : 128, "high" : 128}, # partition wall [€/m2]
    "Pc5" : {"low" : 50, "medium" : 64, "high" : 72}, # fake ceiling [€/m2]
    "Pc6" : {"low" : 50, "medium" : 52, "high" : 62}, # internal plaster and insulation [€/m2]
    "Pc7" : {"low" : 30, "medium" : 30, "high" : 30}, # external plaster [€/m2]
    "Pc8a" : {"low" : 138, "medium" : 182, "high" : 300}, # internal door [€/unit]
    "Pc8b": {"low" : 1930, "medium" : 3168, "high" : 3680},  # entrance door [€/unit]
    "Pc8c": {"low" : 632, "medium" : 763, "high" : 800},  # entrance lock door [€/unit]
    "Pc9a" : {"low" : 595, "medium" : 780, "high" : 1276}, # window [€/unit]
    "Pc9b" : {"low" : 867, "medium" : 1055, "high" : 1447}, # window bay [€/unit]
    "Pc10a" : (15300 + (user["Nf"]-1) * 2000) * user["Sh"] + 4500 * (1-user["Sh"]), # boiler centralized [€/unit]
    "Pc10b" : 4500, # boiler distributed [€/unit]
    "Pc11" : {"low" : 15, "medium" : 31, "high" : 36}, # internal painting [€/m2]
    "Pc12" : {"low" : 27, "medium" : 51, "high" : 51}, # external painting [€/m2]
    "Pc13" : {"low" : 500, "medium" : 1250, "high" : 2000}, # elevator [€/unit]
    "Pc14a" : 100 * int(user["Yc"]<1990) + 250 * int(user["Yc"]>=1990), # electric radiator [€/unit]
    "Pc14b" : 50, # radiator purging [€/unit]
    "Pc14c" : 10 * user["Ai"], # radiator mud pulled out [€/house]
    "Pc15a" : 100, # electrical system renovation [€/m2]
    "Pc15b" : {"low" : 0, "medium" : 500, "high" : 5500},# alarm system [€/unit]
    "Pc16" : 100, # plumbing system renovation [€/m2]

    "Ps1" : 300, # soil consolidation [€/m2]
    "Ps2" : 50, # local repairs [€/m2]
    "Ps3" : 300 # pillar repairs [€/m2]

}