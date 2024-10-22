from MatPlot.mplot_file import Mplot
from solutions.trial_three_body_file import TrialThreeBody
import numpy as np


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


trial = TrialThreeBody()

df = trial.get_df()
# df = systematic_sampling(df, 10)  # take every 10th value
Mplot.animate(df)
