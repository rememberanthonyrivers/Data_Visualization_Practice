import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks as long as the program is active.
while True:
    # Make a random walk with 5000 points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points as a continuous path
    plt.figure(figsize=(10, 6))  # Adjust figure size
    plt.plot(rw.x_values, rw.y_values, linewidth=1, color="blue")

    # Emphasize the first and last points.
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)  # Starting point
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)  # Ending point

    # Remove the axes.
    plt.xticks([])  # Hide x-axis
    plt.yticks([])  # Hide y-axis

    # Show the plot
    plt.show()

    # Ask if the user wants to make another walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == "n":
        break