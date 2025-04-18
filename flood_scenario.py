
from main_function import DamageCalculation
from config import exposure, typology
import numpy as np
import pandas as pd


if __name__ == "__main__":

    duration = np.arange(0, 145, 12)
    height = np.arange(0, 91, 10)
    matrix = np.full((len(height), len(duration)), np.nan)

    for i in duration:
        for j in height:
            exposure["FloodScenario"]["d"] = i
            exposure["FloodScenario"]["He"] = j/100
            matrix[int(j / 10), int(i / 12)] = DamageCalculation("FloodScenario", "BuildingTest")[0]

df = pd.DataFrame(matrix, index=height, columns=duration)
print(df)