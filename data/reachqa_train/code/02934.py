import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Years from 2003 to 2023
years = np.arange(2003, 2024)

# Generate extended yield data for each magical herb with added complexity
dragon_root_yields = [150 + 2*i + np.sin(i/2)*10 for i in range(len(years))]
fey_blossom_yields = [120 + 1.5*i + np.cos(i/2)*8 for i in range(len(years))]
moonshade_yields = [100 + 1.2*i + np.sin(i/3)*5 for i in range(len(years))]
star_ivy_yields = [80 + 1.1*i + np.cos(i/3)*6 for i in range(len(years))]
phoenix_feather_yields = [50 + 1.3*i + np.sin(i/4)*4 for i in range(len(years))]

# Additional herb for complexity
thunder_fruit_yields = [70 + 1.4*i + np.cos(i/4)*7 for i in range(len(years))]

# Combine the data
data = np.array([dragon_root_yields, fey_blossom_yields, moonshade_yields, star_ivy_yields, phoenix_feather_yields, thunder_fruit_yields])

# Labels for each magical herb
labels = ['Dragon Root', 'Fey Blossom', 'Moonshade', 'Star Ivy', 'Phoenix Feather', 'Thunder Fruit']

# Create subplots for boxplot and trend lines
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Boxplot for yield distribution
bp = axes[0].boxplot(data.T, patch_artist=True, notch=True, vert=True, labels=labels)

# Customize colors for boxplot
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=1.5)

for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=1.5)

for median in bp['medians']:
    median.set(color='black', linewidth=2)

for flier in bp['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# Add grid and labels to boxplot
axes[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axes[0].set_title('Magical Herb Yields Distribution from Eloria (2003-2023)', fontsize=16, fontweight='bold', pad=20)
axes[0].set_ylabel('Yield (kg)', fontsize=14)

# Line plot for trends over time
for idx, herb_yield in enumerate(data):
    axes[1].plot(years, herb_yield, label=labels[idx], color=colors[idx], linewidth=2)

# Calculate and plot trend lines
for idx, herb_yield in enumerate(data):
    z = np.polyfit(years, herb_yield, 1)
    p = np.poly1d(z)
    axes[1].plot(years, p(years), '--', color=colors[idx], linewidth=1.5)

# Add grid, labels, and legend to line plot
axes[1].yaxis.grid(True, linestyle='--', alpha=0.7)
axes[1].set_title('Trends in Magical Herb Yields Over Time (2003-2023)', fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel('Year', fontsize=14)
axes[1].set_ylabel('Yield (kg)', fontsize=14)
axes[1].legend(loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()