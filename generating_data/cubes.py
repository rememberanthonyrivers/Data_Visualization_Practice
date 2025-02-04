import matplotlib.pyplot as plt

# First five cubic numbers
x_values_small = list(range(1, 6))
y_values_small = [x**3 for x in x_values_small]

# First 5000 cubic numbers
x_values_large = list(range(1, 5001))
y_values_large = [x**3 for x in x_values_large]

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Plot the first five cubic numbers
axs[0].scatter(x_values_small, y_values_small, color='blue')
axs[0].set_title("First Five Cubic Numbers", fontsize=16)
axs[0].set_xlabel("Value", fontsize=12)
axs[0].set_ylabel("Cube of Value", fontsize=12)
axs[0].tick_params(axis='both', labelsize=10)

# Plot the first 5000 cubic numbers
axs[1].scatter(x_values_large, y_values_large, color='red', s=1)  # Use smaller markers for better visualization
axs[1].set_title("First 5000 Cubic Numbers", fontsize=16)
axs[1].set_xlabel("Value", fontsize=12)
axs[1].set_ylabel("Cube of Value", fontsize=12)
axs[1].tick_params(axis='both', labelsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
