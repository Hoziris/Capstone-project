from config import typology

catalogue = {
    "Pp1" : 20, # pumping [€/m3]
    "Pp2" : 35, # waste disposal [€/m3]
    "Pp3" : 2.4, # cleaning [€/m2]
    "Pp4" : 18, # dehumidification [€/m3]

    "Pc1" : 0,
    "Pc2" : 5, # TBD
    "Pc3" : 11.99, # baseboard [€/ml]
    "Pc4" : 50.43, # partition wall [€/m2]
    "Pc5" : 16.56, # fake ceiling [€/m2]
    "Pc6" : 26.4, # internal plaster [€/m2]
    "Pc7" : 33.16, # external plaster [€/m2]
    "Pc8a" : 150, # internal door [€/unit]
    "Pc8b": 400,  # entrance door [€/unit]
    "Pc8c": 400,  # entrance lock door [€/unit]
    "Pc9a" : 150, # window [€/unit] TBD
    "Pc9b" : 400, # window bay [€/unit] TBD
    "Pc10a" : 17067.03 * typology["BuildingTest"]["Sh"] + 9000 * (1-typology["BuildingTest"]["Sh"]), # boiler centralized [€/unit]
    "Pc10b" : 3897.64, # boiler distributed [€/unit]
    "Pc11" : 10.50, # internal painting [€/m2]
    "Pc12" : 0, # external painting [€/m2] TBD
    "Pc13" : 2500, # elevator [€/unit] TBD
    "Pc14" : 5,
    "Pc15a" : 504.84, # electric radiator [€/unit]
    "Pc15b" : 100, # radiator purging [€/unit]
    "Pc16a" : 150,
    "Pc16b" : 500,
    "Pc17" : 200,

    "Ps1" : 300,
    "Ps2" : 50,
    "Ps3" : 300

}