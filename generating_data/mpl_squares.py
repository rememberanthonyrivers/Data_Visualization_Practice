# One of the simplest plots you can make in matplotlib
# lets display data in a graph ( We’ll use the square number sequence 1, 4, 9, 16, 25 as the data for the graph. )

import matplotlib.pyplot as plt

input_values= [1, 2, 3, 4, 5]
squares= [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# set chart title and label axes .
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels .
plt.tick_params(axis="both", labelsize=14)


# plt.plot(squares)
# .show() displays the graph in a meaningful way
# opens matplotlib’s viewer and displays the plot
plt.show()
