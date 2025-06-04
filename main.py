from main_function import DamageCalculation, print_camembert
from config import user
from attributing_typology import complete_user
from AdaptationCost import adaptation_cost
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

if __name__ == "__main__":

    # Defining the type of flood and type of building
    flood_type = "Runoff" # FloodTest, Runoff, Quick Overflowing, Slow Overflowing, Rising Groundwater
    adapt_package = "None" # None, Basic, Medium, Advanced or Pro

    # Call of calculation of damages function
    try:
        user_filled = complete_user(user)
        ca = adaptation_cost(user_filled, adapt_package)
        #print("Adaptation measures cost", ca)
        #print("none", costs_none)
        #print("advanced", costs_adapt)
        #print_camembert(costs_none, flood_type)
        n, cn = DamageCalculation(flood_type, user_filled, "None")
        b, cb = DamageCalculation(flood_type, user_filled, "Basic")
        ba = adaptation_cost(user_filled, "Basic")
        m, cm = DamageCalculation(flood_type, user_filled, "Medium")
        ma = adaptation_cost(user_filled, "Medium")
        a, ca = DamageCalculation(flood_type, user_filled, "Advanced")
        aa = adaptation_cost(user_filled, "Advanced")
        p, cp = DamageCalculation(flood_type, user_filled, "Pro")
        pa = adaptation_cost(user_filled, "Pro")

        cba = {
            "None": (n, 0),
            "Basic": (b, ba),
            "Medium": (m, ma),
            "Advanced": (a, aa),
            "Pro": (p, pa)
        }

        min_cost = ("None", n, 0)
        for val in cba:
            if (cba[val][0] + cba[val][1]) < (min_cost[1] + min_cost[2]):
                min_cost = (val, cba[val][0], cba[val][1])

        print(cba)

        x = ("None", "Basic", "Medium", "Advanced", "Pro")
        costs_of_flood = np.array([cba[option][0] for option in x])
        adaptation_measures = np.array([cba[option][1] for option in x])
        total_costs = costs_of_flood + adaptation_measures
        min_index = np.argmin(total_costs)

        width = 0.6
        fig, ax = plt.subplots()
        bottom = np.zeros(len(x))

        bars1 = ax.bar(x, adaptation_measures, width, label='Adaptation measures', color='lightblue')
        ax.bar_label(bars1, label_type='center', style = 'italic')
        bottom += adaptation_measures

        bars2 = ax.bar(x, costs_of_flood, width, bottom=bottom, label='Costs of damages', color='peachpuff')
        ax.bar_label(bars2, label_type='center')


        ax.set_title('Cost of flood for different adaptation packages (€)')
        ax.legend()

        plt.show()

    except ValueError as e:
        print(f"Error : {e}")