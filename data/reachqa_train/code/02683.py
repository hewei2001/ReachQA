import matplotlib.pyplot as plt
import numpy as np

# Define months and solar power generation data for each terrain
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])
mountains_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])
urban_generation = np.array([15, 18, 20, 25, 30, 35, 38, 36, 30, 25, 20, 18])
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])

# Calculating percentage contributions
total_generation = desert_generation + mountains_generation + urban_generation + ocean_generation
desert_percentage = (desert_generation / total_generation) * 100
mountains_percentage = (mountains_generation / total_generation) * 100
urban_percentage = (urban_generation / total_generation) * 100
ocean_percentage = (ocean_generation / total_generation) * 100

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 9))

# First subplot: Stacked area chart
axs[0].fill_between(months, 0, desert_generation, color='orange', label='Desert', alpha=0.7)
axs[0].fill_between(months, desert_generation, desert_generation + mountains_generation, color='green', label='Mountains', alpha=0.7)
axs[0].fill_between(months, desert_generation + mountains_generation, desert_generation + mountains_generation + urban_generation, color='blue', label='Urban Areas', alpha=0.7)
axs[0].fill_between(months, desert_generation + mountains_generation + urban_generation, total_generation, color='purple', label='Oceans', alpha=0.7)
axs[0].set_title("Project Solstice:\nMonthly Solar Power Generation Across Terrains in 2123", fontsize=16, weight='bold', pad=20)
axs[0].set_xlabel("Months", fontsize=12)
axs[0].set_ylabel("Solar Power Generation (Gigawatts)", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].set_xticks(months)
axs[0].tick_params(axis='x', rotation=45)
axs[0].set_yticks(np.arange(0, 301, 50))
axs[0].legend(loc='upper left', fontsize=10)

# Second subplot: Line chart for percentage contributions
axs[1].plot(months, desert_percentage, marker='o', linestyle='-', color='orange', label='Desert')
axs[1].plot(months, mountains_percentage, marker='o', linestyle='-', color='green', label='Mountains')
axs[1].plot(months, urban_percentage, marker='o', linestyle='-', color='blue', label='Urban Areas')
axs[1].plot(months, ocean_percentage, marker='o', linestyle='-', color='purple', label='Oceans')
axs[1].set_title("Percentage Contribution of Terrains\n to Total Solar Power Generation", fontsize=16, weight='bold', pad=20)
axs[1].set_xlabel("Months", fontsize=12)
axs[1].set_ylabel("Contribution (%)", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].set_xticks(months)
axs[1].tick_params(axis='x', rotation=45)
axs[1].set_yticks(np.arange(0, 101, 20))
axs[1].legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()