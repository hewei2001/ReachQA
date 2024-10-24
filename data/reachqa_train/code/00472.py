import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.array([2021, 2022, 2023, 2024, 2025])

# Entertainment industry sectors
sectors = ["Gaming", "Cinematic Experiences", "Live Events", "Education & Training"]

# Investment data for each sector (in millions)
investments = np.array([
    [100, 150, 210, 260, 310],  # Gaming
    [80, 110, 140, 170, 200],   # Cinematic Experiences
    [40, 60, 90, 120, 150],     # Live Events
    [30, 50, 80, 110, 140]      # Education & Training
])

# Setup figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width and position index for the x-axis
bar_width = 0.2
x_indices = np.arange(len(years))

# Define colors for each sector's bars
colors = ['dodgerblue', 'orangered', 'forestgreen', 'violet']

# Plot the data for each sector
for idx, sector in enumerate(sectors):
    ax.bar(x_indices + idx * bar_width, investments[idx], width=bar_width, label=sector, color=colors[idx])

# Adding labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Investment (in millions $)', fontsize=12)
ax.set_title('Annual VR Investments by Entertainment Sector (2021-2025)', fontsize=14, fontweight='bold')

# Adjust x-axis ticks and labels
ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(years)

# Add value labels on top of each bar
for i in range(len(years)):
    for j in range(len(sectors)):
        ax.text(i + j * bar_width, investments[j][i] + 5, str(investments[j][i]), ha='center', va='bottom')

# Add a legend to the plot
ax.legend(title='Sectors', loc='upper left')

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for the best fit
plt.tight_layout()

# Display the plot
plt.show()