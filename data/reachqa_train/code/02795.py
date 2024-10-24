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

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stack plot of the cumulative EV adoption
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#F4A582', '#BCBD22']
labels = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
ax.stackplot(years, north_america, europe, asia, south_america, africa, australia, 
             labels=labels, colors=colors, alpha=0.8)

# Title and Labels
ax.set_title('The Rise of Electric Vehicles\nGlobal Adoption Trends 2020-2025', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Cumulative EV Adoption (Millions)', fontsize=12, fontweight='bold')

# Adjust x-axis tick labels to avoid overlap
plt.xticks(years)

# Adding grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper left', fontsize=10, title='Continents')

# Adding annotations to highlight key data points
ax.annotate('Major growth in Europe', xy=(2025, 7), xytext=(2024, 8),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Steady rise in Asia', xy=(2025, 6.2), xytext=(2024, 5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()