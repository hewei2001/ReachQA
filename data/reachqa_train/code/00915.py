import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2050 to 2060
years = np.arange(2050, 2061)

# Energy consumption data (in arbitrary units) for each sector
residential = [60, 58, 55, 53, 52, 50, 49, 48, 46, 45, 44]
industrial = [80, 78, 75, 72, 70, 69, 67, 66, 65, 64, 63]
commercial = [50, 52, 51, 50, 49, 49, 48, 48, 47, 46, 45]
transport = [70, 68, 67, 65, 63, 62, 60, 59, 58, 57, 56]

# Create the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, residential, industrial, commercial, transport, labels=['Residential', 'Industrial', 'Commercial', 'Transport'], colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8)

# Title and axis labels
plt.title('NeoCity Energy Consumption Evolution (2050-2060)\nTowards Sustainable Urban Living', fontsize=16, fontweight='bold', color='darkslategray')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Energy Consumption (Arbitrary Units)', fontsize=12, fontweight='bold')

# Adding a legend outside the main plot area
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Sectors', fontsize=10)

# Grid for better readability
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotating significant milestones
milestones = {
    2052: 'Smart Grids Introduced',
    2055: 'Renewable Integration',
    2058: 'Eco-efficient Transport'
}

for year, text in milestones.items():
    plt.annotate(text, xy=(year, sum([residential[year-2050], industrial[year-2050], commercial[year-2050], transport[year-2050]])*0.8),
                 xytext=(year, sum([residential[year-2050], industrial[year-2050], commercial[year-2050], transport[year-2050]]) + 20),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center', color='black', backgroundcolor='white')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show plot
plt.show()