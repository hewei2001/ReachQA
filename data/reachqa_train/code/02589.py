import numpy as np
import matplotlib.pyplot as plt

# Years of observation
years = np.arange(2000, 2021)

# Population data in thousands
dolphin_population = [30, 32, 34, 36, 38, 40, 42, 45, 48, 50, 52, 55, 58, 61, 65, 68, 70, 72, 75, 78, 80]
sea_turtle_population = [20, 22, 21, 23, 24, 26, 27, 28, 30, 31, 33, 35, 36, 37, 39, 40, 42, 44, 45, 47, 50]
coral_reef_fish_population = [100, 105, 108, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 162, 165, 167, 170, 172, 175, 177, 180]
jellyfish_population = [15, 18, 20, 22, 23, 25, 27, 30, 33, 36, 38, 40, 43, 45, 47, 49, 50, 52, 53, 55, 58]
shark_population = [8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 16, 17]

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the area chart
ax.fill_between(years, 0, dolphin_population, color='#1f77b4', alpha=0.7, label='Dolphins')
ax.fill_between(years, dolphin_population, np.add(dolphin_population, sea_turtle_population), color='#ff7f0e', alpha=0.7, label='Sea Turtles')
ax.fill_between(years, np.add(dolphin_population, sea_turtle_population), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), color='#2ca02c', alpha=0.7, label='Coral Reef Fish')
ax.fill_between(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population]), color='#d62728', alpha=0.7, label='Jellyfish')
ax.fill_between(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population]), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population, shark_population]), color='#9467bd', alpha=0.7, label='Sharks')

# Set title and labels
ax.set_title("Marine Biodiversity in Coral Bay: Population Trends Over Two Decades", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Population (in thousands)", fontsize=12)

# Configure x-axis ticks
plt.xticks(years, rotation=45, ha="right")

# Add legend
ax.legend(loc='upper left', title='Species')

# Improve readability with grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Adjust layout to avoid clipping
plt.tight_layout()

# Display the plot
plt.show()