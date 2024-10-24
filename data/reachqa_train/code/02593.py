import matplotlib.pyplot as plt
import numpy as np

# Define the regions and material types
regions = ['North America', 'Europe', 'Asia']
material_types = ['Leather', 'Synthetic', 'Textiles', 'Rubber', 'Others']

# Market share percentages for each material type by region
market_shares = np.array([
    [30, 25, 20, 15, 10],  # North America
    [25, 30, 15, 20, 10],  # Europe
    [20, 35, 25, 10, 10]   # Asia
])

# Set positions for each region
x = np.arange(len(regions))
bottoms = np.zeros(len(regions))

# Define colors for different materials
colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot each layer of the stacked bar
for idx, (material, color) in enumerate(zip(material_types, colors)):
    ax.bar(x, market_shares[:, idx], bottom=bottoms, label=material, color=color, alpha=0.85)
    bottoms += market_shares[:, idx]

# Add title and labels
ax.set_title('Global Footwear Market Share\nby Material Type (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(regions, rotation=45, ha='right')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)

# Add legend
ax.legend(title='Material Types', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Add percentage labels inside the bars
for region_idx, region_share in enumerate(market_shares):
    y_offset = 0
    for share_idx, share in enumerate(region_share):
        ax.text(region_idx, y_offset + share/2, f"{share}%", ha='center', va='center', fontsize=10, color='white')
        y_offset += share

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()