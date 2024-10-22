from MatPlot.mplot_file import Mplot
from solutions.trial_three_body_file import TrialThreeBody

import numpy as np
import pandas as pd

"""
ref:https://arxiv.org/pdf/math/0511219
"""


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


df = pd.read_csv('../../tests/starting_params.csv')
print(df)
for i in range(12):
    print(df.iat[0, i])

trial = TrialThreeBody()
trial.set_G(1)
trial.set_m1(1)
trial.set_m2(1)
trial.set_m3(1)

trial.X1 = 1.07590
trial.Y1 = 0.0
trial.X2 = -0.07095
trial.Y2 = 0.0
trial.X3 = -1.00496
trial.Y3 = 0.0

trial.VX1 = 0.0
trial.VY1 = 0.19509
trial.VX2 = 0.0
trial.VY2 = -1.23187
trial.VX3 = 0.0
trial.VY3 = 1.03678

trial.dt = 0.001
trial.n_iterations = 20000
df = trial.get_df()
df = systematic_sampling(df, 10)  # take every 10th value
# Mplot.show(df)
Mplot.animate(df)
