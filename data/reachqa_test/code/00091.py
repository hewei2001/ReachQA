import matplotlib.pyplot as plt
import numpy as np

# Data for solar energy production in Solaria (2010-2020)
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
solar_production = np.array([50, 55, 65, 75, 85, 100, 120, 140, 170, 200, 230])  # in GWh

# Calculate annual growth rates
growth_rate = np.zeros_like(solar_production)
growth_rate[1:] = ((solar_production[1:] - solar_production[:-1]) / solar_production[:-1]) * 100

# Create main plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot solar production with gradient effect
norm = plt.Normalize(min(solar_production), max(solar_production))
cmap = plt.get_cmap('YlOrRd')
ax1.plot(years, solar_production, marker='o', color='orange', linestyle='-', linewidth=2, label='Solar Production')
ax1.fill_between(years, solar_production, color='orange', alpha=0.3)

# Add annotations and highlights
for i, production in enumerate(solar_production):
    ax1.annotate(f'{production} GWh', xy=(years[i], production), xytext=(0, 8), textcoords='offset points', ha='center', fontsize=9)

# Second axis for growth rate
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='blue', linestyle='--', marker='s', linewidth=1.5, label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', color='blue', fontsize=12)
ax2.tick_params(axis='y', labelcolor='blue')

# Highlight maximum growth rate
max_growth_idx = np.argmax(growth_rate)
ax1.scatter(years[max_growth_idx], solar_production[max_growth_idx], color='red', zorder=5)
ax1.annotate('Max Growth', xy=(years[max_growth_idx], solar_production[max_growth_idx]), xytext=(0, -30), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='red'), fontsize=10, color='red')

# Add plot titles and labels
ax1.set_title("Decade of Sunshine:\nSolar Energy Production and Growth in Solaria (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Solar Energy Production (GWh)", fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(range(0, 251, 25))

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), bbox_transform=ax1.transAxes)

# Add grid and layout adjustment
ax1.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()