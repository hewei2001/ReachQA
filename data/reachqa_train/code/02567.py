import matplotlib.pyplot as plt
import numpy as np

# Data: Number of hectares added each year for different green space types
years = np.arange(2020, 2031)
parks = np.array([10, 15, 25, 35, 45, 55, 65, 75, 90, 100, 120])
gardens = np.array([5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60])
reserves = np.array([2, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50])

# Cumulative data
parks_cumulative = np.cumsum(parks)
gardens_cumulative = np.cumsum(gardens)
reserves_cumulative = np.cumsum(reserves)

# Calculate year-on-year growth rates
parks_growth_rate = np.diff(parks) / parks[:-1] * 100
gardens_growth_rate = np.diff(gardens) / gardens[:-1] * 100
reserves_growth_rate = np.diff(reserves) / reserves[:-1] * 100

# Create a plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Stackplot for cumulative data
ax1.stackplot(years, parks_cumulative, gardens_cumulative, reserves_cumulative,
              labels=['Parks', 'Community Gardens', 'Natural Reserves'],
              colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.7)

ax1.set_title('Urban Green Space Expansion\nA Decade of Greener Living in EcoVille (2020-2030)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cumulative Green Space Area (Hectares)', fontsize=12)

# Customize legend
ax1.legend(loc='upper left', title='Green Space Type', fontsize=10)

# Set ticks and grid
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate significant milestone
ax1.annotate('Significant Expansion\nInitiative in 2025', xy=(2025, 220), xytext=(2025, 360),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Secondary Y-axis for growth rates
ax2 = ax1.twinx()
ax2.plot(years[1:], parks_growth_rate, label='Parks Growth Rate', color='#1b9e77', linestyle='--', marker='o')
ax2.plot(years[1:], gardens_growth_rate, label='Gardens Growth Rate', color='#d95f02', linestyle='--', marker='o')
ax2.plot(years[1:], reserves_growth_rate, label='Reserves Growth Rate', color='#7570b3', linestyle='--', marker='o')

ax2.set_ylabel('Annual Growth Rate (%)', fontsize=12)
ax2.legend(loc='upper right', title='Growth Rate', fontsize=10)
ax2.grid(visible=False)

# Use tight_layout to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()