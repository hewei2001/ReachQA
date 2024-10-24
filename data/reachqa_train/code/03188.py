import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2014, 2024)
sustainable_usage = np.array([10, 15, 18, 22, 27, 32, 36, 41, 47, 53])
standard_deviation = np.array([2, 3, 2, 4, 3, 3, 4, 3, 3, 4])

# Create the line chart with error bars
plt.figure(figsize=(12, 6))
plt.errorbar(years, sustainable_usage, yerr=standard_deviation, fmt='o-', color='#2c7fb8',
             ecolor='#a6bddb', elinewidth=2, capsize=4, label='Sustainable Material Usage')

# Adding significant milestones
milestones = {
    2015: "Intro: Organic Cotton",
    2018: "Shift to Recycled Polyester",
    2021: "Hemp Utilization Tripled"
}

for year, milestone in milestones.items():
    plt.annotate(milestone,
                 (year, sustainable_usage[years == year]),
                 textcoords="offset points",
                 xytext=(0, 15),
                 ha='center',
                 fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray'))

# Plot enhancements
plt.title("EcoChic's Sustainable Material Usage Over a Decade\n(2014-2023)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Sustainable Material Usage (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years)
plt.yticks(np.arange(0, 60, 5))
plt.legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()