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

trial.X1 = -1.609965115714630
trial.X1 = -1.60996
trial.Y1 = 0
trial.X2 = 1
trial.Y2 = 0
trial.X3 = 0
trial.Y3 = 0

trial.VX1 = 0
trial.VY1 = -0.6656909425824538
trial.VY1 = -0.66569
trial.VX2 = 0
trial.VY2 = -0.1529561125709906
trial.VY2 = -0.152956
trial.VX3 = 0
trial.VY3 = -(trial.m1 * trial.VY1 + trial.m2 * trial.VY2) / trial.m3

trial.dt = 0.01
trial.n_iterations = 10000
df = trial.get_df()
df = systematic_sampling(df, 1)  # take every 10th value
# Mplot.show(df)
Mplot.animate(df)