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
fig, ax = plt.subplots(figsize=(14, 9))

# Colors for each species
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the area chart with enhanced visual elements
ax.fill_between(years, 0, dolphin_population, color=colors[0], alpha=0.7, label='Dolphins', edgecolor='black', linewidth=1.2)
ax.fill_between(years, dolphin_population, np.add(dolphin_population, sea_turtle_population), color=colors[1], alpha=0.7, label='Sea Turtles', edgecolor='black', linewidth=1.2)
ax.fill_between(years, np.add(dolphin_population, sea_turtle_population), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), color=colors[2], alpha=0.7, label='Coral Reef Fish', edgecolor='black', linewidth=1.2)
ax.fill_between(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population]), color=colors[3], alpha=0.7, label='Jellyfish', edgecolor='black', linewidth=1.2)
ax.fill_between(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population]), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population, shark_population]), color=colors[4], alpha=0.7, label='Sharks', edgecolor='black', linewidth=1.2)

# Set title and labels with enhanced styles
ax.set_title("Marine Biodiversity in Coral Bay:\nPopulation Trends Over Two Decades", fontsize=18, fontweight='bold', loc='left', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Population (in thousands)", fontsize=14)

# Add data markers
ax.plot(years, dolphin_population, marker='o', markersize=5, color=colors[0], linestyle='None')
ax.plot(years, np.add(dolphin_population, sea_turtle_population), marker='s', markersize=5, color=colors[1], linestyle='None')
ax.plot(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), marker='^', markersize=5, color=colors[2], linestyle='None')
ax.plot(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population]), marker='d', markersize=5, color=colors[3], linestyle='None')
ax.plot(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population, shark_population]), marker='x', markersize=5, color=colors[4], linestyle='None')

# Add annotations for key points
ax.annotate('Sharks hit max', xy=(2020, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, jellyfish_population, shark_population])[-1]), 
            xytext=(2010, 400), textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Configure x-axis ticks
plt.xticks(years, rotation=45, ha="right")

# Add legend with enhanced style
ax.legend(loc='upper left', title='Species', fontsize=12, title_fontsize='13')

# Improve readability with refined grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Adjust layout to avoid clipping and ensure elements fit well
plt.tight_layout()

# Display the plot
plt.show()