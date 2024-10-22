import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Mplot:


    @staticmethod
    def show(df):
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

    @staticmethod
    def show_velocities(df):
        # scatter plot
        # Get current axis
        ax = plt.gca()

        df.plot(kind='scatter',
                x='vx1',
                y='vy1',
                c='time', cmap='viridis_r',
                s=30,
                marker='o', ax=ax)

        df.plot(kind='scatter',
                x='vx3',
                y='vy3',
                c='time', cmap='plasma_r',
                s=3,
                marker='o', ax=ax)

        df.plot(kind='scatter',
                x='vx2',
                y='vy2',
                c='time', cmap='magma_r',
                s=15,
                marker='o', ax=ax)

        # set the title
        plt.title('3body velocities')

        # show the plot
        plt.show()

    @staticmethod
    def animate(df):
        x1 = list(df['x1'])
        y1 = list(df['y1'])
        x2 = list(df['x2'])
        y2 = list(df['y2'])
        x3 = list(df['x3'])
        y3 = list(df['y3'])

        # create a figure, axis and plot element
        fig = plt.figure()
        ax = plt.axes(xlim=(1.1 * min(x1 + x2 + x3), 1.1 * max(x1 + x2 + x3)),
                      ylim=(1.1 * min(y1 + y2 + y3), 1.1 * max(y1 + y2 + y3)))
        line, = ax.plot([], [], marker='.', lw=0)

        def animate(i):
            line.set_data([x1[i], x2[i], x3[i]], [y1[i], y2[i], y3[i]])
            return line,

        plt.title('Mplot, 3 body')
        anim = animation.FuncAnimation(fig, animate, frames=len(x1), interval=20, blit=True)
        plt.show()

