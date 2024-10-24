import matplotlib.pyplot as plt
import numpy as np

# Data setup
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

contributions = np.array([
    [320, 220, 180, 370],  # North America
    [270, 310, 150, 420],  # Europe
    [410, 260, 200, 310],  # Asia
    [160, 110, 100, 110],  # Africa
    [190, 160, 110, 160]   # South America
])

# Total contributions for each sector across all regions
total_contributions = contributions.sum(axis=0)

# Time-series data for each sector's growth over 5 years
years = np.arange(2019, 2024)
growth = np.array([
    [1.0, 1.05, 1.10, 1.12, 1.15],
    [1.0, 1.03, 1.07, 1.11, 1.16],
    [1.0, 1.04, 1.08, 1.10, 1.14],
    [1.0, 1.06, 1.09, 1.13, 1.18]
])
annual_growth = (contributions.sum(axis=0)[:, np.newaxis] * growth).T

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# Stacked Bar Chart
ax1 = axes[0]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
bottom = np.zeros(len(regions))

for i, sector in enumerate(sectors):
    ax1.bar(regions, contributions[:, i], label=sector, color=colors[i], alpha=0.85, bottom=bottom)
    bottom += contributions[:, i]

ax1.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax1.set_title('Annual Contributions to Global Conservation Efforts\nby Region and Sector', 
              fontsize=14, fontweight='bold', pad=15)
ax1.legend(title='Conservation Sectors', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
ax1.set_xticks(np.arange(len(regions)))
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Line Chart for Yearly Growth
ax2 = axes[1]
for i, sector in enumerate(sectors):
    ax2.plot(years, annual_growth[:, i], marker='o', label=sector, color=colors[i])

ax2.set_ylabel('Annual Contributions (in million $)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_title('Projected Sector Growth (2019-2023)', fontsize=14, fontweight='bold', pad=15)
ax2.legend(title='Conservation Sectors', fontsize=10)
ax2.set_xticks(years)
ax2.set_xlim(years.min(), years.max())
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure nothing overlaps
plt.tight_layout()
plt.show()