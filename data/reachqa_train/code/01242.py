import matplotlib.pyplot as plt
import numpy as np

# Data for bird population densities in urban parks over months
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Manually constructed population densities (birds per sq. km)
sparrows = np.array([15, 18, 20, 25, 35, 40, 50, 45, 30, 25, 20, 18])
robins = np.array([10, 12, 15, 20, 25, 30, 20, 15, 10, 8, 6, 5])
blue_jays = np.array([5, 6, 8, 10, 12, 14, 18, 17, 14, 12, 10, 8])
finches = np.array([2, 3, 5, 8, 12, 15, 10, 7, 5, 3, 2, 1])

# Cumulative population for stacked plotting
cumulative_sparrows = sparrows
cumulative_robins = cumulative_sparrows + robins
cumulative_blue_jays = cumulative_robins + blue_jays
cumulative_finches = cumulative_blue_jays + finches

# Overall population for line plot (simple moving average as example)
total_population = cumulative_finches
moving_avg = np.convolve(total_population, np.ones(3)/3, mode='valid')

# Plotting
plt.figure(figsize=(14, 8))
plt.fill_between(months, 0, cumulative_sparrows, color='#FFDD44', alpha=0.6, label='Sparrows')
plt.fill_between(months, cumulative_sparrows, cumulative_robins, color='#77AAFF', alpha=0.6, label='Robins')
plt.fill_between(months, cumulative_robins, cumulative_blue_jays, color='#33DDDD', alpha=0.6, label='Blue Jays')
plt.fill_between(months, cumulative_blue_jays, cumulative_finches, color='#FF7777', alpha=0.6, label='Finches')

# Overlay line plot
plt.plot(months[1:-1], moving_avg, color='black', linestyle='-', marker='o', markersize=6, label='Moving Avg Trend', linewidth=2)

# Title and labels
plt.title("Seasonal Bird Population Dynamics\nin Urban Parks with Trend Analysis", fontsize=16, weight='bold', pad=20)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Population Density (Birds per sq. km)", fontsize=12)

# Rotation for x-ticks
plt.xticks(rotation=45)

# Grid, legend, and layout adjustments
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()

# Annotations for peak months
peak_month = months[np.argmax(total_population)]
peak_value = np.max(total_population)
plt.annotate(f'Peak: {peak_value}', xy=(peak_month, peak_value), xytext=(peak_month, peak_value+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Show plot
plt.show()