import matplotlib.pyplot as plt
import numpy as np

# Data representing annual CO2 emissions (metric tons) for different farming practices
traditional_tilling = [25, 30, 27, 33, 29, 28, 31, 34, 30, 26]
no_till_farming = [20, 18, 22, 19, 21, 17, 23, 24, 19, 20]
organic_farming = [15, 12, 13, 14, 16, 15, 13, 12, 17, 14]
agroforestry = [10, 9, 11, 8, 12, 9, 11, 10, 9, 10]
precision_agriculture = [18, 16, 19, 20, 15, 17, 18, 16, 21, 19]

# Organizing the data into a list for plotting
emission_data = [traditional_tilling, no_till_farming, organic_farming, agroforestry, precision_agriculture]
practices = ['Traditional Tilling', 'No-Till Farming', 'Organic Farming', 'Agroforestry', 'Precision Agriculture']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the horizontal box plot
box = ax.boxplot(emission_data, vert=False, patch_artist=True, labels=practices, notch=True)

# Customize the appearance of the box plot
colors = ['#d62728', '#1f77b4', '#2ca02c', '#9467bd', '#ff7f0e']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")
for cap in box['caps']:
    cap.set(color='gray', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

# Titles and labels
ax.set_title('Annual CO2 Emissions from Various Agricultural Practices\nAssessing Environmental Footprint', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Annual CO2 Emissions (Metric Tons)', fontsize=12)
ax.set_ylabel('Agricultural Practices', fontsize=12)

# Add grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, practices, title='Practices', loc='lower right', fontsize=10, title_fontsize=12, frameon=True)

# Adjust layout for better visualization
plt.tight_layout()

# Display the plot
plt.show()