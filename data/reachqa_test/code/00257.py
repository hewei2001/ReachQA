import matplotlib.pyplot as plt
import numpy as np

# Define the decades from 1960 to 2020
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Hypothetical data for spice usage in metric tons
turmeric_usage = np.array([5, 10, 18, 25, 35, 50, 70])
cumin_usage = np.array([8, 12, 20, 30, 45, 55, 60])
paprika_usage = np.array([4, 8, 15, 20, 25, 30, 35])
cinnamon_usage = np.array([3, 5, 10, 15, 25, 35, 45])

# Calculate spice usage proportions as a percentage of total usage for new plot
total_usage = turmeric_usage + cumin_usage + paprika_usage + cinnamon_usage
turmeric_percentage = (turmeric_usage / total_usage) * 100
cumin_percentage = (cumin_usage / total_usage) * 100
paprika_percentage = (paprika_usage / total_usage) * 100
cinnamon_percentage = (cinnamon_usage / total_usage) * 100

# Create figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the stacked area chart on the first subplot
axes[0].stackplot(decades, turmeric_usage, cumin_usage, paprika_usage, cinnamon_usage, 
                  labels=["Turmeric", "Cumin", "Paprika", "Cinnamon"], colors=['#FFD700', '#FFA500', '#FF4500', '#8B4513'], alpha=0.8)
axes[0].set_title("Evolving Culinary Trends: Global Spice Usage\nAcross Decades (1960-2020)", fontsize=14, fontweight='bold', pad=15)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Spice Usage (Metric Tons)', fontsize=12)
axes[0].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].legend(loc='upper left', title="Spices", fontsize=10)

# Plotting the line chart of spice usage proportions on the second subplot
axes[1].plot(decades, turmeric_percentage, label="Turmeric", color='#FFD700', marker='o', linestyle='-')
axes[1].plot(decades, cumin_percentage, label="Cumin", color='#FFA500', marker='o', linestyle='-')
axes[1].plot(decades, paprika_percentage, label="Paprika", color='#FF4500', marker='o', linestyle='-')
axes[1].plot(decades, cinnamon_percentage, label="Cinnamon", color='#8B4513', marker='o', linestyle='-')
axes[1].set_title("Spice Usage Proportions Over Time", fontsize=14, fontweight='bold', pad=15)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Spice Usage (%)', fontsize=12)
axes[1].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(loc='upper right', title="Spices", fontsize=10)

# Adjust layout for optimal display
plt.tight_layout()

# Display the chart
plt.show()