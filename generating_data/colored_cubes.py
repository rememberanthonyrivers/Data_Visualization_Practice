import matplotlib.pyplot as plt
import numpy as np

# First five cubic numbers
x_values_small = list(range(1, 6))
y_values_small = [x**3 for x in x_values_small]

# First 5000 cubic numbers
x_values_large = list(range(1, 5001))
y_values_large = [x**3 for x in x_values_large]

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Apply a colormap to the first five cubic numbers
scatter1 = axs[0].scatter(x_values_small, y_values_small, c=y_values_small, cmap='plasma', edgecolor='black', s=100)
axs[0].set_title("First Five Cubic Numbers", fontsize=16)
axs[0].set_xlabel("Value", fontsize=12)
axs[0].set_ylabel("Cube of Value", fontsize=12)
axs[0].tick_params(axis='both', labelsize=10)
fig.colorbar(scatter1, ax=axs[0], label="Cube Value")

# Apply a colormap to the first 5000 cubic numbers
scatter2 = axs[1].scatter(x_values_large, y_values_large, c=y_values_large, cmap='viridis', edgecolor='black', s=1)
axs[1].set_title("First 5000 Cubic Numbers", fontsize=16)
axs[1].set_xlabel("Value", fontsize=12)
axs[1].set_ylabel("Cube of Value", fontsize=12)
axs[1].tick_params(axis='both', labelsize=10)
fig.colorbar(scatter2, ax=axs[1], label="Cube Value")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
