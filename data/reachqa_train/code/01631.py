import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2015, 2026)

# Define the number of EVs in thousands for each region over the years
north_america = [100, 150, 230, 330, 450, 580, 730, 890, 1070, 1260, 1460]
europe = [80, 120, 200, 290, 410, 550, 720, 900, 1100, 1310, 1530]
asia = [60, 90, 170, 270, 390, 530, 690, 870, 1070, 1290, 1520]
other_regions = [20, 35, 60, 95, 140, 200, 280, 380, 500, 640, 800]

# Stack the data
data = np.vstack([north_america, europe, asia, other_regions])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the stacked area plot
ax.stackplot(years, data, labels=['North America', 'Europe', 'Asia', 'Other Regions'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Customize the plot with a backstory
ax.set_title('Growth of Electric Vehicle Adoption by Region\nfrom 2015 to 2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Electric Vehicles (in thousands)', fontsize=12)

# Add legend with title, positioned outside the main plot area
ax.legend(loc='upper left', title='Regions', fontsize=10, bbox_to_anchor=(1, 1))

# Customize grid lines to improve readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Avoid overlapping x-axis labels by adjusting rotation
plt.xticks(years, rotation=45)

# Automatically adjust layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()