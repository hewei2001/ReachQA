import matplotlib.pyplot as plt
import numpy as np

# Define years for the timeline
years = np.arange(2010, 2021)

# Renewable energy adoption data for different regions
renewable_adoption = {
    'North America': [10, 12, 13, 15, 18, 20, 23, 25, 28, 31, 35],
    'Europe': [15, 18, 21, 25, 28, 32, 36, 41, 45, 50, 55],
    'Asia': [5, 7, 10, 12, 15, 18, 20, 24, 30, 37, 45],
    'Africa': [2, 3, 5, 7, 9, 11, 13, 16, 19, 22, 26],
    'South America': [8, 10, 12, 14, 16, 20, 24, 28, 33, 38, 44]
}

# Create the plot
plt.figure(figsize=(14, 8))

# Define colors for each region
colors = ['blue', 'green', 'red', 'orange', 'purple']

# Plot each region's data
for i, (region, adoption) in enumerate(renewable_adoption.items()):
    plt.plot(years, adoption, label=region, color=colors[i], marker='o', linewidth=2)
    # Annotate each data point with the corresponding percentage
    for year, percent in zip(years, adoption):
        plt.annotate(f'{percent}%', (year, percent), textcoords="offset points", xytext=(-10,10), ha='center',
                     fontsize=9, color=colors[i], backgroundcolor='white', alpha=0.8)

# Add a multi-line title and axis labels
plt.title('Decade of Green:\nRenewable Energy Adoption Across Regions (2010-2020)', fontsize=18, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy (% of Total Consumption)', fontsize=14)

# Set y-axis range and add gridlines
plt.ylim(0, 60)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend, positioned to avoid data occlusion
plt.legend(title='Regions', loc='upper left', fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()