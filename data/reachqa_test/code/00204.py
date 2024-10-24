import matplotlib.pyplot as plt
import numpy as np

# Data: Years and the average number of daily cyclists in thousands
years = np.arange(2010, 2021)
daily_cyclists = np.array([5, 6, 9, 14, 18, 23, 20, 28, 35, 40, 47])

# Data for weather conditions: Average number of rainy days per year
rainy_days = np.array([120, 118, 115, 110, 108, 105, 110, 100, 95, 92, 90])

# Calculate moving average for a smoother trend line
window_size = 3
moving_average = np.convolve(daily_cyclists, np.ones(window_size)/window_size, mode='valid')

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the original data
ax1.plot(years, daily_cyclists, marker='o', linestyle='-', color='#2C7BB6', label='Daily Cyclists (in thousands)', linewidth=2)

# Plot the moving average
ax1.plot(years[window_size-1:], moving_average, linestyle='--', color='#D7191C', linewidth=2, label='3-Year Moving Average')

# Add a bar chart for average rainy days per year
ax2 = ax1.twinx()
ax2.bar(years, rainy_days, color='gray', alpha=0.3, label='Rainy Days', width=0.4)
ax2.set_ylabel('Average Rainy Days', fontsize=12)
ax2.set_ylim(80, 130)

# Annotate key events
ax1.annotate('Launch of Bike-Share Program', xy=(2015, 23), xytext=(2012.5, 32),
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='#D7191C')
ax1.annotate('New Cycling Lanes', xy=(2018, 35), xytext=(2016, 45),
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='#D7191C')

# Set titles and labels
ax1.set_title('Urban Cycling Trends in Cyclopolis\n(2010-2020) with Weather Influence', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Daily Cyclists (in thousands)', fontsize=12)

# Customize the grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Add legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

# Rotate x-axis labels for better readability
ax1.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()