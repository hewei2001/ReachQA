import matplotlib.pyplot as plt
import numpy as np

# Define the regions and years
regions = ['Sub-Saharan Africa', 'South Asia', 'Latin America',
           'East Asia & Pacific', 'Europe & Central Asia']
years = [1950, 1970, 1990, 2010, 2020]

# Literacy rates data (in percentage) for each region over the years
literacy_rates = {
    'Sub-Saharan Africa': [10, 20, 40, 60, 70],
    'South Asia': [20, 35, 55, 70, 80],
    'Latin America': [50, 65, 75, 85, 92],
    'East Asia & Pacific': [40, 60, 75, 90, 95],
    'Europe & Central Asia': [70, 80, 88, 95, 98]
}

# Calculate the growth rates between decades for each region
growth_rates = {}
for region in regions:
    rates = literacy_rates[region]
    growth = [((rates[i] - rates[i-1]) / rates[i-1]) * 100 if i != 0 else 0 for i in range(len(rates))]
    growth_rates[region] = growth

# Initialize the plot with subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(18, 8))

# Colors for different years
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5']

# Plot the first subplot (Horizontal Bar Chart)
for i, year in enumerate(years):
    y_positions = np.arange(len(regions)) + (i * 0.15)
    rates = [literacy_rates[region][i] for region in regions]
    bars = ax1.barh(y_positions, rates, height=0.15, label=f'Year {year}', color=colors[i], alpha=0.8)
    for bar in bars:
        ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width()}%', va='center', ha='left', fontsize=9)

ax1.set_yticks(np.arange(len(regions)) + 0.3)
ax1.set_yticklabels(regions)
ax1.set_xlabel('Literacy Rate (%)')
ax1.set_title('Literacy Rates Across Regions (1950-2020)', fontsize=14, fontweight='bold')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, axis='x', alpha=0.7)
ax1.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot the second subplot (Line Chart)
for region in regions:
    ax2.plot(years, growth_rates[region], marker='o', label=region)

ax2.set_xlabel('Year')
ax2.set_ylabel('Growth Rate (%)')
ax2.set_title('Decadal Growth in Literacy Rates', fontsize=14, fontweight='bold')
ax2.axhline(0, color='grey', linewidth=0.8)
ax2.grid(True, linestyle='--', linewidth=0.5)
ax2.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()