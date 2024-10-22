import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation

from MatPlot.mplot_file import Mplot


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


df = pd.read_csv('../three_body.csv')
df = systematic_sampling(df, 10)  # take every 10th value
df['dx3_x2'] = df.x3 - df.x2
df['dy3_y2'] = df.y3 - df.y2

df['time'] = np.arange(0, len(df))
# scatter plot
# Get current axis
ax = plt.gca()


df.plot(kind='scatter',
        x='x3',
        y='y3',
        c='time', cmap='viridis_r',
        s=3,
        marker='o', ax=ax)

# set the title
plt.title('Sun, earth, moon')

# show the plot
plt.show()
