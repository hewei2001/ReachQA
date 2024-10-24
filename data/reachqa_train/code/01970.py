import numpy as np
import matplotlib.pyplot as plt

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Area of land used for each crop (in hectares)
wheat = np.array([30, 35, 37, 40, 45, 50, 55, 60, 65, 67, 70])
corn = np.array([20, 22, 25, 28, 30, 35, 40, 42, 45, 46, 50])
soybeans = np.array([15, 18, 20, 22, 25, 27, 30, 35, 40, 42, 45])
barley = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35])

# Derived data: Percentage growth over the decade
wheat_growth = ((wheat - wheat[0]) / wheat[0]) * 100
corn_growth = ((corn - corn[0]) / corn[0]) * 100
soybeans_growth = ((soybeans - soybeans[0]) / soybeans[0]) * 100
barley_growth = ((barley - barley[0]) / barley[0]) * 100

# Cumulative data for area plot
wheat_cum = wheat
corn_cum = corn + wheat_cum
soybeans_cum = soybeans + corn_cum
barley_cum = barley + soybeans_cum

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Area chart
axs[0].fill_between(years, wheat_cum, label='Wheat', color='#FFD700', alpha=0.7)
axs[0].fill_between(years, corn_cum, wheat_cum, label='Corn', color='#FF6347', alpha=0.7)
axs[0].fill_between(years, soybeans_cum, corn_cum, label='Soybeans', color='#4682B4', alpha=0.7)
axs[0].fill_between(years, barley_cum, soybeans_cum, label='Barley', color='#32CD32', alpha=0.7)
axs[0].set_title('Agricultural Produce Growth Trends:\nA Decade of Change in Valley Farms (2010-2020)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Area of Land Used (hectares)', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].grid(visible=True, linestyle='--', alpha=0.5)

# Second subplot: Line plot for percentage growth
axs[1].plot(years, wheat_growth, marker='o', label='Wheat Growth %', color='#FFD700')
axs[1].plot(years, corn_growth, marker='s', label='Corn Growth %', color='#FF6347')
axs[1].plot(years, soybeans_growth, marker='^', label='Soybeans Growth %', color='#4682B4')
axs[1].plot(years, barley_growth, marker='d', label='Barley Growth %', color='#32CD32')
axs[1].set_title('Percentage Growth in Land Use per Crop (2010-2020)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth (%)', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()