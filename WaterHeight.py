from main_function import DamageCalculation
from config import exposure, user
from attributing_typology import complete_user
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":

    height = np.arange(0, 500, 0.1)
    total_preliminary_costs = []
    total_components_costs = []
    total_structural_costs = []
    total_costs = []
    cost_Cp1, cost_Cp2, cost_Cp3, cost_Cp4 = [], [], [], []
    cost_Cc1, cost_Cc2, cost_Cc3, cost_Cc4, cost_Cc5, cost_Cc6, cost_Cc7, cost_Cc8, cost_Cc9, cost_Cc10, cost_Cc11, cost_Cc12, cost_Cc13, cost_Cc14, cost_Cc15, cost_Cc16, cost_Cc17 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    cost_Cs1, cost_Cs2, cost_Cs3 = [], [], []
    exposure["FloodScenario"]["d"] = 24
    user_filled = complete_user(user)
    for i in height :
        exposure["FloodScenario"]["He"] = i / 100
        s, costs = DamageCalculation("FloodScenario", user_filled)
        cost_Cp1.append(costs["Cp1"])
        cost_Cp2.append(costs["Cp2"])
        cost_Cp3.append(costs["Cp3"])
        cost_Cp4.append(costs["Cp4"])
        cost_Cc1.append(costs["Cc1"])
        cost_Cc2.append(costs["Cc2"])
        cost_Cc3.append(costs["Cc3"])
        cost_Cc4.append(costs["Cc4"])
        cost_Cc5.append(costs["Cc5"])
        cost_Cc6.append(costs["Cc6"])
        cost_Cc7.append(costs["Cc7"])
        cost_Cc8.append(costs["Cc8"])
        cost_Cc9.append(costs["Cc9"])
        cost_Cc10.append(costs["Cc10"])
        cost_Cc11.append(costs["Cc11"])
        cost_Cc12.append(costs["Cc12"])
        cost_Cc13.append(costs["Cc13"])
        cost_Cc14.append(costs["Cc14"])
        cost_Cc15.append(costs["Cc15"])
        cost_Cc16.append(costs["Cc16"])
        cost_Cs1.append(costs["Cs1"])
        cost_Cs2.append(costs["Cs2"])
        cost_Cs3.append(costs["Cs3"])
        total_preliminary_costs.append(costs["Cp1"] + costs["Cp2"] + costs["Cp3"] + costs["Cp4"])
        total_components_costs.append(costs["Cc1"] + costs["Cc2"] + costs["Cc3"] + costs["Cc4"] + costs["Cc5"] + costs["Cc6"] + costs["Cc7"] + costs["Cc8"] + costs["Cc9"] + costs["Cc10"] + costs["Cc11"] + costs["Cc12"] + costs["Cc13"] + costs["Cc14"] + costs["Cc15"] + costs["Cc16"])
        total_structural_costs.append(costs["Cs1"] + costs["Cs2"] + costs["Cs3"])
        total_costs.append(s)

fig, axes = plt.subplots(2, 2, figsize=(15, 8))

axes[0][0].plot(height, cost_Cp1, label="Cp1")
axes[0][0].plot(height, cost_Cp2, label="Cp2")
axes[0][0].plot(height, cost_Cp3, label="Cp3")
axes[0][0].plot(height, cost_Cp4, label="Cp4")
axes[0][0].plot(height, total_preliminary_costs, label="Total preliminary costs", linewidth=2)
axes[0][0].set_title("Cost for different Cp values")
axes[0][0].set_xlabel("Height of external water (cm)")
axes[0][0].set_ylabel("Cost of Damages (€)")
axes[0][0].legend()
axes[0][0].grid(True)

axes[0][1].plot(height, cost_Cc1, label="Cc1")
axes[0][1].plot(height, cost_Cc2, label="Cc2")
axes[0][1].plot(height, cost_Cc3, label="Cc3")
axes[0][1].plot(height, cost_Cc4, label="Cc4")
axes[0][1].plot(height, cost_Cc5, label="Cc5")
axes[0][1].plot(height, cost_Cc6, label="Cc6")
axes[0][1].plot(height, cost_Cc7, label="Cc7")
axes[0][1].plot(height, cost_Cc8, label="Cc8")
axes[0][1].plot(height, cost_Cc9, label="Cc9")
axes[0][1].plot(height, cost_Cc10, label="Cc10")
axes[0][1].plot(height, cost_Cc11, label="Cc11")
axes[0][1].plot(height, cost_Cc12, label="Cc12")
axes[0][1].plot(height, cost_Cc13, label="Cc13")
axes[0][1].plot(height, cost_Cc14, label="Cc14")
axes[0][1].plot(height, cost_Cc15, label="Cc15")
axes[0][1].plot(height, cost_Cc16, label="Cc16")
axes[0][1].plot(height, total_components_costs, label="Total components costs", linewidth=2)
axes[0][1].set_title("Cost for different Cc values")
axes[0][1].set_xlabel("Height of external water (cm)")
axes[0][1].set_ylabel("Cost of Damages (€)")
axes[0][1].legend()
axes[0][1].grid(True)

axes[1][0].plot(height, cost_Cp1, label="Cp1")
axes[1][0].plot(height, cost_Cp2, label="Cp2")
axes[1][0].plot(height, cost_Cp3, label="Cp3")
axes[1][0].plot(height, total_structural_costs, label="Total structural costs", linewidth=2)
axes[1][0].set_title("Cost for different Cs values")
axes[1][0].set_xlabel("Height of external water (cm)")
axes[1][0].set_ylabel("Cost of Damages (€)")
axes[1][0].legend()
axes[1][0].grid(True)

axes[1][1].plot(height, total_costs, label="Total cost", linewidth=2)
axes[1][1].plot(height, total_preliminary_costs, label="Total preliminary costs")
axes[1][1].plot(height, total_components_costs, label="Total components costs")
axes[1][1].plot(height, total_structural_costs, label="Total structural costs")
axes[1][1].set_title("Repartition of costs according to water height")
axes[1][1].set_xlabel("Height of external water (cm)")
axes[1][1].set_ylabel("Cost of Damages (€)")
axes[1][1].legend()
axes[1][1].grid(True)

plt.tight_layout()
plt.show()



