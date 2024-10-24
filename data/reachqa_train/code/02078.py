import matplotlib.pyplot as plt
import numpy as np

# Define the years and the number of new residential units for each district
years = ['2015', '2016', '2017', '2018', '2019', '2020']
central = [150, 180, 210, 240, 300, 350]
riverside = [90, 110, 140, 170, 200, 230]
hilltop = [50, 60, 70, 80, 100, 120]
eastside = [130, 160, 190, 210, 260, 320]
westend = [40, 60, 80, 100, 130, 160]

# Set positions for the bars
x = np.arange(len(years))

# Set the width of the bars
width = 0.15

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for each district
bars_central = ax.bar(x - 2*width, central, width, label='Central District', color='#FF5733')
bars_riverside = ax.bar(x - width, riverside, width, label='Riverside District', color='#33FFBD')
bars_hilltop = ax.bar(x, hilltop, width, label='Hilltop District', color='#3380FF')
bars_eastside = ax.bar(x + width, eastside, width, label='Eastside District', color='#F033FF')
bars_westend = ax.bar(x + 2*width, westend, width, label='Westend District', color='#FFBD33')

# Add labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('New Residential Units', fontsize=14)
ax.set_title('Urban Growth and Housing Developments\nin Metropolis City (2015-2020)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)

# Add data annotations
def add_annotations(bars):
    for bar in bars:
        yval = bar.get_height()
        ax.annotate(f'{yval}', xy=(bar.get_x() + bar.get_width() / 2, yval),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

add_annotations(bars_central)
add_annotations(bars_riverside)
add_annotations(bars_hilltop)
add_annotations(bars_eastside)
add_annotations(bars_westend)

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()