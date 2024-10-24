import matplotlib.pyplot as plt
import numpy as np

# Define the years and fabrics
years = ['2018', '2019', '2020', '2021', '2022', '2023']
fabrics = ['Organic Cotton', 'Recycled Polyester', 'Bamboo Fabric', 'Hemp', 'Tencel']

# Data: Percentage of collections using each fabric type
data = {
    'Organic Cotton': [25, 30, 35, 40, 45, 50],
    'Recycled Polyester': [10, 15, 20, 30, 40, 45],
    'Bamboo Fabric': [5, 10, 15, 20, 25, 30],
    'Hemp': [3, 5, 8, 12, 18, 22],
    'Tencel': [7, 10, 14, 19, 23, 27]
}

# Calculate the average percentage of collections using sustainable fabrics each year
average_adoption = [np.mean([data[fabric][i] for fabric in fabrics]) for i in range(len(years))]

# Plot settings
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
positions = np.arange(len(years))

# Colors for each fabric
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Plot each fabric's data as bar chart
for i, fabric in enumerate(fabrics):
    ax.bar(positions + i * bar_width, data[fabric], bar_width, label=fabric, color=colors[i])

# Overlay a line chart for the average adoption
ax.plot(positions + bar_width * (len(fabrics) / 2), average_adoption, 
        marker='o', color='darkred', linewidth=2, label='Average Adoption')

# Annotate bars with data values
for i, fabric in enumerate(fabrics):
    for j in range(len(years)):
        ax.text(positions[j] + i * bar_width, data[fabric][j] + 1, str(data[fabric][j]),
                ha='center', va='bottom', fontsize=10, color='dimgrey')

# Annotate line chart data points
for i, value in enumerate(average_adoption):
    ax.text(positions[i] + bar_width * (len(fabrics) / 2), value + 1, f'{value:.1f}%', 
            ha='center', va='bottom', fontsize=10, color='darkred')

# Set labels, title, and ticks
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Collections', fontsize=12)
ax.set_title('The Rise of Sustainable Fabrics:\nAdoption in Fashion Industry (2018-2023)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(positions + bar_width * (len(fabrics) / 2))
ax.set_xticklabels(years)

# Add legend and grid
ax.legend(title='Fabrics', title_fontsize='13', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Enhance layout
plt.tight_layout()

# Show plot
plt.show()