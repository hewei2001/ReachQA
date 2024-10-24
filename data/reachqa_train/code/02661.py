import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy sources contributions (percentage of total renewable energy)
solar = [5, 7, 10, 15, 20, 25, 30, 35, 38, 42, 45]
wind = [30, 28, 27, 25, 22, 20, 18, 17, 17, 16, 15]
hydroelectric = [50, 48, 45, 42, 40, 38, 35, 33, 32, 31, 30]
biomass = [15, 17, 18, 18, 18, 17, 17, 15, 13, 11, 10]

# Stack the data for the area plot
data = np.vstack([solar, wind, hydroelectric, biomass])

# Create the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'], 
              colors=['#FFD700', '#87CEEB', '#32CD32', '#8B4513'], alpha=0.8)

# Titles and labels
plt.title("Renewable Energy Source Contributions (2010-2020)\nTowards a Sustainable Future", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Total Renewable Energy', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title="Energy Sources", fontsize=10, title_fontsize=11)

# Enhance the visual with a grid
plt.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()