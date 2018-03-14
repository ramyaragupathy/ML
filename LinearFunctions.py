import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='darkgrid')

# Consider a linear function y = 3x + 1. Given two points, find the function's slope


def slope(x1, x2, y1, y2):
    value = (y2 - y1) / (x2 - x1)
    return value


slope_one = slope(0, 4, 1, 13)
slope_two = slope(5, -1, 16, -2)

# Let's describe the trajectory of a ball after it's kicked by a football player using y = -x^2 + 3x -1
# This is a non-linear equation
# Use numpy.linspace() to generate a NumPy array containing 301 values from 0 to 3 and assign to x.
x = np.linspace(0, 3, 100)
# Transform x by applying the function:y = -x^2 + 3x -1  Assign the resulting array of transformed values to y.
y = -1 * (x ** 2) + x * 3 - 1
# Use pyplot.plot() to generate a line plot with x on the x-axis and y on the y-axis.
plt.plot(x, y)
plt.show()


def draw_secant(x_values):
    x = np.linspace(-20, 30, 100)
    y = -1 * (x ** 2) + x * 3 - 1
    plt.plot(x, y)
    plt.show()

    
def draw_secant(x_values):
    x = np.linspace(-20, 30, 100)
    y = -1 * (x ** 2) + x * 3 - 1
    plt.plot(x, y)

    x_0 = x_values[0]
    x_1 = x_values[1]
    y_0 = -1 * (x_0 ** 2) + x_0 * 3 - 1
    y_1 = -1 * (x_1 ** 2) + x_1 * 3 - 1
    m = (y_1 - y_0) / (x_1 - x_0)
    b = y_1 - m * x_1

    y_secant = x * m + b
    plt.plot(x, y_secant, c='green')
    plt.show()


draw_secant([3, 5])
draw_secant([3, 10])
draw_secant([3, 15])
