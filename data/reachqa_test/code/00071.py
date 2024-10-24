import matplotlib.pyplot as plt
import numpy as np

# Define tech cities and the corresponding artificial coffee consumption data
cities = ['San Francisco', 'New York', 'Austin', 'Seattle', 'Berlin']
coffee_consumption = [
    [3, 4, 3.5, 5, 4.5, 3, 6, 2.5, 3.5, 4],   # San Francisco
    [5, 5.5, 4, 6, 6.5, 7, 3.5, 4, 5, 4.5],   # New York
    [3, 3.5, 2.5, 4, 3, 3.5, 4, 2, 3, 2.5],   # Austin
    [4.5, 5, 4.5, 5.5, 5, 4, 5, 4.5, 5.5, 6], # Seattle
    [4, 4.5, 3.5, 4, 5, 4, 4.5, 3.5, 4, 3]    # Berlin
]

# Calculate monthly average consumption for the overlay line plot
monthly_avg_consumption = [np.mean(data) for data in coffee_consumption]

# Create a figure and axis for the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create the box plot with custom styling
box = ax.boxplot(coffee_consumption, vert=False, patch_artist=True,
                 notch=True, whis=1.5, widths=0.5,
                 boxprops=dict(facecolor='#AEC6CF', color='black'),
                 whiskerprops=dict(color='darkgrey', linewidth=2),
                 capprops=dict(color='black', linewidth=2),
                 medianprops=dict(color='#FF6347', linewidth=2))

# Customize individual box colors for better distinction
colors = ['#FFDDC1', '#F0E68C', '#98FB98', '#87CEFA', '#FFB6C1']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Overlay line plot representing monthly average consumption
ax.plot(monthly_avg_consumption, range(1, len(cities) + 1), marker='o', linestyle='--', color='navy', label='Monthly Avg Consumption')

# Set y-axis labels
ax.set_yticks(range(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=11)

# Title and labels
ax.set_title('Caffeine Pulse:\nCoffee Consumption Trends in Tech Hubs - 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Daily Coffee Consumption (Cups)', fontsize=12)
ax.set_ylabel('Tech Cities', fontsize=12)

# Add grid lines for reference
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add legend for overlay plot
ax.legend(loc='upper right', fontsize=11)

# Adjust layout to avoid text overlapping
plt.tight_layout()

# Display the plot
plt.show()