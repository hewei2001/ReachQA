import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(1990, 2021, 5)

# Hypothetical data: percentage of the commuting population using each mode
electric_vehicles = np.array([1, 2, 5, 10, 15, 20, 25])
bicycles = np.array([5, 7, 10, 15, 17, 20, 23])
public_transit = np.array([20, 25, 27, 28, 30, 33, 35])
walking = np.array([10, 12, 13, 14, 16, 18, 20])

# Stack the data for plotting
data = np.vstack([electric_vehicles, bicycles, public_transit, walking])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked areas
ax.stackplot(years, data, labels=["Electric Vehicles", "Bicycles", "Public Transit", "Walking"],
             colors=['#69b3a2', '#404080', '#f4a582', '#fed9a6'], alpha=0.8)

# Add title and labels
ax.set_title("Journey to a Greener Future:\nEvolution of Eco-Friendly Transportation Modes (1990-2020)",
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Total Commuting Population", fontsize=12)

# Customize x-ticks and y-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.set_yticks(np.arange(0, 101, 10))

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend with a clear title
ax.legend(loc='upper left', fontsize=10, title='Transportation Mode', title_fontsize='12')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()