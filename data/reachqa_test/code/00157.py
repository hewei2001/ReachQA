import matplotlib.pyplot as plt
import numpy as np

# List of leading fashion brands
brands = [
    "EcoChic", 
    "GreenWear", 
    "SustainableStyle", 
    "EarthThreads", 
    "ConsciousCouture"
]

# Adoption rates (%) of eco-friendly materials by these brands
organic_cotton = [65, 70, 55, 60, 75]
recycled_polyester = [40, 50, 35, 45, 60]
bamboo_fabric = [25, 30, 20, 15, 40]

# Hypothetical eco-friendliness index scores over the last few years
eco_index_scores = [72, 85, 78, 80, 90]

# Set up the positions and width for the bars
bar_width = 0.25
r1 = np.arange(len(brands))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create the bar chart
bars1 = ax1.bar(r1, organic_cotton, width=bar_width, color='forestgreen', edgecolor='black', label='Organic Cotton')
bars2 = ax1.bar(r2, recycled_polyester, width=bar_width, color='royalblue', edgecolor='black', label='Recycled Polyester')
bars3 = ax1.bar(r3, bamboo_fabric, width=bar_width, color='darkgoldenrod', edgecolor='black', label='Bamboo Fabric')

# Annotate bar chart
for bars, data in zip([bars1, bars2, bars3], [organic_cotton, recycled_polyester, bamboo_fabric]):
    for bar, v in zip(bars, data):
        ax1.text(bar.get_x() + bar.get_width() / 2, v + 1, f"{v}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the primary y-axis (for the bar chart)
ax1.set_xlabel("Fashion Brands", fontsize=14)
ax1.set_ylabel("Adoption Rate (%)", fontsize=14)
ax1.set_xticks([r + bar_width for r in range(len(brands))])
ax1.set_xticklabels(brands, rotation=45, ha='right')
ax1.set_ylim(0, 80)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Create a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(r1 + bar_width, eco_index_scores, color='darkred', marker='o', linestyle='-', linewidth=2, markersize=8, label='Eco-Friendliness Index')
ax2.set_ylabel("Eco-Friendliness Index", fontsize=14, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')
ax2.set_ylim(60, 100)

# Annotate line plot
for i, v in enumerate(eco_index_scores):
    ax2.text(r1[i] + bar_width, v - 3, f"{v}", ha='center', va='bottom', fontsize=10, color='darkred', fontweight='bold')

# Title and Legend
plt.title("Sustainable Fashion Trends:\nThe Rise of Eco-Friendly Materials and Index Scores in 2023", fontsize=16, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), bbox_transform=ax1.transAxes, fontsize=12)

# Adjust layout
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()