import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2023)

# Define renewable energy data as a percentage of total energy consumption for each country
germany = np.array([10, 12, 15, 18, 22, 25, 29, 34, 38, 42, 46, 49, 52])
spain = np.array([13, 14, 16, 19, 23, 27, 30, 35, 39, 43, 47, 50, 53])
france = np.array([8, 9, 12, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41])
italy = np.array([11, 12, 14, 17, 21, 24, 28, 32, 36, 40, 44, 47, 50])
sweden = np.array([20, 22, 25, 28, 32, 36, 40, 44, 48, 51, 54, 57, 60])

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot each country's data with distinctive styles
plt.plot(years, germany, marker='o', linestyle='-', color='blue', linewidth=2, label='Germany')
plt.plot(years, spain, marker='s', linestyle='-', color='green', linewidth=2, label='Spain')
plt.plot(years, france, marker='^', linestyle='-', color='red', linewidth=2, label='France')
plt.plot(years, italy, marker='D', linestyle='-', color='purple', linewidth=2, label='Italy')
plt.plot(years, sweden, marker='*', linestyle='-', color='orange', linewidth=2, label='Sweden')

# Annotate key events
plt.annotate('Germany\'s Renewable Energy Act', xy=(2014, 18), 
             xytext=(2015, 15), textcoords='data', 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, ha='center')

plt.annotate('Spain reaches 30%', xy=(2017, 30), 
             xytext=(2016, 35), textcoords='data', 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, ha='center')

plt.annotate('Italy Solar Incentives', xy=(2020, 28), 
             xytext=(2018, 33), textcoords='data', 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, ha='center')

plt.annotate('Sweden targets 100% renewable', xy=(2022, 60), 
             xytext=(2019, 65), textcoords='data', 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, ha='center')

# Customize the plot
plt.title('Renewable Energy Adoption in European Countries\n(2010-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Energy from Renewable Sources', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()