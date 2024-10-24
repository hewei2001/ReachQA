import matplotlib.pyplot as plt
import numpy as np

# Years for the timeline
years = np.arange(2013, 2024)

# Hypothetical sales data (in thousands) for each company
vrtech_sales = np.array([5, 8, 12, 20, 30, 45, 70, 100, 130, 160, 200])
realscene_sales = np.array([3, 7, 10, 18, 25, 40, 60, 85, 115, 145, 180])
immersify_sales = np.array([2, 6, 9, 16, 22, 35, 55, 78, 105, 140, 170])

# Calculate market shares based on sales
total_sales = vrtech_sales + realscene_sales + immersify_sales
vrtech_market_share = (vrtech_sales / total_sales) * 100
realscene_market_share = (realscene_sales / total_sales) * 100
immersify_market_share = (immersify_sales / total_sales) * 100

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Line plot for sales data
ax1.plot(years, vrtech_sales, label='VRTech', color='steelblue', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, realscene_sales, label='RealScene', color='darkorange', marker='s', linestyle='--', linewidth=2)
ax1.plot(years, immersify_sales, label='Immersify', color='green', marker='^', linestyle='-.', linewidth=2)

# Annotate significant milestones
ax1.annotate('VRTech Breakthrough', xy=(2017, 30), xytext=(2015, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkblue')
ax1.annotate('RealScene 4K Intro', xy=(2019, 85), xytext=(2017, 95),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkorange')
ax1.annotate('Immersify Growth', xy=(2021, 105), xytext=(2019, 120),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkgreen')

# Titles and labels for the line plot
ax1.set_title('VR Technology Adoption\nGrowth in Sales (2013-2023)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales (in thousands)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10, title='Companies', frameon=False)

# Bar plot for market share data
bar_width = 0.25
indices = np.arange(len(years))

ax2.bar(indices, vrtech_market_share, width=bar_width, label='VRTech', color='steelblue')
ax2.bar(indices + bar_width, realscene_market_share, width=bar_width, label='RealScene', color='darkorange')
ax2.bar(indices + 2*bar_width, immersify_market_share, width=bar_width, label='Immersify', color='green')

# Titles and labels for the bar plot
ax2.set_title('Market Share Distribution\n(2013-2023)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Market Share (%)', fontsize=12)
ax2.set_xticks(indices + bar_width)
ax2.set_xticklabels(years, rotation=45)
ax2.grid(True, linestyle='--', alpha=0.5, axis='y')
ax2.legend(loc='upper right', fontsize=10, title='Market Share', frameon=False)

# Automatically adjust layout
plt.tight_layout()
plt.show()