import matplotlib.pyplot as plt
import numpy as np

# Define months and solar power generation data for each terrain
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])  # In gigawatts
mountains_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])  # In gigawatts
urban_generation = np.array([15, 18, 20, 25, 30, 35, 38, 36, 30, 25, 20, 18])  # In gigawatts
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])  # In gigawatts

# Stacking data for cumulative area plot
total_generation = desert_generation + mountains_generation + urban_generation + ocean_generation
mountains_cumulative = desert_generation + mountains_generation
urban_cumulative = mountains_cumulative + urban_generation
ocean_cumulative = urban_cumulative + ocean_generation

# Create a figure and axis for the plot
plt.figure(figsize=(14, 9))

# Plot each terrain's solar power generation as a stacked area chart
plt.fill_between(months, 0, desert_generation, color='orange', label='Desert', alpha=0.7)
plt.fill_between(months, desert_generation, mountains_cumulative, color='green', label='Mountains', alpha=0.7)
plt.fill_between(months, mountains_cumulative, urban_cumulative, color='blue', label='Urban Areas', alpha=0.7)
plt.fill_between(months, urban_cumulative, ocean_cumulative, color='purple', label='Oceans', alpha=0.7)

# Title and labels
plt.title("Project Solstice:\nMonthly Solar Power Generation Across Terrains in 2123", fontsize=18, weight='bold', pad=20)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Solar Power Generation (Gigawatts)", fontsize=14)

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Customize plot appearance
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 301, 50))

# Ensure layout is tight and elements are not clipped
plt.tight_layout()

# Display the area chart
plt.show()