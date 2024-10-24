import matplotlib.pyplot as plt
import numpy as np

# Define years and regions
years = np.arange(2010, 2021)
regions = ['North America', 'Europe', 'Asia-Pacific']

# EV adoption data in percentage
north_america = np.array([1, 2, 3, 5, 7, 10, 15, 22, 30, 42, 55])
europe = np.array([1, 3, 6, 10, 15, 25, 35, 50, 68, 80, 92])
asia_pacific = np.array([1, 2, 4, 7, 12, 18, 25, 35, 47, 60, 75])

# Create the area chart
plt.figure(figsize=(14, 8))

# Plot area chart
plt.fill_between(years, north_america, label='North America', color='#1f77b4', alpha=0.7)
plt.fill_between(years, europe, north_america, label='Europe', color='#ff7f0e', alpha=0.7)
plt.fill_between(years, asia_pacific, europe, label='Asia-Pacific', color='#2ca02c', alpha=0.7)

# Adding labels and title
plt.title('Electric Vehicle Adoption Trends (2010-2020)\nAcross Regions', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('EV Adoption (%)', fontsize=12)

# Add legend
plt.legend(loc='upper left', title='Regions')

# Customize grid and axes
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate significant data points
for year, na, eu, ap in zip(years, north_america, europe, asia_pacific):
    plt.text(year, na - 5, f'{na}%', color='white', ha='center', va='center', fontsize=9)
    plt.text(year, (na + eu) / 2, f'{eu}%', color='black', ha='center', va='center', fontsize=9)
    plt.text(year, (eu + ap) / 2 + 5, f'{ap}%', color='black', ha='center', va='center', fontsize=9)

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()