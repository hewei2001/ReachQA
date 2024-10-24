import matplotlib.pyplot as plt
import numpy as np

# Define the years from 1980 to 2020 with five-year intervals
years = ['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020']

# Define shares for various energy sources across these years
coal = [50, 48, 45, 42, 40, 35, 30, 25, 20]
nuclear = [10, 12, 15, 18, 20, 22, 20, 17, 15]
natural_gas = [20, 18, 20, 22, 25, 28, 30, 27, 25]
hydro = [15, 14, 12, 11, 10, 10, 10, 10, 10]
renewables = [5, 8, 8, 7, 5, 5, 10, 20, 30]
geothermal = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# Prepare data for the stackplot
data = np.array([coal, nuclear, natural_gas, hydro, renewables, geothermal])

# Configure the figure
plt.figure(figsize=(14, 9))
plt.stackplot(years, coal, nuclear, natural_gas, hydro, renewables, geothermal,
              labels=['Coal', 'Nuclear', 'Natural Gas', 'Hydro', 'Renewables', 'Geothermal'],
              colors=['#8B0000', '#FFD700', '#1E90FF', '#32CD32', '#FF8C00', '#8B4513'], 
              alpha=0.85)

# Add key events annotations
plt.text('1997', 85, 'Kyoto Protocol\nSigned', horizontalalignment='center', fontsize=9, color='black')
plt.text('2015', 80, 'Paris Agreement\nAdopted', horizontalalignment='center', fontsize=9, color='black')

# Title and labels with enhanced detail
plt.title('Transformation of Energy Generation Mix (1980-2020)\nAnalysis of Trends & Impact of Major Agreements', fontsize=15, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage Share (%)', fontsize=12)

# Legend configuration
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()