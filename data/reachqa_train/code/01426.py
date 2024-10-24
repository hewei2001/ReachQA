import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Hypothetical data representing emissions in million metric tons
co2_emissions = np.array([29.5, 30.2, 31.0, 31.8, 32.6, 33.4, 34.0, 34.5, 35.1, 35.6, 36.0, 36.2, 36.5, 36.3, 36.1, 35.8, 35.3, 34.7, 34.2, 33.6, 33.0])
ch4_emissions = np.array([4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.1, 5.0, 4.9, 4.8, 4.7, 4.6, 4.5, 4.3, 4.2, 4.1, 4.0])
n2o_emissions = np.array([2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.5, 3.5, 3.5, 3.4, 3.3, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.7])

# Create the line chart
plt.figure(figsize=(12, 8))
plt.plot(years, co2_emissions, label='CO2 Emissions', color='red', marker='o', linestyle='-', linewidth=2)
plt.plot(years, ch4_emissions, label='CH4 Emissions', color='green', marker='s', linestyle='--', linewidth=2)
plt.plot(years, n2o_emissions, label='N2O Emissions', color='blue', marker='^', linestyle='-.', linewidth=2)

# Chart titles and labels
plt.title('Trends in Global Greenhouse Gas Emissions\n(2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Emissions (Million Metric Tons)', fontsize=12)

# Customize the tick marks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(2, 38, 2))

# Add a legend
plt.legend(title='Gas Type', title_fontsize='13', fontsize=11, loc='upper right')

# Annotate a specific point of interest
plt.annotate('Peak CO2 Emissions', xy=(2010, 36.0), xytext=(2008, 36.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Add a grid to the background
plt.grid(visible=True, which='major', linestyle='--', linewidth=0.5)

# Adjust layout to prevent clipping of title or labels
plt.tight_layout()

# Display the chart
plt.show()