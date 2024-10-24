import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2025
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])

# Cumulative number of electric vehicles (in millions) adopted by each continent
north_america = np.array([0.8, 1.5, 2.7, 3.5, 4.2, 5.1])
europe = np.array([1.0, 2.0, 3.1, 4.6, 5.8, 7.0])
asia = np.array([0.9, 1.8, 3.2, 4.1, 5.0, 6.2])
south_america = np.array([0.2, 0.5, 0.9, 1.2, 1.8, 2.3])
africa = np.array([0.1, 0.3, 0.6, 1.0, 1.5, 2.0])
australia = np.array([0.3, 0.6, 1.0, 1.5, 2.1, 2.7])

# Constructing growth rate data for the overlay plot
growth_rate = np.array([0.25, 0.32, 0.45, 0.5, 0.55, 0.6])  # Hypothetical growth rate per year

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 9))

# Stack plot of the cumulative EV adoption
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#F4A582', '#BCBD22']
labels = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
ax1.stackplot(years, north_america, europe, asia, south_america, africa, australia, 
              labels=labels, colors=colors, alpha=0.8)

# Setting primary y-axis properties
ax1.set_title('The Rise of Electric Vehicles\nGlobal Adoption Trends and Growth Rates (2020-2025)', 
              fontsize=18, fontweight='bold', pad=30)
ax1.set_xlabel('Year', fontsize=14, fontweight='bold')
ax1.set_ylabel('Cumulative EV Adoption (Millions)', fontsize=14, fontweight='bold')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=11, title='Continents', title_fontsize=12)

# Secondary y-axis for growth rate
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, 'o--', color='tab:red', label='Global EV Growth Rate', linewidth=2, markersize=6)
ax2.set_ylabel('Growth Rate (%)', fontsize=14, fontweight='bold', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.legend(loc='upper right', fontsize=11, title='Growth Trend', title_fontsize=12)

# Adjust x-axis tick labels to avoid overlap
ax1.set_xticks(years)

# Annotations for significant trends
ax1.annotate('Major growth in Europe', xy=(2025, 7), xytext=(2024, 8),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Steady rise in Asia', xy=(2025, 6.2), xytext=(2024, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()