import matplotlib.pyplot as plt
import numpy as np

# Define plant families and their percentage distribution
plant_families = ['Fagaceae', 'Pinaceae', 'Fabaceae', 'Poaceae', 'Asteraceae']
percentage_distribution = [30, 25, 20, 15, 10]  # Total sum equals 100%

# Calculate the cumulative sum for stacking bars
cumulative_percentage = np.cumsum(percentage_distribution)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for each family segment
colors = ['#8FBC8F', '#2E8B57', '#66CDAA', '#3CB371', '#20B2AA']

# Plot each segment in the horizontal stacked bar chart
for i, family in enumerate(plant_families):
    start = cumulative_percentage[i] - percentage_distribution[i]
    ax.barh(0, percentage_distribution[i], left=start, color=colors[i], edgecolor='black', label=family)
    # Annotate with percentage labels
    ax.text(start + percentage_distribution[i]/2, 0, f'{percentage_distribution[i]}%', 
            va='center', ha='center', color='white', weight='bold')

# Customize the chart
ax.set_xlim(0, 100)
ax.set_yticks([])  # No y-axis ticks needed for a single category
ax.set_xlabel('Percentage Distribution (%)', fontsize=12)
ax.set_title('Distribution of Plant Species in a\nBiodiversity Study', fontsize=14, weight='bold')

# Add a legend
ax.legend(title='Plant Families', loc='upper center', bbox_to_anchor=(0.5, -0.15), 
          ncol=len(plant_families), fontsize=10, frameon=False)

# Grid configuration
ax.grid(False)  # Disable the grid for a cleaner look

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()