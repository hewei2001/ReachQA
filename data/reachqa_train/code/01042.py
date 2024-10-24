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

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for different years
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5']

# Plot each region's literacy rates as horizontal bars for each year
for i, year in enumerate(years):
    y_positions = np.arange(len(regions)) + (i * 0.15)
    rates = [literacy_rates[region][i] for region in regions]
    bars = ax.barh(y_positions, rates, height=0.15, label=f'Year {year}', color=colors[i], alpha=0.8)
    
    # Add data labels
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width()}%', va='center', ha='left', fontsize=10)

# Set labels and title
ax.set_yticks(np.arange(len(regions)) + 0.3)
ax.set_yticklabels(regions)
ax.set_xlabel('Literacy Rate (%)')
ax.set_title('Evolution of Literacy Rates (1950-2020)\nAcross Different World Regions',
             fontsize=16, fontweight='bold', pad=20)

# Enable grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='x', alpha=0.7)

# Show legend
ax.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()