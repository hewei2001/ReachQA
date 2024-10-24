import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2050 to 2060
years = np.arange(2050, 2061)

# Energy consumption data (in arbitrary units) for each sector, using more complex patterns
residential = [60, 58, 61, 59, 57, 54, 53, 51, 50, 48, 47]
industrial = [80, 78, 82, 77, 75, 74, 72, 70, 69, 68, 66]
commercial = [50, 51, 52, 53, 51, 50, 49, 48, 48, 47, 46]
transport = [70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60]
agriculture = [20, 21, 23, 24, 22, 21, 22, 23, 22, 21, 20]
technology = [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Subcategories within residential
urban_residential = np.array(residential) * 0.7
rural_residential = np.array(residential) * 0.3

# Plotting the stacked area chart
plt.figure(figsize=(14, 10))
plt.stackplot(years, urban_residential, rural_residential, industrial, commercial, transport, agriculture, technology,
              labels=['Urban Residential', 'Rural Residential', 'Industrial', 'Commercial', 'Transport', 'Agriculture', 'Technology'],
              colors=['#FF9999', '#FF6666', '#66B3FF', '#99FF99', '#FFCC99', '#FFB366', '#CC99FF'], alpha=0.9)

# Title and axis labels
plt.title('NeoCity Energy Consumption Evolution (2050-2060)\nTowards Sustainable Urban Living\nIn-depth Sectoral Analysis', fontsize=16, fontweight='bold', color='darkslategray')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Energy Consumption (Arbitrary Units)', fontsize=12, fontweight='bold')

# Adding a legend outside the main plot area
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Sectors', fontsize=10)

# Grid for better readability
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotating significant milestones and peak points
milestones = {
    2052: 'Smart Grids Introduced',
    2055: 'Renewable Integration',
    2058: 'Eco-efficient Transport'
}

for year, text in milestones.items():
    consumption = sum([urban_residential[year-2050], rural_residential[year-2050], industrial[year-2050], 
                       commercial[year-2050], transport[year-2050], agriculture[year-2050], technology[year-2050]])
    plt.annotate(text, xy=(year, consumption*0.7),
                 xytext=(year, consumption + 10),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center', color='black', backgroundcolor='white')

# Highlighting peak points
peak_years = {2052: 'Peak Residential', 2056: 'Peak Industrial'}
for year, label in peak_years.items():
    plt.annotate(label, xy=(year, sum([urban_residential[year-2050], rural_residential[year-2050], industrial[year-2050], 
                                       commercial[year-2050], transport[year-2050], agriculture[year-2050], technology[year-2050]])*0.9),
                 xytext=(year, sum([urban_residential[year-2050], rural_residential[year-2050], industrial[year-2050], 
                                    commercial[year-2050], transport[year-2050], agriculture[year-2050], technology[year-2050]]) + 5),
                 arrowprops=dict(facecolor='green', arrowstyle='->'),
                 fontsize=9, ha='center', color='darkgreen', backgroundcolor='lightyellow')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show plot
plt.show()