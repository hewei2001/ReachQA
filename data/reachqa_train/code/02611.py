import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2061, 5)

# Energy usage data as percentage of total transportation energy
fossil_fuels = [80, 75, 65, 55, 40, 30, 20, 10, 5]
electric = [10, 15, 20, 25, 30, 35, 40, 45, 50]
hydrogen = [5, 6, 8, 10, 15, 20, 25, 30, 35]
biofuels = [5, 4, 7, 10, 15, 15, 15, 15, 10]

# Set up the figure and axis
plt.figure(figsize=(12, 8))

# Create stacked area chart
plt.stackplot(years, fossil_fuels, electric, hydrogen, biofuels,
              labels=['Fossil Fuels', 'Electric', 'Hydrogen', 'Biofuels'],
              colors=['#d95f02', '#7570b3', '#1b9e77', '#e7298a'],
              alpha=0.85)

# Title and labels with formatting
plt.title('Transportation Energy Evolution\nFrom Fossil Fuels to Future Energy (2020-2060)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Source Proportion (%)', fontsize=14)

# Customize legend
plt.legend(title="Energy Sources", fontsize=11, title_fontsize='13', loc='upper left', bbox_to_anchor=(1, 1))

# Ensure grid lines for y-axis
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Enhance the readability of x-axis labels
plt.xticks(years, rotation=45, ha='right')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()