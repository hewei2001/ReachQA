import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy consumption (in exajoules) for each sector
residential_consumption = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.8, 6.5, 7.5, 8]
industrial_consumption = [1, 1.5, 2, 2.8, 3.5, 4.2, 5.1, 6, 7.2, 8.6, 9.5]
transportation_consumption = [0.5, 0.6, 0.8, 1, 1.5, 2, 2.8, 3.5, 4.5, 5.7, 7]

# Cumulative consumption data for stacked plotting
consumptions = np.vstack([residential_consumption, industrial_consumption, transportation_consumption])

# Set up the plot
plt.figure(figsize=(12, 8))

# Plotting the stacked area chart
plt.stackplot(years, consumptions, labels=['Residential', 'Industrial', 'Transportation'], 
              colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.7)

# Titles and labels
plt.title("The Rise of Renewable Energy\nConsumption Across Sectors (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (Exajoules)", fontsize=12)

# Adding a legend
plt.legend(loc='upper left', title="Sectors")

# Customizing grid and style
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Adding annotations for significant trends
plt.annotate('Residential solar growth', xy=(2019, 16), xytext=(2016, 17),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

plt.annotate('Electric vehicles boom', xy=(2020, 22.5), xytext=(2018, 20.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

# Rotating x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()