import pandas as pd

from MatPlot.mplot_file import Mplot
from solutions.trial_three_body_file import TrialThreeBody
import numpy as np

"""
ref: https://numericaltank.sjtu.edu.cn/three-body/2022-NA-3body.pdf
Three body problem - from Newton to supercomputers and machine learning, Liao, Li Yang, New Astronomy 96 (2022) 101850
"""


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


trial = TrialThreeBody()
trial.set_G(1)
trial.m1 = 1.0
trial.m2 = 1.0
trial.m3 = 1.0

df_params = pd.read_csv('starting_params/3_body_starting_params.csv')

i = 2
trial.X1 = df_params.iat[i, 1]
trial.Y1 = df_params.iat[i, 2]
trial.X2 = df_params.iat[i, 3]
trial.Y2 = df_params.iat[i, 4]
trial.X3 = df_params.iat[i, 5]
trial.Y3 = df_params.iat[i, 6]
trial.VX1 = df_params.iat[i, 7]
trial.VY1 = df_params.iat[i, 8]
trial.VX2 = df_params.iat[i, 9]
trial.VY2 = df_params.iat[i, 10]
trial.VX3 = df_params.iat[i, 11]
trial.VY3 = df_params.iat[i, 12]

# rial.VY3 = -(trial.m1 * trial.VY1 + trial.m2 * trial.VY2) / trial.m3

trial.dt = 0.001
trial.n_iterations = 10000
df = trial.get_df()
df = systematic_sampling(df, 10)  # take every 10th value
# Mplot.show(df)
Mplot.animate(df)
