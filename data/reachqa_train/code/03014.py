import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average number of bicycles per household for each city
amsterdam_bicycles = [1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.3, 2.4, 2.5, 2.5, 2.6]
berlin_bicycles = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.8, 1.9, 2.0, 2.1]
copenhagen_bicycles = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.5, 2.6, 2.7, 2.8, 2.9]
paris_bicycles = [0.7, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]

# Plotting
plt.figure(figsize=(12, 8))

# Plot each city's data with different styles
plt.plot(years, amsterdam_bicycles, marker='o', label='Amsterdam', linestyle='-', linewidth=2, color='blue')
plt.plot(years, berlin_bicycles, marker='s', label='Berlin', linestyle='--', linewidth=2, color='green')
plt.plot(years, copenhagen_bicycles, marker='^', label='Copenhagen', linestyle='-.', linewidth=2, color='red')
plt.plot(years, paris_bicycles, marker='d', label='Paris', linestyle=':', linewidth=2, color='purple')

# Annotate data points to make them readable
for (city_data, color) in zip([amsterdam_bicycles, berlin_bicycles, copenhagen_bicycles, paris_bicycles], ['blue', 'green', 'red', 'purple']):
    for (year, bicycle_count) in zip(years, city_data):
        plt.text(year, bicycle_count + 0.05, f'{bicycle_count}', fontsize=9, color=color, ha='center', va='bottom')

# Customize plot
plt.title('Average Number of Bicycles Per Household\nin European Cities (2010-2020)', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Number of Bicycles', fontsize=12)
plt.xticks(years, rotation=45)
plt.ylim(0, 3)
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(title='City', loc='upper left', fontsize=10)

# Adjust layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()