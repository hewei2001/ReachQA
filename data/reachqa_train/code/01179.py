import matplotlib.pyplot as plt
import numpy as np

# Data for the chart: types of green spaces and their area in hectares
categories = ['Parks', 'Gardens', 'Greenways', 'Community Gardens', 'Rooftop Gardens']
area_coverage = [120, 75, 40, 25, 10]  # Area in hectares

# Positions for each category on the x-axis
x_positions = np.arange(len(categories))

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(x_positions, area_coverage, color=['#76c893', '#c9e4c5', '#f0f3bd', '#f4a261', '#e76f51'], width=0.6)

# Annotate each bar with the area covered
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval} ha', ha='center', va='bottom', fontsize=10, weight='bold')

# Customize the plot
ax.set_xlabel('Types of Green Spaces', fontsize=12, weight='bold')
ax.set_ylabel('Area Coverage (hectares)', fontsize=12, weight='bold')
ax.set_title('Urban Green Spaces Distribution\nin Greenfield City', fontsize=14, weight='bold')

# Set the x-ticks to match the categories and adjust rotation for readability
ax.set_xticks(x_positions)
ax.set_xticklabels(categories, rotation=15, ha='right', fontsize=11)

# Add grid lines for better estimation of values
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()