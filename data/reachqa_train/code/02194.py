import matplotlib.pyplot as plt
import numpy as np

# Define the sources and their contributions
sources = [
    'Packaging Waste',
    'Fishing Equipment',
    'Textile Fibers',
    'Industrial Discharges',
    'Household Products',
    'Automotive Materials'
]

# Further breakdown into subcategories and regions
subcategories = ['Plastic Bags', 'Bottles', 'Nets', 'Lines', 'Cotton', 'Polyester', 
                 'Chemicals', 'Oils', 'Cleaners', 'Detergents', 'Tires', 'Bumpers']
regions = ['North America', 'Europe', 'Asia']

# Contributions matrix: rows correspond to sources, columns to subcategories
contributions = np.array([
    [2.5, 2.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Packaging Waste
    [0, 0, 2.1, 2.2, 0, 0, 0, 0, 0, 0, 0, 0],  # Fishing Equipment
    [0, 0, 0, 0, 1.2, 2.6, 0, 0, 0, 0, 0, 0],  # Textile Fibers
    [0, 0, 0, 0, 0, 0, 1.0, 1.1, 0, 0, 0, 0],  # Industrial Discharges
    [0, 0, 0, 0, 0, 0, 0, 0, 0.9, 0.8, 0, 0],  # Household Products
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0.6]   # Automotive Materials
])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors
colors = plt.cm.tab20.colors

# Create a stacked bar chart for subcategories
for j in range(contributions.shape[1]):
    ax.barh(sources, contributions[:, j], left=np.sum(contributions[:, :j], axis=1), 
            color=colors[j % len(colors)], label=subcategories[j], edgecolor='black', alpha=0.8)

# Add data labels to the bars
for i, source_contributions in enumerate(contributions):
    cumulative = 0
    for j, value in enumerate(source_contributions):
        if value > 0:
            cumulative += value
            ax.text(cumulative - value / 2, i, f"{value:.1f}", va='center', ha='center', fontsize=8, color='white')

# Set chart title and labels
ax.set_title('Ocean Plastic Waste Distribution by Source and Subcategories in 2023\nAnalyzing Regional Contributions', fontsize=14, fontweight='bold')
ax.set_xlabel('Contribution (Million Metric Tons)', fontsize=12)

# Configure the x-axis and y-axis
ax.set_xlim(0, np.sum(contributions) + 2)
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Add a subtle background
ax.set_facecolor('whitesmoke')

# Adjust layout to prevent overlap
plt.tight_layout()

# Add legend for subcategories
ax.legend(subcategories, title='Subcategories', fontsize=9, title_fontsize='10')

# Add secondary bar chart to showcase regional analysis
fig2, ax2 = plt.subplots(figsize=(12, 4))
regional_contributions = np.array([
    [1.5, 1.6, 1.4],
    [0.9, 0.8, 1.0],
    [0.5, 0.6, 0.6],
    [0.6, 0.4, 1.1],
    [0.3, 0.4, 1.0],
    [0.2, 0.2, 0.8]
])

# Stacked bar chart for regions
for i, region in enumerate(regions):
    ax2.barh(sources, regional_contributions[:, i], left=np.sum(regional_contributions[:, :i], axis=1), 
             color=colors[i+6], label=region, edgecolor='black', alpha=0.85)

ax2.set_title('Regional Plastic Waste Contributions', fontsize=14, fontweight='bold')
ax2.set_xlabel('Contribution (Million Metric Tons)', fontsize=12)

# Add legend for regions
ax2.legend(regions, title='Regions', fontsize=9, title_fontsize='10')

plt.tight_layout()

# Display the plots
plt.show()