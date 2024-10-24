import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Dolphin populations in thousands for each oceanic region
pacific_population = np.array([120, 125, 130, 135, 140, 138, 137, 142, 145, 147, 150])
atlantic_population = np.array([110, 113, 115, 118, 120, 123, 127, 130, 133, 137, 140])
indian_population = np.array([90, 92, 94, 97, 100, 105, 108, 112, 115, 117, 119])

# Calculate annual percentage change for each oceanic region
def calculate_percentage_change(data):
    return 100 * (data[1:] - data[:-1]) / data[:-1]

pacific_change = calculate_percentage_change(pacific_population)
atlantic_change = calculate_percentage_change(atlantic_population)
indian_change = calculate_percentage_change(indian_population)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Plot the line chart
ax1.plot(years, pacific_population, marker='o', linestyle='-', color='dodgerblue', linewidth=2, label='Pacific Ocean')
ax1.plot(years, atlantic_population, marker='s', linestyle='--', color='forestgreen', linewidth=2, label='Atlantic Ocean')
ax1.plot(years, indian_population, marker='^', linestyle='-.', color='orangered', linewidth=2, label='Indian Ocean')
ax1.set_title('Ocean Conservation Efforts:\nTracking Dolphin Populations Over Time', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Dolphin Population (Thousands)', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.axvspan(2015, 2017, color='lightblue', alpha=0.3, label='Pacific Success Initiative')
ax1.annotate('Pacific Success', xy=(2016, 138), xytext=(2014, 145),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue'),
             fontsize=10, color='blue')

# Plot the bar chart for percentage change
ind = np.arange(len(pacific_change))  # index for bar positions
width = 0.25  # bar width

ax2.bar(ind - width, pacific_change, width=width, color='dodgerblue', alpha=0.7, label='Pacific Ocean')
ax2.bar(ind, atlantic_change, width=width, color='forestgreen', alpha=0.7, label='Atlantic Ocean')
ax2.bar(ind + width, indian_change, width=width, color='orangered', alpha=0.7, label='Indian Ocean')
ax2.set_title('Annual Percentage Change in Dolphin Population', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Percentage Change (%)', fontsize=12, fontweight='bold')
ax2.set_xticks(ind)
ax2.set_xticklabels(years[1:])  # exclude the first year since change is computed from the second year onwards
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()