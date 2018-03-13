import numpy as np
import matplotlib.pyplot as plt

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
