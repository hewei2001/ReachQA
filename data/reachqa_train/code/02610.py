import matplotlib.pyplot as plt
import numpy as np

# Data for the area chart
years = np.arange(2013, 2023)
solar = np.array([5, 7, 10, 13, 16, 20, 25, 30, 35, 40])
wind = np.array([15, 18, 20, 22, 24, 26, 28, 30, 32, 34])
hydro = np.array([50, 48, 45, 42, 40, 38, 36, 34, 32, 30])
geothermal = np.array([5, 7, 8, 10, 12, 14, 15, 16, 17, 18])
other_sources = 100 - (solar + wind + hydro + geothermal)

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart
ax.stackplot(years, solar, wind, hydro, geothermal, other_sources, 
             labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Other Sources'],
             colors=['#ffcc00', '#66c2a5', '#8da0cb', '#fc8d62', '#e78ac3'],
             alpha=0.85)

# Title and labels
ax.set_title('The Evolution of Green Energy Adoption\n(2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Contribution to Renewable Energy (%)', fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10, title="Energy Sources", frameon=False)

# Improving the x-axis visibility
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate specific points
for i, txt in enumerate(solar):
    ax.text(years[i], txt + 3, f"{txt}%", fontsize=9, color='black', ha='center')
for i, txt in enumerate(wind):
    ax.text(years[i], txt + solar[i] + 3, f"{txt}%", fontsize=9, color='black', ha='center')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()