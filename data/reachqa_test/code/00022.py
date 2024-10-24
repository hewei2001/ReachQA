import matplotlib.pyplot as plt
import numpy as np

# Extended range of years from 2010 to 2023
years = np.arange(2010, 2024)

# Solar energy production data (in TWh)
us_production = [10, 15, 20, 25, 30, 40, 55, 70, 85, 100, 120, 135, 150, 170]
germany_production = [12, 18, 22, 28, 35, 42, 48, 55, 63, 70, 78, 85, 92, 100]
china_production = [8, 15, 25, 30, 45, 60, 80, 110, 145, 190, 250, 320, 400, 450]

# Wind energy production data (in TWh)
us_wind = [20, 30, 40, 50, 65, 80, 100, 125, 150, 175, 200, 225, 250, 280]
germany_wind = [18, 25, 32, 40, 48, 55, 65, 75, 85, 95, 105, 115, 125, 135]
china_wind = [15, 25, 40, 55, 70, 90, 110, 140, 170, 210, 260, 310, 370, 430]

# Error margins (± in TWh)
us_errors = [2, 3, 2, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
germany_errors = [1, 2, 3, 4, 3, 3, 4, 5, 4, 5, 6, 7, 8, 9]
china_errors = [5, 4, 6, 7, 9, 12, 15, 20, 25, 30, 35, 40, 45, 50]

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Solar energy production with error bars
axs[0].errorbar(years, us_production, yerr=us_errors, fmt='-o', capsize=3, label='United States', color='tab:blue')
axs[0].errorbar(years, germany_production, yerr=germany_errors, fmt='-s', capsize=3, label='Germany', color='tab:green')
axs[0].errorbar(years, china_production, yerr=china_errors, fmt='-^', capsize=3, label='China', color='tab:red')

# Wind energy production without error bars
axs[1].plot(years, us_wind, '-o', label='United States Wind', color='tab:cyan')
axs[1].plot(years, germany_wind, '-s', label='Germany Wind', color='tab:olive')
axs[1].plot(years, china_wind, '-^', label='China Wind', color='tab:purple')

# Customizing the first subplot for solar energy
axs[0].set_title('Solar Energy Production Trends (2010-2023)\nComparison of Leading Nations', fontsize=16)
axs[0].set_ylabel('Production (TWh)', fontsize=14)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(title='Countries (Solar)', loc='upper left', fontsize=10)

# Customizing the second subplot for wind energy
axs[1].set_title('Wind Energy Production Trends (2010-2023)', fontsize=16)
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Production (TWh)', fontsize=14)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].legend(title='Countries (Wind)', loc='upper left', fontsize=10)

# Setting x-ticks for both plots
plt.xticks(years, rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()