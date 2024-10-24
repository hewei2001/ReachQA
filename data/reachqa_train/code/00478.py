import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2010, 2021)

# Renewable energy data for each region (values adjusted for clarity)
north_america = {
    'Solar': [2, 3, 5, 7, 10, 13, 15, 16, 18, 20, 22],
    'Wind': [5, 7, 10, 13, 16, 19, 22, 25, 27, 29, 31],
    'Hydro': [30, 32, 35, 37, 38, 39, 40, 40, 40, 41, 42],
}

europe = {
    'Solar': [3, 5, 7, 9, 12, 15, 18, 21, 23, 24, 25],
    'Wind': [10, 13, 16, 20, 24, 27, 30, 33, 35, 36, 38],
    'Hydro': [20, 22, 23, 24, 24, 25, 26, 26, 27, 27, 28],
}

asia_pacific = {
    'Solar': [1, 2, 4, 6, 9, 12, 15, 17, 19, 21, 24],
    'Wind': [4, 6, 9, 12, 15, 18, 22, 25, 28, 30, 33],
    'Hydro': [35, 36, 36, 37, 38, 39, 40, 41, 42, 43, 44],
}

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting North America
ax.stackplot(years, north_america.values(), labels=['Solar (NA)', 'Wind (NA)', 'Hydro (NA)'],
             colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)

# Plotting Europe
ax.stackplot(years, europe.values(), labels=['Solar (EU)', 'Wind (EU)', 'Hydro (EU)'],
             colors=['#ff6666', '#3366cc', '#66cc66'], alpha=0.7)

# Plotting Asia-Pacific
ax.stackplot(years, asia_pacific.values(), labels=['Solar (AP)', 'Wind (AP)', 'Hydro (AP)'],
             colors=['#ff4d4d', '#4d94ff', '#4dff4d'], alpha=0.6)

# Title and labels
ax.set_title("Decade of Renewable Energy Adoption\nacross Key Global Regions (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Total Energy Production", fontsize=12)

# Legends and grid
ax.legend(loc='upper left', fontsize=10, title="Region & Energy Type", ncol=2)
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()