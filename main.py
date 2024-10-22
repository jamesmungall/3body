from MatPlot.mplot_file import Mplot
from solutions.trial_three_body_file import TrialThreeBody

import numpy as np


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

trial.X1 = 0.716248295713
trial.Y1 = 0.384288553041
trial.X2 = 0.086172594591
trial.Y2 = 1.342795868577
trial.X3 = 0.538777980808
trial.Y3 = 0.481049882656

trial.VX1 = 1.245268230896
trial.VY1 = 2.444311951777
trial.VX2 = -0.675224323690
trial.VY2 = -0.962879613630
trial.VX3 = -0.570043907206
trial.VY3 = -1.481432338147

trial.dt = 0.001
trial.n_iterations = 10000
df = trial.get_df()
df = systematic_sampling(df, 10)  # take every 10th value
Mplot.show(df)
Mplot.animate(df)
