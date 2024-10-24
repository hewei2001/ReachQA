import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Years extended from 2000 to 2025
years = np.arange(2000, 2026)

# Health index data extended and new regions added
region_a_health = np.array([80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
                            70, 68, 67, 65, 64, 63, 62, 60, 58, 57, 
                            55, 53, 52, 51, 50, 49])
region_b_health = np.array([60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
                            80, 81, 82, 83, 84, 85])
region_c_health = np.array([85, 84, 83, 82, 81, 80, 79, 78, 77, 76,
                            75, 73, 72, 70, 69, 68, 66, 65, 63, 62, 
                            60, 58, 57, 55, 54, 53])
region_d_health = np.array([70, 69, 68, 67, 66, 65, 64, 63, 62, 61,
                            60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 
                            50, 49, 48, 47, 46, 45])

# Variability in measurements (Error bars)
region_a_error = np.array([3] * len(years))
region_b_error = np.array([4] * len(years))
region_c_error = np.array([2] * len(years))
region_d_error = np.array([3.5] * len(years))

# Set up the plot with subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Main plot: Health index with error bars
axs[0, 0].errorbar(years, region_a_health, yerr=region_a_error, fmt='-o', label='Region A', color='teal', capsize=5, alpha=0.8)
axs[0, 0].errorbar(years, region_b_health, yerr=region_b_error, fmt='-s', label='Region B', color='coral', capsize=5, alpha=0.8)
axs[0, 0].errorbar(years, region_c_health, yerr=region_c_error, fmt='-d', label='Region C', color='orchid', capsize=5, alpha=0.8)
axs[0, 0].errorbar(years, region_d_health, yerr=region_d_error, fmt='-^', label='Region D', color='navy', capsize=5, alpha=0.8)
axs[0, 0].set_title('Coral Reef Health Index Across Regions (2000-2025)', fontsize=12, fontweight='bold')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Health Index')
axs[0, 0].set_xticks(years[::2])  # Display every second year
axs[0, 0].set_yticks(np.arange(40, 90, 5))
axs[0, 0].legend(title='Regions', fontsize=9)
axs[0, 0].grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Second subplot: Moving average plot
window_size = 5
region_a_mavg = np.convolve(region_a_health, np.ones(window_size)/window_size, mode='valid')
region_b_mavg = np.convolve(region_b_health, np.ones(window_size)/window_size, mode='valid')
region_c_mavg = np.convolve(region_c_health, np.ones(window_size)/window_size, mode='valid')
region_d_mavg = np.convolve(region_d_health, np.ones(window_size)/window_size, mode='valid')

axs[0, 1].plot(years[window_size-1:], region_a_mavg, '-o', label='Region A', color='teal')
axs[0, 1].plot(years[window_size-1:], region_b_mavg, '-s', label='Region B', color='coral')
axs[0, 1].plot(years[window_size-1:], region_c_mavg, '-d', label='Region C', color='orchid')
axs[0, 1].plot(years[window_size-1:], region_d_mavg, '-^', label='Region D', color='navy')
axs[0, 1].set_title('5-Year Moving Average', fontsize=12)
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Avg Health Index')
axs[0, 1].grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Third subplot: Derivative plot (rate of change)
region_a_derivative = np.diff(region_a_health)
region_b_derivative = np.diff(region_b_health)
region_c_derivative = np.diff(region_c_health)
region_d_derivative = np.diff(region_d_health)

axs[1, 0].plot(years[1:], region_a_derivative, '-o', label='Region A', color='teal')
axs[1, 0].plot(years[1:], region_b_derivative, '-s', label='Region B', color='coral')
axs[1, 0].plot(years[1:], region_c_derivative, '-d', label='Region C', color='orchid')
axs[1, 0].plot(years[1:], region_d_derivative, '-^', label='Region D', color='navy')
axs[1, 0].set_title('Yearly Rate of Change', fontsize=12)
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Rate of Change')
axs[1, 0].grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Fourth subplot: Cumulative sum
region_a_cumsum = np.cumsum(region_a_health - np.mean(region_a_health))
region_b_cumsum = np.cumsum(region_b_health - np.mean(region_b_health))
region_c_cumsum = np.cumsum(region_c_health - np.mean(region_c_health))
region_d_cumsum = np.cumsum(region_d_health - np.mean(region_d_health))

axs[1, 1].plot(years, region_a_cumsum, '-o', label='Region A', color='teal')
axs[1, 1].plot(years, region_b_cumsum, '-s', label='Region B', color='coral')
axs[1, 1].plot(years, region_c_cumsum, '-d', label='Region C', color='orchid')
axs[1, 1].plot(years, region_d_cumsum, '-^', label='Region D', color='navy')
axs[1, 1].set_title('Cumulative Health Change', fontsize=12)
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Cumulative Index')
axs[1, 1].grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()