import matplotlib.pyplot as plt
import numpy as np

# Define the categories and corresponding data for each farming practice
categories = ['Soil Health', 'Water Usage', 'Biodiversity', 'Carbon Footprint', 'Crop Yield']
traditional_farming = [6, 4, 5, 3, 7]
organic_farming = [8, 6, 8, 5, 6]
precision_agriculture = [9, 7, 9, 4, 8]

# Convert data to numpy arrays and prepare for plotting
values = np.array([traditional_farming, organic_farming, precision_agriculture])
num_vars = len(categories)

# Calculate angles for the radar chart (one extra angle to close the plot)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Append first value to each data set to close the radar plots
values = np.concatenate((values, values[:, [0]]), axis=1)

# Create a radar chart figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each practice's data
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
labels = ['Traditional Farming', 'Organic Farming', 'Precision Agriculture']

for value, color, label in zip(values, colors, labels):
    ax.fill(angles, value, color=color, alpha=0.25)
    ax.plot(angles, value, color=color, linewidth=2, label=label)

# Customize the radar chart
ax.set_yticklabels([])  # Hide the radial ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, weight='bold', ha='center')

# Title and legend
plt.title("Sustainability Performance of Agricultural Practices", size=15, weight='bold', va='top', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Show the radar chart
plt.show()