import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their tallest building heights in meters
cities = ['New York', 'Dubai', 'Shanghai', 'London', 'Tokyo', 'Kuala Lumpur', 'Sydney']
heights = [450, 830, 632, 310, 634, 452, 309]

# Color palette for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the vertical bar chart
bars = ax.bar(cities, heights, color=colors, edgecolor='black', width=0.6)

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 15, f'{height} m', 
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Customize the appearance
ax.set_xlabel('City', fontsize=12, fontweight='bold')
ax.set_ylabel('Height (m)', fontsize=12, fontweight='bold')
ax.set_title('Battle of the Skyscrapers:\nTallest Buildings by City in 2023', fontsize=16, fontweight='bold')
ax.set_ylim(0, max(heights) + 100)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Enhance x-axis labels to prevent overlap
ax.set_xticklabels(cities, fontsize=11, weight='bold', rotation=45, ha='right')

# Add a legend
ax.legend(['Height of Tallest Building'], loc='upper left', fontsize=10, frameon=False)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()