import matplotlib.pyplot as plt
import numpy as np

# Key trading cities in Eldoria
cities = ['Aramoor', 'Braavos', 'Evendale', 'Galewatch', 'Highreach']

# Data: Number of successful caravans reaching each city over a 10-year period
caravans_data = {
    'Aramoor': [150, 160, 145, 175, 180, 165, 170, 160, 155, 165],
    'Braavos': [140, 135, 150, 145, 155, 150, 140, 130, 135, 140],
    'Evendale': [160, 170, 165, 180, 185, 175, 170, 165, 160, 175],
    'Galewatch': [120, 130, 125, 135, 130, 125, 120, 115, 125, 130],
    'Highreach': [100, 110, 105, 115, 110, 100, 105, 110, 115, 120]
}

# Years for the x-axis
years = list(range(1010, 1020))

# Create the figure and set up a 1x2 subplot layout
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

# Data preparation for the box plot
box_data = [caravans_data[city] for city in cities]

# First subplot: Box plot
ax1 = axes[0]
bp = ax1.boxplot(box_data, patch_artist=True, labels=cities, notch=True, medianprops=dict(color='black', linewidth=2))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for whisker, cap in zip(bp['whiskers'], bp['caps']):
    whisker.set(color='gray', linewidth=1.5)
    cap.set(color='gray', linewidth=1.5)

ax1.set_title("Trade Stability in Eldoria:\nA Decade of Successful Caravans (1010-1019)", fontsize=14, weight='bold')
ax1.set_xlabel("Trading Cities", fontsize=12)
ax1.set_ylabel("Successful Caravans (per year)", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Second subplot: Line chart for trends over the years
ax2 = axes[1]
for city, color in zip(cities, colors):
    ax2.plot(years, caravans_data[city], label=city, marker='o', linestyle='-', linewidth=2, color=color)

ax2.set_title("Yearly Trends of Successful Caravans", fontsize=14, weight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Successful Caravans (per year)", fontsize=12)
ax2.legend(title="Cities", loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()