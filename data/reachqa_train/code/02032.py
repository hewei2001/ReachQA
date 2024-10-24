import matplotlib.pyplot as plt
import numpy as np

# Years for the X-axis
years = np.arange(2010, 2021)

# Global Knowledge Index values for each field
technology_index = [50, 55, 60, 65, 70, 75, 80, 85, 88, 92, 95]
environment_index = [40, 42, 44, 48, 50, 55, 60, 62, 65, 68, 70]
medicine_index = [45, 50, 55, 58, 60, 63, 68, 72, 75, 77, 80]
history_index = [30, 35, 37, 40, 43, 46, 50, 54, 58, 60, 65]

# Plotting the line chart
plt.figure(figsize=(12, 7))

# Plot each line with different styles
plt.plot(years, technology_index, marker='o', linestyle='-', linewidth=2, color='b', label='Technology')
plt.plot(years, environment_index, marker='s', linestyle='--', linewidth=2, color='g', label='Environment')
plt.plot(years, medicine_index, marker='^', linestyle='-.', linewidth=2, color='r', label='Medicine')
plt.plot(years, history_index, marker='d', linestyle=':', linewidth=2, color='m', label='History')

# Adding labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Global Knowledge Index', fontsize=12)
plt.title('Decade of Insights:\nGlobal Knowledge Index (2010-2020)', fontsize=14, fontweight='bold', pad=20)

# Adding grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adding a legend
plt.legend(title='Fields of Knowledge', loc='upper left', fontsize=10)

# Annotate specific important data points
plt.annotate('Breakthrough Year', xy=(2018, 85), xytext=(2014, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjusting layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()