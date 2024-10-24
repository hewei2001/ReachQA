import matplotlib.pyplot as plt
import numpy as np

# Time range from 2010 to 2023
years = np.arange(2010, 2024)

# Data for urban green space coverage percentage over time
nyc_green_space = [14.0, 14.5, 15.0, 15.2, 15.5, 15.7, 16.0, 16.4, 16.8, 17.2, 17.6, 18.0, 18.4, 18.8]
tokyo_green_space = [7.0, 7.2, 7.5, 8.0, 8.5, 9.0, 9.6, 10.2, 10.8, 11.5, 12.0, 12.5, 13.0, 13.5]
london_green_space = [33.0, 33.5, 34.0, 34.5, 35.0, 35.2, 35.5, 35.7, 36.0, 36.3, 36.6, 36.9, 37.2, 37.5]
sydney_green_space = [22.0, 22.4, 23.0, 23.5, 24.0, 24.6, 25.2, 25.8, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5]
nairobi_green_space = [10.0, 10.5, 11.0, 11.8, 12.5, 13.2, 14.0, 14.9, 15.7, 16.5, 17.0, 17.5, 18.0, 18.5]

# Plotting the line chart
plt.figure(figsize=(14, 8))

plt.plot(years, nyc_green_space, marker='o', linestyle='-', color='green', linewidth=2, label='New York City')
plt.plot(years, tokyo_green_space, marker='s', linestyle='--', color='blue', linewidth=2, label='Tokyo')
plt.plot(years, london_green_space, marker='^', linestyle='-.', color='purple', linewidth=2, label='London')
plt.plot(years, sydney_green_space, marker='D', linestyle=':', color='orange', linewidth=2, label='Sydney')
plt.plot(years, nairobi_green_space, marker='v', linestyle='-', color='red', linewidth=2, label='Nairobi')

# Add title and labels
plt.title("The Evolution of Urban Green Spaces:\nA Decade of Growth and Transformation", fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Green Space Coverage (%)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Cities', fontsize=10)

# Add grid for readability
plt.grid(alpha=0.3)

# Annotate key growth milestones
plt.annotate('Significant Expansion\nin 2020s', xy=(2019, 18.0), xytext=(2015, 19.5),
             arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=10, ha='center')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()