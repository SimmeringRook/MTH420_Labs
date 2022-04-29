# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Thomas Knudson
MTH 420, S2022
Apr 29, 2022
"""

import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    return np.var(np.mean(np.random.normal(size=(n,n)), axis=0))

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    samples = np.arange(start=100, stop=1100, step=100)
    variance = np.zeros(samples.shape)
    for i, sample in enumerate(samples):
        variance[i] = var_of_means(sample)
    
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(samples, variance)
    plt.show()

# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    domain = np.linspace(-2*np.pi, 2*np.pi, num=50)
    sine, cosine, arctan  = np.sin(domain), np.cos(domain), np.arctan(domain)

    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(domain, sine, label="sin(x)")
    ax.plot(domain, cosine, label="cos(x)")
    ax.plot(domain, arctan, label="arctan(x)")

    ax.set_xlim( (-2*np.pi, 2*np.pi) )
    ax.set_xticks([x for x in np.linspace(-2*np.pi, 2*np.pi, 5)])
    pi = r'$\pi$'
    ax.set_xticklabels([f'{int(x/np.pi)}{pi}' for x in np.linspace(-2*np.pi, 2*np.pi, 5)])

    ax.set_ylim( (-np.pi/2, np.pi/2) )
    ax.set_yticks([y for y in np.linspace(-np.pi/2, np.pi/2, 5)])
    ax.set_yticklabels( [f'{y/np.pi}{pi}' for y in np.linspace(-np.pi/2, np.pi/2, 5)])

    plt.legend()
    plt.show()


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    fig, ax = plt.subplots(nrows=1, ncols=1)

    domain = np.linspace(-2,6)
    func = np.true_divide(1, np.subtract(domain, 1))

    first_interval, second_interval = np.argwhere(func < 0), np.argwhere(func>0)

    ax.plot(domain[first_interval], func[first_interval], 'm--', linewidth=4)
    ax.plot(domain[second_interval], func[second_interval], 'm--', linewidth=4)

    ax.set_xlim(-2, 6)
    ax.set_ylim(-6, 6)
    plt.show()

# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    domain = np.linspace(0, 2*np.pi, num=50)

    fig, axes = plt.subplots(nrows=2, ncols=2)
    data = [(domain, np.sin(domain), "sin(x)", 'g-'), (domain, np.sin(2*domain), "sin(2x)", 'r--'), (domain, 2*np.sin(domain), "2sin(x)", 'b--'), (domain, 2*np.sin(2*domain), "2sin(2x)", 'm--')]

    pi = r'$\pi$'

    x_ticks = [x for x in np.linspace(domain[0], domain[-1], 4)]
    x_labels = [f'{round(x/np.pi,1)}{pi}' for x in np.linspace(domain[0], domain[-1], 4)]
    y_ticks = [y for y in np.arange(-2,3)]
    y_labels = [f'{y}' for y in np.arange(-2,3)]

    from itertools import product
    for i, (xi, yi) in enumerate(product(range(2),range(2))):
        x, y, title, style = data[i]
        axes[xi, yi].plot(x, y, style)
        axes[xi, yi].set_title(title)

        axes[xi, yi].set_xlim( (domain[0], domain[-1]) )
        axes[xi, yi].set_xticks(x_ticks)
        axes[xi, yi].set_xticklabels(x_labels)

        axes[xi, yi].set_ylim( (-2, 2) )
        axes[xi, yi].set_yticks(y_ticks)
        axes[xi, yi].set_yticklabels(y_labels)

    plt.tight_layout()
    fig.suptitle("Plot of sine functions")
    plt.show()

# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    fig, (ax_heat, ax_contour) = plt.subplots(nrows=1, ncols=2)

    x_domain, y_domain = np.linspace(-2*np.pi,2*np.pi), np.linspace(-2*np.pi,2*np.pi)
    x_domain, y_domain = np.meshgrid(x_domain, y_domain)
    func = np.true_divide(np.multiply(np.sin(x_domain), np.sin(y_domain)), np.multiply(x_domain, y_domain))

    pcm = ax_heat.pcolormesh(x_domain, y_domain, func, cmap="viridis")
    fig.colorbar(pcm, ax=ax_heat)

    cont = ax_contour.contour(x_domain, y_domain, func, 10, cmap="viridis")
    fig.colorbar(cont, ax=ax_contour)

    pi = r'$\pi$'

    x_ticks = [x for x in np.linspace(-2*np.pi,2*np.pi, 4)]
    x_labels = [f'{round(x/np.pi,1)}{pi}' for x in np.linspace(-2*np.pi,2*np.pi, 4)]
    y_ticks = [y for y in np.linspace(-2*np.pi,2*np.pi, 4)]
    y_labels = [f'{round(y/np.pi,1)}{pi}' for y in np.linspace(-2*np.pi,2*np.pi, 4)]

    for ax in (ax_heat, ax_contour):
        ax.set_xlim((-2*np.pi,2*np.pi))
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_labels)

        ax.set_ylim((-2*np.pi,2*np.pi))
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_labels)

    plt.show()
