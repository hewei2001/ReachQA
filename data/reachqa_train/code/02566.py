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

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the area chart using stackplot for cumulative data
ax.stackplot(years, parks_cumulative, gardens_cumulative, reserves_cumulative,
             labels=['Parks', 'Community Gardens', 'Natural Reserves'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.7)

# Add title and labels
ax.set_title('Urban Green Space Expansion: A Decade of Greener Living\nEcoVille, 2020-2030', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cumulative Green Space Area (Hectares)', fontsize=12)

# Customize legend
ax.legend(loc='upper left', title='Green Space Type', fontsize=10)

# Set ticks and grid
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate significant milestone
ax.annotate('Significant Expansion\nInitiative in 2025', xy=(2025, 100), xytext=(2025, 250),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Use tight_layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()