import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Average annual ocean surface temperatures (in degrees Celsius)
atlantic_temps = np.array([22.5, 22.7, 22.9, 23.1, 23.3, 23.5, 23.7, 23.9, 24.0, 24.2, 24.4])
pacific_temps = np.array([21.0, 21.2, 21.4, 21.6, 21.7, 21.9, 22.1, 22.3, 22.4, 22.6, 22.8])
indian_temps = np.array([26.0, 26.1, 26.3, 26.5, 26.6, 26.8, 26.9, 27.1, 27.2, 27.4, 27.5])

# Calculate the annual change in temperature for additional insights
atlantic_change = np.diff(atlantic_temps)
pacific_change = np.diff(pacific_temps)
indian_change = np.diff(indian_temps)

# Create a subplot with a line plot and a bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})

# Line Chart: Ocean Temperatures
ax1.plot(years, atlantic_temps, color='royalblue', linewidth=2, marker='o', markersize=6, label='Atlantic Ocean')
ax1.plot(years, pacific_temps, color='coral', linewidth=2, marker='s', markersize=6, label='Pacific Ocean')
ax1.plot(years, indian_temps, color='goldenrod', linewidth=2, marker='^', markersize=6, label='Indian Ocean')

# Annotate each line with the final temperature
ax1.annotate(f"{atlantic_temps[-1]}°C", xy=(years[-1], atlantic_temps[-1]), xytext=(years[-1] + 0.2, atlantic_temps[-1] - 0.2),
             arrowprops=dict(facecolor='royalblue', arrowstyle='->'), fontsize=9, color='navy')
ax1.annotate(f"{pacific_temps[-1]}°C", xy=(years[-1], pacific_temps[-1]), xytext=(years[-1] + 0.2, pacific_temps[-1] - 0.2),
             arrowprops=dict(facecolor='coral', arrowstyle='->'), fontsize=9, color='darkred')
ax1.annotate(f"{indian_temps[-1]}°C", xy=(years[-1], indian_temps[-1]), xytext=(years[-1] + 0.2, indian_temps[-1] - 0.2),
             arrowprops=dict(facecolor='goldenrod', arrowstyle='->'), fontsize=9, color='goldenrod')

# Adding title, labels, and customizations
ax1.set_title('Climate Change Impact on Ocean Temperatures:\nA Decade of Change (2010-2020)', fontsize=14, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Avg Surface Temperature (°C)', fontsize=12)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Ocean', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), borderaxespad=0.)

# Bar Chart: Annual Change in Temperatures
ax2.bar(years[1:], atlantic_change, color='royalblue', alpha=0.7, label='Atlantic Change')
ax2.bar(years[1:], pacific_change, color='coral', alpha=0.7, label='Pacific Change', bottom=atlantic_change)
ax2.bar(years[1:], indian_change, color='goldenrod', alpha=0.7, label='Indian Change', bottom=atlantic_change + pacific_change)

# Adding title, labels, and customizations
ax2.set_title('Annual Change in Ocean Temperatures\n(2011-2020)', fontsize=14, weight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Temperature Change (°C)', fontsize=12)
ax2.set_xticks(years[1:])
ax2.legend(title='Change by Ocean', fontsize=10, loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()