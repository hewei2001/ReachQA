import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(1990, 2021, 5)

# Hypothetical data: percentage of the commuting population using each mode
electric_vehicles = np.array([1, 2, 5, 10, 15, 20, 25])
bicycles = np.array([5, 7, 10, 15, 17, 20, 23])
public_transit = np.array([20, 25, 27, 28, 30, 33, 35])
walking = np.array([10, 12, 13, 14, 16, 18, 20])

# Calculate annual growth percentage for each mode
growth_electric_vehicles = np.diff(electric_vehicles, prepend=0) / electric_vehicles * 100
growth_bicycles = np.diff(bicycles, prepend=0) / bicycles * 100
growth_public_transit = np.diff(public_transit, prepend=0) / public_transit * 100
growth_walking = np.diff(walking, prepend=0) / walking * 100

# Create a 1x2 grid of subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Stacked area plot
axes[0].stackplot(years, electric_vehicles, bicycles, public_transit, walking,
                  labels=["Electric Vehicles", "Bicycles", "Public Transit", "Walking"],
                  colors=['#69b3a2', '#404080', '#f4a582', '#fed9a6'], alpha=0.8)
axes[0].set_title("Journey to a Greener Future:\nEvolution of Eco-Friendly Transportation Modes (1990-2020)",
                  fontsize=16, fontweight='bold', pad=15)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Percentage of Total Commuting Population", fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45, fontsize=10)
axes[0].set_yticks(np.arange(0, 101, 10))
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend(loc='upper left', fontsize=10, title='Transportation Mode', title_fontsize='12')

# Line plot for growth percentages
axes[1].plot(years, growth_electric_vehicles, marker='o', label="Electric Vehicles", color='#69b3a2')
axes[1].plot(years, growth_bicycles, marker='o', label="Bicycles", color='#404080')
axes[1].plot(years, growth_public_transit, marker='o', label="Public Transit", color='#f4a582')
axes[1].plot(years, growth_walking, marker='o', label="Walking", color='#fed9a6')
axes[1].set_title("Growth Rate of Eco-Friendly Transportation Modes\n(Annual Percentage Change)",
                  fontsize=16, fontweight='bold', pad=15)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Growth Rate (%)", fontsize=12)
axes[1].set_xticks(years)
axes[1].set_xticklabels(years, rotation=45, fontsize=10)
axes[1].legend(loc='upper left', fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()