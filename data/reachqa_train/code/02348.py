import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d

# Extended years from 2000 to 2023
years = np.arange(2000, 2024)

# Extend the dataset for more complexity and new regions
north_america_speeds = [0.5, 0.7, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18, 20, 25, 30, 32, 35, 40, 43, 45, 48]
europe_speeds = [0.4, 0.6, 0.8, 1.2, 1.5, 2.2, 3, 4, 5, 6.5, 7.5, 9, 10, 13, 15, 18, 22, 25, 28, 31, 35, 38, 40, 42]
asia_speeds = [0.3, 0.5, 0.6, 0.9, 1.2, 1.8, 2.5, 3, 4, 5, 6, 9, 11, 13, 17, 21, 24, 27, 30, 34, 37, 39, 42, 45]
africa_speeds = [0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.2, 1.5, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 28, 30, 32, 35]
south_america_speeds = [0.2, 0.3, 0.4, 0.6, 0.9, 1.2, 1.5, 2, 3, 4, 5, 7, 9, 11, 14, 17, 20, 23, 27, 29, 32, 35, 38, 41]

# New dataset for a different technology: Mobile speeds
mobile_speeds = [0.1, 0.15, 0.2, 0.3, 0.45, 0.6, 0.9, 1.2, 1.6, 2, 3, 4.5, 6, 7, 10, 12, 14, 18, 21, 25, 28, 31, 34, 37]

# Set up the figure and axis
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 10))

# Define colors for each line
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Main plot for fixed internet speeds
axs[0].plot(years, north_america_speeds, marker='o', color=colors[0], label='North America', linewidth=2)
axs[0].plot(years, europe_speeds, marker='s', color=colors[1], label='Europe', linewidth=2)
axs[0].plot(years, asia_speeds, marker='^', color=colors[2], label='Asia', linewidth=2)
axs[0].plot(years, africa_speeds, marker='D', color=colors[3], label='Africa', linewidth=2)
axs[0].plot(years, south_america_speeds, marker='v', color=colors[4], label='South America', linewidth=2)

# Plot the moving average for North America as a complex analytical feature
na_moving_avg = uniform_filter1d(north_america_speeds, size=3)
axs[0].plot(years, na_moving_avg, linestyle='--', color=colors[5], label='North America Avg', linewidth=2)

# Advanced Annotations (e.g., year 2020 global pandemic)
axs[0].annotate('COVID-19 Pandemic', xy=(2020, 35), xytext=(2015, 45),
                arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, fontstyle='italic')

# Set title, labels, and grid for the first subplot
axs[0].set_title('Evolution of Internet Speeds: 2000-2023', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Internet Speed (Mbps)', fontsize=12)
axs[0].grid(visible=True, linestyle='--', alpha=0.5)
axs[0].legend(loc='upper left', fontsize=9)

# Second subplot for mobile technology speeds
axs[1].plot(years, mobile_speeds, marker='x', color=colors[5], label='Mobile Technology', linewidth=2)
axs[1].set_title('Growth of Mobile Internet Speeds', fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Mobile Internet Speed (Mbps)', fontsize=12)
axs[1].grid(visible=True, linestyle='--', alpha=0.5)
axs[1].legend(loc='upper left', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()