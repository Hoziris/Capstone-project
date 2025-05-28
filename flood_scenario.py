
from main_function import DamageCalculation
from config import user, exposure
from attributing_typology import complete_user
import numpy as np
import pandas as pd


if __name__ == "__main__":

    duration = np.arange(0, 145, 12)
    height = np.arange(0, 91, 10)
    matrix = np.full((len(height), len(duration)), np.nan)
    user_filled = complete_user(user)

    for i in duration:
        for j in height:
            exposure["FloodScenario"]["d"] = i
            exposure["FloodScenario"]["He"] = j/100
            matrix[int(j / 10), int(i / 12)] = DamageCalculation("FloodScenario", user_filled)[0]

df = pd.DataFrame(matrix, index=height, columns=duration)
print(df)