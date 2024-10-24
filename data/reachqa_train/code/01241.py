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

# Plotting the stacked area chart
plt.figure(figsize=(12, 7))
plt.fill_between(months, 0, cumulative_sparrows, color='#FFDD44', alpha=0.6, label='Sparrows')
plt.fill_between(months, cumulative_sparrows, cumulative_robins, color='#77AAFF', alpha=0.6, label='Robins')
plt.fill_between(months, cumulative_robins, cumulative_blue_jays, color='#33DDDD', alpha=0.6, label='Blue Jays')
plt.fill_between(months, cumulative_blue_jays, cumulative_finches, color='#FF7777', alpha=0.6, label='Finches')

# Title and labels
plt.title("Seasonal Bird Population Dynamics\nin Urban Parks", fontsize=14, weight='bold', pad=20)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Population Density (Birds per sq. km)", fontsize=12)

# Avoid label overlap
plt.xticks(rotation=45)

# Adding grid for better value estimation
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
plt.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()