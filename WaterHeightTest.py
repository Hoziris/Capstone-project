from main_function import DamageCalculation
from config import exposure, typology
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":

    height = np.arange(0, 350, 0.1)
    total_costs_short_flood = []
    total_costs_long_flood = []
    for i in height :
        exposure["FloodScenario"]["He"] = i / 100
        exposure["FloodScenario"]["d"] = 12
        s, costs = DamageCalculation("FloodScenario", "BuildingTest")
        total_costs_short_flood.append(s/typology["BuildingTest"]["Ai"])
        exposure["FloodScenario"]["d"] = 48
        s, costs = DamageCalculation("FloodScenario", "BuildingTest")
        total_costs_long_flood.append(s/typology["BuildingTest"]["Ai"])

plt.plot(height, total_costs_short_flood, label='Short Flood')
plt.plot(height, total_costs_long_flood, label='Long Flood')

plt.xlabel("Height of water He (cm)")
plt.ylabel("Cost of Damages (€/m2)")
plt.title("Costs according to the water height")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



