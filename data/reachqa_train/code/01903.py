import matplotlib.pyplot as plt
import numpy as np

# Define missions and their budget allocation percentages
missions = [
    'Europa Ice Research',
    'Mars Geodome Colonization',
    'Titan Atmospheric Analysis',
    'Venus Cloud Cities',
    'Asteroid Belt Mining',
    'Jupiter Moons Exploration',
    'Saturn Rings Study',
    'Neptune Core Examination',
    'Mercury Surface Survey',
    'Lunar Water Extraction'
]

# Assign budget allocations, ensuring the sum is 100
budget_allocation = [10.5, 15.5, 7.5, 10, 6, 12, 8, 9, 11, 10.5]

# Define colors for each mission
colors = ['#4caf50', '#2196f3', '#ffeb3b', '#ff5722', '#9c27b0',
          '#3f51b5', '#00bcd4', '#cddc39', '#607d8b', '#e91e63']

# Create the figure and a set of subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle("Planetary Exploration Budget Analysis\nGalactic Federation - 2077", 
             fontsize=18, weight='bold', y=0.95)

# Plot each mission's percentage as a horizontal bar (Main Plot)
axs[0].barh(missions, budget_allocation, color=colors, edgecolor='black')

# Add labels with percentages inside the bars
for i, (bar, percentage) in enumerate(zip(axs[0].patches, budget_allocation)):
    axs[0].text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2,
                f'{percentage:.1f}%', va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Main Plot Customization
axs[0].set_xlim(0, 20)
axs[0].set_xticks(np.arange(0, 21, 5))
axs[0].set_xlabel('Budget Allocation (%)', fontsize=12)
axs[0].set_ylabel('Exploration Missions', fontsize=12)
axs[0].set_title('Current Year Budget Distribution', fontsize=14, weight='bold', pad=10)

# Comparisons of Projected Future Allocations (Second Plot)
future_allocations = [9.5, 16, 8, 9, 6.5, 13, 8.5, 8.5, 12, 9]
axs[1].barh(missions, future_allocations, color=colors, edgecolor='black', alpha=0.7)

# Add labels with percentages inside the bars (Second Plot)
for bar, percentage in zip(axs[1].patches, future_allocations):
    axs[1].text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2,
                f'{percentage:.1f}%', va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Second Plot Customization
axs[1].set_xlim(0, 20)
axs[1].set_xticks(np.arange(0, 21, 5))
axs[1].set_xlabel('Projected Allocation (%)', fontsize=12)
axs[1].set_title('Next Year Budget Forecast', fontsize=14, weight='bold', pad=10)

# Adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the charts
plt.show()