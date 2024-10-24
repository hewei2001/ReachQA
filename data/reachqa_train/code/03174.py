import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding average EV range data
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
avg_range = np.array([60, 75, 90, 120, 150, 200, 250])

# Create the plot with specified dimensions
plt.figure(figsize=(12, 6))

# Plot the line chart with markers
plt.plot(years, avg_range, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='Average Range')

# Annotate each data point with its value
for year, range_val in zip(years, avg_range):
    plt.annotate(f'{range_val} miles', xy=(year, range_val), 
                 xytext=(0, 10), textcoords='offset points',
                 ha='center', va='bottom', fontsize=9, color='darkgreen')

# Title and axis labels
plt.title('Evolution of Electric Vehicle Battery Range\nOver the Decades (1990-2020)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average EV Range (miles)', fontsize=12)

# Add a legend to explain the chart line
plt.legend(loc='upper left', fontsize=10)

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()