import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy production data (TWh) for each country
germany_production = [50, 58, 65, 80, 92, 105, 118, 132, 148, 160, 172]
usa_production = [150, 160, 175, 180, 185, 195, 205, 215, 230, 245, 260]
china_production = [200, 215, 230, 250, 280, 310, 350, 390, 430, 470, 520]
india_production = [60, 65, 70, 75, 85, 100, 120, 140, 160, 180, 200]

# Error margins (TWh)
germany_error = [5, 5, 6, 6, 7, 7, 8, 8, 9, 10, 11]
usa_error = [10, 10, 11, 11, 12, 12, 13, 13, 15, 15, 16]
china_error = [15, 15, 16, 16, 17, 17, 18, 18, 19, 20, 22]
india_error = [4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]

# Plotting
plt.figure(figsize=(14, 7))

# Plot lines with error bars
plt.errorbar(years, germany_production, yerr=germany_error, label='Germany', fmt='-o', capsize=4, color='forestgreen')
plt.errorbar(years, usa_production, yerr=usa_error, label='USA', fmt='-o', capsize=4, color='steelblue')
plt.errorbar(years, china_production, yerr=china_error, label='China', fmt='-o', capsize=4, color='orange')
plt.errorbar(years, india_production, yerr=india_error, label='India', fmt='-o', capsize=4, color='crimson')

# Add title and labels with detailed formatting
plt.title('Renewable Energy Growth in Select Countries (2010-2020)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (TWh)', fontsize=12)

# Set grid with better visualization options
plt.grid(True, linestyle='--', alpha=0.7)

# Create legend with improved font size
plt.legend(title="Countries", fontsize=11, title_fontsize='13')

# Setting x-ticks to make it more comprehensive
plt.xticks(years, rotation=45)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()