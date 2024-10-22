import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tests.test_three_body import test_three_body
from tests.three_body_solutions import three_body_solutions


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


df = three_body_solutions()
df = systematic_sampling(df, 10)  # take every 10th value
#print(df)
# scatter plot
# Get current axis
ax = plt.gca()

df.plot(kind='scatter',
        x='x1',
        y='y1',
        c='time', cmap='viridis_r',
        s=30,
        marker='o', ax=ax)

df.plot(kind='scatter',
        x='x3',
        y='y3',
        c='time', cmap='plasma_r',
        s=3,
        marker='o', ax=ax)

df.plot(kind='scatter',
        x='x2',
        y='y2',
        c='time', cmap='magma_r',
        s=15,
        marker='o', ax=ax)

# set the title
plt.title('3body 1')

# show the plot
plt.show()
