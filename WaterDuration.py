from main_function import DamageCalculation
from config import exposure, typology
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":

    duration = np.arange(0, 200, 1)
    total_preliminary_costs = []
    total_components_costs = []
    total_structural_costs = []
    total_costs = []
    exposure["FloodScenario"]["He"] = 0.5
    for i in duration :
        exposure["FloodScenario"]["d"] = i
        s, costs = DamageCalculation("FloodScenario", "BuildingTest")
        total_preliminary_costs.append(costs["Cp1"] + costs["Cp2"] + costs["Cp3"] + costs["Cp4"])
        total_components_costs.append(costs["Cc1"] + costs["Cc2"] + costs["Cc3"] + costs["Cc4"] + costs["Cc5"] + costs["Cc6"] + costs["Cc7"] + costs["Cc8"] + costs["Cc9"] + costs["Cc10"] + costs["Cc11"] + costs["Cc12"] + costs["Cc13"] + costs["Cc14"] + costs["Cc15"] + costs["Cc16"] + costs["Cc17"])
        total_structural_costs.append(costs["Cs1"] + costs["Cs2"] + costs["Cs3"])
        total_costs.append(s)

plt.plot(duration, total_costs, label="Total cost")
plt.plot(duration, total_preliminary_costs, label="Total preliminary costs")
plt.plot(duration, total_components_costs, label="Total components costs")
plt.plot(duration, total_structural_costs, label="Total structural costs")
plt.xlabel("Duration of the flood (h)")
plt.ylabel("Cost of Damages (€)")
plt.title("Repartition of costs according to the flood duration")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
