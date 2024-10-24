import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

# Data representing customer acquisition in various regions using different strategies
customer_acquisition_data = np.array([
    [150, 80, 60, 100, 90],   # North America
    [120, 95, 55, 90, 70],    # Europe
    [180, 75, 70, 130, 100],  # Asia
    [100, 85, 50, 80, 65],    # South America
    [70, 60, 40, 65, 55],     # Africa
    [130, 90, 45, 110, 80]    # Australia
])

regions = ["North America", "Europe", "Asia", "South America", "Africa", "Australia"]
strategies = ["Social Media", "TV Ads", "Email", "Search Engine", "Billboards"]

# Create a custom colormap
colors = ["#f7fbff", "#6baed6", "#2171b5"]
cmap = LinearSegmentedColormap.from_list("CustomBlue", colors, N=100)

# Normalize data for percentage-based heatmap
normalized_data = customer_acquisition_data / customer_acquisition_data.sum(axis=1, keepdims=True) * 100

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))
cax = ax.imshow(normalized_data, cmap=cmap, aspect='auto')

# Add titles and labels
ax.set_title("Regional Effectiveness of Marketing Strategies\n(Customer Acquisition as a Percentage of Total Regional Acquisition)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Marketing Strategies", fontsize=12)
ax.set_ylabel("Regions", fontsize=12)

# Set x and y ticks
ax.set_xticks(np.arange(len(strategies)))
ax.set_yticks(np.arange(len(regions)))

# Label the ticks with the respective list entries
ax.set_xticklabels(strategies)
ax.set_yticklabels(regions)

# Rotate the tick labels and set alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations with dynamic color
for i in range(len(regions)):
    for j in range(len(strategies)):
        value = normalized_data[i, j]
        color = "white" if value > 50 else "black"  # Dynamic text color based on value
        text = ax.text(j, i, f"{value:.1f}%", ha="center", va="center", color=color)

# Add a color bar with label
cbar = ax.figure.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label("Percentage of New Customers", fontsize=12)

# Add gridlines
ax.grid(which="major", color='gray', linestyle='--', linewidth=0.5)

# Add a secondary plot (bar chart) showing total customers acquired by each strategy
total_acquisition = customer_acquisition_data.sum(axis=0)
fig, ax2 = plt.subplots(figsize=(6, 4))
bars = ax2.bar(strategies, total_acquisition, color=sns.color_palette("husl", len(strategies)))

ax2.set_title("Total Customer Acquisition by Strategy", fontsize=14, fontweight='bold')
ax2.set_ylabel("Number of New Customers", fontsize=12)
ax2.set_xlabel("Marketing Strategies", fontsize=12)
ax2.set_xticklabels(strategies, rotation=45, ha='right')

# Add text annotations on the bars
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{bar.get_height()}', ha='center', va='bottom', color='black', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()