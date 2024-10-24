import matplotlib.pyplot as plt
import numpy as np

# Data: Energy consumption in GWh for 100 neighborhoods
energy_consumption = [
    150, 155, 160, 162, 165, 170, 175, 180, 185, 188, 190, 195, 198, 200, 205,
    210, 215, 220, 223, 225, 230, 235, 238, 240, 245, 250, 255, 258, 260, 265,
    270, 275, 278, 280, 285, 290, 295, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450, 460, 470, 480, 490,
    200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270,
    275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345,
    350, 355, 360, 365, 370, 375, 380, 385, 390, 395
]

# Calculate cumulative energy consumption
cumulative_consumption = np.cumsum(np.sort(energy_consumption))

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the histogram
n, bins, patches = ax1.hist(energy_consumption, bins=14, color='mediumseagreen', edgecolor='black', alpha=0.8, label='Histogram')

# Title and labels
plt.title('Energy Consumption Distribution in Ecohaven\nIdentifying High-Use Neighborhoods for 2030 Initiatives', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Energy Consumption (GWh)', fontsize=12)
ax1.set_ylabel('Number of Neighborhoods', fontsize=12)

# Add a second y-axis to the right for cumulative data
ax2 = ax1.twinx()
ax2.plot(np.sort(energy_consumption), cumulative_consumption, color='navy', linestyle='--', linewidth=2, marker='o', markersize=4, label='Cumulative Consumption')
ax2.set_ylabel('Cumulative Consumption (GWh)', fontsize=12)

# Add mean line and annotation
mean_consumption = np.mean(energy_consumption)
ax1.axvline(mean_consumption, color='red', linestyle='-', linewidth=2)
ax1.text(mean_consumption + 5, max(n) * 0.9, f'Mean: {mean_consumption:.2f} GWh', color='red', fontsize=10)

# Customize the plot's appearance
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(bins)
ax1.set_yticks(np.arange(0, max(n) + 1, 5))
ax1.tick_params(axis='x', rotation=45)

# Add legend
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85))

# Adjust layout to prevent overlapping text
fig.tight_layout()

# Display the plot
plt.show()