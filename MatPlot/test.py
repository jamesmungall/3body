import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

from MatPlot.mplot_file import Mplot


# Define systematic sampling function
def systematic_sampling(input_df, step):
    indexes = np.arange(0, len(input_df), step=step)
    result = input_df.iloc[indexes]
    return result


df = pd.read_csv('../three_body.csv')
# df = systematic_sampling(df, 10)  # take every 10th value

# Mplot.animate(df)

x1 = list(df['x1'])
y1 = list(df['y1'])
x2 = list(df['x2'])
y2 = list(df['y2'])
x3 = list(df['x3'])
y3 = list(df['y3'])

dx = []
for i in range(len(x2)):
    dx.append(x2[i]-x3[i])
dy = []
for i in range(len(y2)):
    dy.append(y2[i]-y3[i])


# create a figure, axis and plot element
fig = plt.figure()
ax = plt.axes(xlim=(1.1*min(x1+x2+x3), 1.1*max(x1+x2+x3)), ylim=(1.1*min(y1+y2+y3), 1.1*max(y1+y2+y3)))
line, = ax.plot([], [], marker='.', lw=0)


def animate(i):
    line.set_data([x1[i], x2[i], x3[i]], [y1[i], y2[i], y3[i]])
    return line,


plt.title('Mplot, 3 body')
anim = animation.FuncAnimation(fig, animate, frames=len(x1), interval=20, blit=True)
plt.show()
