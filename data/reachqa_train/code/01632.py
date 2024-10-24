import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Define the years
years = np.arange(2015, 2026)

# Define the number of EVs in thousands for each region over the years
north_america = np.array([100, 150, 230, 330, 450, 580, 730, 890, 1070, 1260, 1460])
europe = np.array([80, 120, 200, 290, 410, 550, 720, 900, 1100, 1310, 1530])
asia = np.array([60, 90, 170, 270, 390, 530, 690, 870, 1070, 1290, 1520])
other_regions = np.array([20, 35, 60, 95, 140, 200, 280, 380, 500, 640, 800])

# Stack the data for the area plot
data = np.vstack([north_america, europe, asia, other_regions])

# Calculate total EVs and market share for the line plot
total_evs = north_america + europe + asia + other_regions
market_share = (data / total_evs) * 100

# Create a figure with subplots
fig = plt.figure(figsize=(16, 8))
gs = GridSpec(1, 2, figure=fig)

# Subplot 1: Stacked Area Chart
ax1 = fig.add_subplot(gs[0, 0])
ax1.stackplot(years, data, labels=['North America', 'Europe', 'Asia', 'Other Regions'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)
ax1.set_title('Growth of Electric Vehicle Adoption by Region\nfrom 2015 to 2025', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Electric Vehicles (in thousands)', fontsize=12)
ax1.legend(loc='upper left', title='Regions', fontsize=10, bbox_to_anchor=(1, 1))
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Subplot 2: Line Chart for Market Share
ax2 = fig.add_subplot(gs[0, 1], sharex=ax1)
for i, region in enumerate(['North America', 'Europe', 'Asia', 'Other Regions']):
    ax2.plot(years, market_share[i], label=region, marker='o', linestyle='-', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'][i])
ax2.set_title('Regional Market Share in Global EV Adoption\n2015 to 2025', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Market Share (%)', fontsize=12)
ax2.legend(loc='upper left', title='Regions', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure proper display
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()