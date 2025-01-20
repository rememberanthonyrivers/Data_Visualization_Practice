# One of the simplest plots you can make in matplotlib
# lets display data in a graph ( We’ll use the square number sequence 1, 4, 9, 16, 25 as the data for the graph. )

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.plot(squares)
# .show() displays the graph in a meaningful way
# opens matplotlib’s viewer and displays the plot
plt.show()