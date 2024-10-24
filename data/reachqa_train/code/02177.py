import matplotlib.pyplot as plt
import numpy as np

# Define Tech Sectors and the number of Start-Ups in each
tech_sectors = ['FinTech', 'HealthTech', 'EdTech', 'AgriTech', 'CleanTech']
start_ups = [150, 90, 120, 60, 110]

# Related data: hypothetical growth rates for each sector
growth_rates = [12, 8, 10, 5, 7]  # Percentage growth rates

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Create the bar chart
bars = ax1.bar(np.arange(len(tech_sectors)), start_ups, color=colors, edgecolor='black', alpha=0.8, label='Number of Start-Ups')

# Title and axis labels
ax1.set_title("Silicon Valley's Tech Sector Boom:\nStart-Up Distribution and Growth Rates Over the Past Year", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Tech Sectors", fontsize=12)
ax1.set_ylabel("Number of Start-Ups", fontsize=12, color='black')

# Set x-ticks and labels, with rotation for clarity
ax1.set_xticks(np.arange(len(tech_sectors)))
ax1.set_xticklabels(tech_sectors, fontsize=10, rotation=25)

# Add value labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 5, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Add horizontal grid lines only on y-axis for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Set up secondary axis for growth rate
ax2 = ax1.twinx()
ax2.set_ylabel("Growth Rate (%)", fontsize=12, color='seagreen')

# Create the line plot for growth rates
line = ax2.plot(np.arange(len(tech_sectors)), growth_rates, color='seagreen', marker='o', markersize=8, linestyle='-', linewidth=2, label='Growth Rate (%)')

# Annotate growth rates above markers
for i, growth in enumerate(growth_rates):
    ax2.text(i, growth + 0.5, f"{growth}%", ha='center', va='bottom', fontsize=10, fontweight='bold', color='seagreen')

# Add legend for clarity
fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes, fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()