import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2050, 2061)

# Mineral resource extraction data in arbitrary units (e.g., tons)
iron = [50, 55, 62, 70, 78, 87, 97, 108, 120, 133, 147]
magnesium = [30, 35, 40, 46, 52, 59, 67, 75, 84, 94, 105]
silicon = [20, 22, 25, 29, 34, 40, 47, 55, 64, 74, 85]
helium3 = [5, 6, 8, 10, 13, 17, 22, 28, 35, 43, 52]

# Set up the plot
plt.figure(figsize=(14, 8))

# Create stacked bar chart
plt.bar(years, iron, label='Iron', color='#ff9999', width=0.6)
plt.bar(years, magnesium, bottom=iron, label='Magnesium', color='#66b3ff', width=0.6)
plt.bar(years, silicon, bottom=np.array(iron)+np.array(magnesium), label='Silicon', color='#99ff99', width=0.6)
plt.bar(years, helium3, bottom=np.array(iron)+np.array(magnesium)+np.array(silicon), label='Helium-3', color='#ffcc99', width=0.6)

# Add title and labels
plt.title("Distribution of Mineral Resources on a Martian Colony\nExtraction Growth from 2050 to 2060", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Resource Extraction (Tons)", fontsize=12)

# Add legend
plt.legend(title='Minerals', loc='upper left', fontsize=10)

# Adjust x-axis labels for better readability
plt.xticks(years, rotation=45)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optimize layout to ensure no overlapping text and good spacing
plt.tight_layout()

# Display the plot
plt.show()