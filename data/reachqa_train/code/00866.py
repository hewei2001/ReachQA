import matplotlib.pyplot as plt
import numpy as np

# Define the expanded categories
categories = [
    'Soil Health', 'Water Usage', 'Biodiversity', 'Carbon Footprint',
    'Crop Yield', 'Economic Viability', 'Energy Consumption', 'Pesticide Use'
]

# Extend the data with additional farming practices and categories
traditional_farming = [6, 4, 5, 3, 7, 5, 4, 6]
organic_farming = [8, 6, 8, 5, 6, 7, 3, 7]
precision_agriculture = [9, 7, 9, 4, 8, 8, 5, 6]
hydroponics = [5, 3, 6, 2, 9, 4, 7, 5]
agroforestry = [7, 5, 8, 6, 5, 9, 6, 4]

# Convert data to numpy arrays and prepare for plotting
values = np.array([
    traditional_farming, organic_farming, precision_agriculture,
    hydroponics, agroforestry
])
num_vars = len(categories)

# Calculate angles for the radar chart (one extra angle to close the plot)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Append first value to each data set to close the radar plots
values = np.concatenate((values, values[:, [0]]), axis=1)

# Create a radar chart figure
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each practice's data with distinct styles
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
labels = [
    'Traditional Farming', 'Organic Farming', 'Precision Agriculture',
    'Hydroponics', 'Agroforestry'
]
line_styles = ['-', '--', '-.', ':', '-']

for value, color, label, line_style in zip(values, colors, labels, line_styles):
    ax.fill(angles, value, color=color, alpha=0.25)
    ax.plot(angles, value, color=color, linewidth=2, linestyle=line_style, label=label)

# Customize the radar chart
ax.set_yticklabels([])  # Hide the radial ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, weight='bold', ha='center')

# Title and legend
plt.title(
    "Sustainability Performance\nof Agricultural Practices",
    size=15, weight='bold', va='top', y=1.1
)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Show the radar chart
plt.show()