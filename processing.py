from main_function import DamageCalculation, print_camembert
from config import user
from attributing_typology import complete_user
from AdaptationCost import adaptation_cost


DB_MAPPING = {
    "centralized": 0,
    "distributed": 1
}

EB_MAPPING = {
    "no": 0,
    "yes": 1
}

SH_MAPPING = {
    "individual": 0,
    "collective": 1
}

SJ_MAPPING = {
    "adjoined": 2,
    "separated": 4
}

SB_MAPPING = {
    "brick": 1,
    "concrete": 2,
    "stone": 3
}

SP_MAPPING = {
    "wood": 1,
    "porcelain_stoneware": 2,
    "natural": 3
}

EE_MAPPING = {
    "no": 0,
    "yes": 1
}

ER_MAPPING = {
    "no": 0,
    "yes": 1
}

QM_MAPPING = {
    "low": 0,
    "high": 1
}

def treatement(user_dict) :

    # Defining the type of flood and type of building
    #flood_type = "FloodTest" # FloodTest, Runoff, Quick Overflowing, Slow Overflowing, Rising Groundwater
    #adapt_package = "Pro" # None, Basic, Medium, Advanced or Pro

    db_value = user_dict["Db"]
    user_dict["Db"] = float(DB_MAPPING.get(db_value))

    eb_value = user_dict["Eb"]
    user_dict["Eb"] = float(EB_MAPPING.get(eb_value))

    sh_value = user_dict["Sh"]
    user_dict["Sh"] = float(SH_MAPPING.get(sh_value))

    sj_value = user_dict["Sj"]
    user_dict["Sj"] = float(SJ_MAPPING.get(sj_value))

    if user_dict.get("Sb") is not None:
        sb_value = user_dict["Sb"]
        user_dict["Sb"] = float(SB_MAPPING.get(sb_value))

    if user_dict.get("Sp") is not None:
        sp_value = user_dict["Sp"]
        user_dict["Sp"] = float(SP_MAPPING.get(sp_value))

    if user_dict.get("Ee") is not None:
        ee_value = user_dict["Ee"]
        user_dict["Ee"] = float(EE_MAPPING.get(ee_value))

    if user_dict.get("Er") is not None:
        er_value = user_dict["Er"]
        user_dict["Er"] = float(ER_MAPPING.get(er_value))

    if user_dict.get("Qm") is not None:
        qm_value = user_dict["Qm"]
        user_dict["Qm"] = float(QM_MAPPING.get(qm_value))

    user_filled = complete_user(user_dict)

    n, cn = DamageCalculation(user_dict["Flood_Scenario"], user_filled, "None")
    b, cb = DamageCalculation(user_dict["Flood_Scenario"], user_filled, "Basic")
    ba = adaptation_cost(user_filled, "Basic")
    m, cm = DamageCalculation(user_dict["Flood_Scenario"], user_filled, "Medium")
    ma = adaptation_cost(user_filled, "Medium")
    a, ca = DamageCalculation(user_dict["Flood_Scenario"], user_filled, "Advanced")
    aa = adaptation_cost(user_filled, "Advanced")
    p, cp = DamageCalculation(user_dict["Flood_Scenario"], user_filled, "Pro")
    pa = adaptation_cost(user_filled, "Pro")

    cba = {
        "None" : n,
        "Basic" : b + ba,
        "Medium" : m + ma,
        "Advanced" : a + aa,
        "Pro" : p + pa
    }

    min_cost = ("None", n)
    for val in cba :
        if cba[val] < min_cost[1] :
            min_cost = (val, cba[val])

    return n, min_cost