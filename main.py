from main_function import DamageCalculation, print_camembert
from config import user
from attributing_typology import complete_user
from AdaptationCost import adaptation_cost

if __name__ == "__main__":

    # Defining the type of flood and type of building
    flood_type = "Runoff" # FloodTest, Runoff, Quick Overflowing, Slow Overflowing, Rising Groundwater
    adapt_package = "Advanced" # None, Basic, Medium, Advanced or Pro

    # Call of calculation of damages function
    try:
        user_filled = complete_user(user)
        ca = adaptation_cost(user_filled, adapt_package)
        print("Adaptation measures cost", ca)
        s, costs_none = DamageCalculation(flood_type, user_filled, "None")
        t, costs_adapt = DamageCalculation(flood_type, user_filled, adapt_package)
        print("none", costs_none)
        print("advanced", costs_adapt)
        #print_camembert(costs, flood_type)
    except ValueError as e:
        print(f"Error : {e}")