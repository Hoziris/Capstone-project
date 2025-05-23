from main_function import DamageCalculation, print_camembert

if __name__ == "__main__":
    # Defining the type of flood and type of building
    flood_type = "Rising Groundwater"
    building_type = "BuildingTest"

    # Call of calculation of damages function
    try:
        costs = DamageCalculation(flood_type, building_type)[1]
        print(costs)
        print_camembert(costs, flood_type)
    except ValueError as e:
        print(f"Error : {e}")