import matplotlib.pyplot as plt
import numpy as np

# Define the attributes for the rose chart
attributes = ['Petal Color Intensity', 'Bloom Duration (Days)', 
              'Bioluminescence Level', 'Scent Strength', 'Pollen Production']

# Data for each alien plant species
species = ['Zelvoria', 'Astral Rose', 'Nebula Lily', 'Orion Thistle', 'Celestial Blossom']
data_values = {
    'Zelvoria': [9, 14, 7, 6, 8],
    'Astral Rose': [6, 12, 10, 4, 9],
    'Nebula Lily': [8, 7, 5, 9, 6],
    'Orion Thistle': [7, 8, 9, 10, 5],
    'Celestial Blossom': [5, 10, 8, 6, 7]
}

# Average values for benchmark overlay plot
benchmark_values = [7, 10, 8, 7, 7]

# Number of attributes
num_vars = len(attributes)

# Calculate angles for each variable for the polar plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the plot

# Colors for each species
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Set up the polar plot
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

# Plot each species on the radar chart
for i, (species_name, values) in enumerate(data_values.items()):
    values += values[:1]  # Close the plot
    ax.plot(angles, values, color=colors[i], linewidth=2, linestyle='solid', label=species_name)
    ax.fill(angles, values, color=colors[i], alpha=0.2)

# Overlay plot: Benchmark values using scatter plot
benchmark_values += benchmark_values[:1]
ax.scatter(angles, benchmark_values, color='gold', s=100, edgecolor='black', label='Benchmark')

# Add attributes labels at correct angles
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='darkslategray', wrap=True)

# Enhance grid appearance
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Hide the radial labels
ax.set_yticklabels([])

# Add a title to the chart
plt.title("Cosmic Petals: Exploring Andromeda's\nExtraterrestrial Flora with Benchmark Comparison", 
          size=14, color='darkgreen', pad=20, loc='center')

# Add a legend to the chart
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10, 
           title="Alien Species", title_fontsize=12, frameon=True)

# Automatically adjust the layout to make it more readable
plt.tight_layout()

# Display the enhanced radar chart
plt.show()