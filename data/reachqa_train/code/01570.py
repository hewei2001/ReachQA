import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2022
years = np.arange(2012, 2023)

# Interest index data for different regions
north_america = np.array([10, 15, 18, 22, 30, 40, 50, 65, 78, 85, 95])
europe = np.array([8, 12, 15, 20, 25, 35, 45, 55, 67, 74, 80])
asia_pacific = np.array([5, 8, 12, 18, 27, 35, 48, 60, 72, 82, 90])

# New data: Predicted Growth Rate in percentage for each region
north_america_growth = np.array([5, 6, 5.5, 6, 7, 8, 9, 10, 11, 9.5, 9])
europe_growth = np.array([4, 4.5, 4.8, 5.5, 6.5, 7, 8, 9, 9.5, 9, 8.5])
asia_pacific_growth = np.array([6, 7, 7.5, 8, 9, 10, 11, 12, 13, 13.5, 14])

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plotting the line chart for interest index
ax1.plot(years, north_america, label='North America', marker='o', linestyle='-', linewidth=2.5, color='blue')
ax1.plot(years, europe, label='Europe', marker='s', linestyle='--', linewidth=2.5, color='green')
ax1.plot(years, asia_pacific, label='Asia-Pacific', marker='^', linestyle='-.', linewidth=2.5, color='red')

# Title, labels, and grid for the first plot
ax1.set_title('Rising Curiosity: Quantum Computing in Academia\n(2012-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Interest Index', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title="Regions", loc='upper left', fontsize=10)

# Plotting the bar chart for predicted growth rate
bar_width = 0.25
ax2.bar(years - bar_width, north_america_growth, width=bar_width, label='North America', color='blue', alpha=0.7)
ax2.bar(years, europe_growth, width=bar_width, label='Europe', color='green', alpha=0.7)
ax2.bar(years + bar_width, asia_pacific_growth, width=bar_width, label='Asia-Pacific', color='red', alpha=0.7)

# Title, labels, and legend for the second plot
ax2.set_title('Predicted Growth Rate in Interest\n(2012-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(title="Regions", loc='upper left', fontsize=10)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()