import matplotlib.pyplot as plt
import numpy as np

# Original data
years = np.arange(2014, 2024)
sustainable_usage = np.array([10, 15, 18, 22, 27, 32, 36, 41, 47, 53])
standard_deviation = np.array([2, 3, 2, 4, 3, 3, 4, 3, 3, 4])

# Related data for stacked bar chart
# Assume contributions from different materials (Organic Cotton, Recycled Polyester, Hemp) over the years
organic_cotton = np.array([2, 3, 3, 4, 5, 6, 7, 8, 9, 10])
recycled_polyester = np.array([3, 5, 7, 8, 10, 11, 12, 13, 14, 15])
hemp = sustainable_usage - organic_cotton - recycled_polyester

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# First subplot: Line chart with error bars
ax1.errorbar(years, sustainable_usage, yerr=standard_deviation, fmt='o-', color='#2c7fb8',
             ecolor='#a6bddb', elinewidth=2, capsize=4, label='Sustainable Material Usage')
milestones = {
    2015: "Intro: Organic Cotton",
    2018: "Shift to Recycled Polyester",
    2021: "Hemp Utilization Tripled"
}
for year, milestone in milestones.items():
    ax1.annotate(milestone,
                 (year, sustainable_usage[years == year]),
                 textcoords="offset points",
                 xytext=(0, 15),
                 ha='center',
                 fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray'))

ax1.set_title("EcoChic's Sustainable Material Usage\nOver a Decade (2014-2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sustainable Material Usage (%)", fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 60, 5))
ax1.legend(loc='upper left', fontsize=10)

# Second subplot: Stacked bar chart
ax2.bar(years, organic_cotton, label='Organic Cotton', color='#66c2a5')
ax2.bar(years, recycled_polyester, bottom=organic_cotton, label='Recycled Polyester', color='#fc8d62')
ax2.bar(years, hemp, bottom=organic_cotton + recycled_polyester, label='Hemp', color='#8da0cb')

ax2.set_title("Material Contribution Breakdown\n(2014-2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Usage Contribution (%)", fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 60, 5))
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plots
plt.show()