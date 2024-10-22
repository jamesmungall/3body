from MatPlot.mplot_file import Mplot
from solutions.starting_params.starting_params import StartingParams
from solutions.trial_three_body_file import TrialThreeBody
import numpy as np


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


# def populate_trial_params(p):


trial = TrialThreeBody()
data = StartingParams()
p = data.params_5

trial.X1 = p[0]
trial.Y1 = p[1]
trial.X2 = p[2]
trial.Y2 = p[3]
trial.X3 = p[4]
trial.Y3 = p[5]

trial.VX1 = p[6]
trial.VY1 = p[7]
trial.VX2 = p[8]
trial.VY2 = p[9]
trial.VX3 = p[10]
trial.VY3 = p[11]

trial.n_iterations = 1000
trial.dt = 0.01
df = trial.get_df()
df = systematic_sampling(df, 10)  # take every 10th value
Mplot.show(df)
