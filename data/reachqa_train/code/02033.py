import matplotlib.pyplot as plt
import numpy as np

# Extended years for the X-axis
years = np.arange(2000, 2031)

# Extended Global Knowledge Index values for each field
technology_index = [40 + 3*np.sin(0.3*x) + 5*np.log(x+1) for x in range(len(years))]
environment_index = [45 + 2*np.cos(0.2*x) + 4*np.sqrt(x) for x in range(len(years))]
medicine_index = [48 + 1.5*np.sin(0.2*x + np.pi/4) + 3.5*np.sqrt(x) for x in range(len(years))]
history_index = [35 + np.sin(0.5*x) + 2*x/10 for x in range(len(years))]
physics_index = [50 + np.cos(0.4*x + np.pi/6) + 2.5*np.log(x+1) for x in range(len(years))]
mathematics_index = [38 + 1.2*np.sin(0.25*x + np.pi/3) + 2.8*np.sqrt(x) for x in range(len(years))]

# Creating a figure with multiple subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 10))

# Plotting the line chart
ax[0].plot(years, technology_index, marker='o', linestyle='-', linewidth=2, color='b', label='Technology')
ax[0].plot(years, environment_index, marker='s', linestyle='--', linewidth=2, color='g', label='Environment')
ax[0].plot(years, medicine_index, marker='^', linestyle='-.', linewidth=2, color='r', label='Medicine')
ax[0].plot(years, history_index, marker='d', linestyle=':', linewidth=2, color='m', label='History')
ax[0].plot(years, physics_index, marker='x', linestyle='-', linewidth=2, color='c', label='Physics')
ax[0].plot(years, mathematics_index, marker='p', linestyle='--', linewidth=2, color='orange', label='Mathematics')

# Adding labels and title
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Global Knowledge Index')
ax[0].set_title('Two Decades of Knowledge Growth\nA Comparative Analysis (2000-2030)', fontweight='bold')

# Adding grid and legend
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(title='Fields of Knowledge', loc='upper left', fontsize=9)

# Annotate specific data points
ax[0].annotate('Tech Breakthrough', xy=(2025, technology_index[25]), xytext=(2018, 80),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)
ax[0].annotate('Medicine Peak', xy=(2015, medicine_index[15]), xytext=(2008, 65),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Creating a subplot for statistical insights
moving_avg = np.convolve(technology_index, np.ones(5)/5, mode='valid')

ax[1].plot(years[2:-2], moving_avg, color='blue', linestyle='-', linewidth=2, label='Tech 5-Year Moving Average')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('5-Year Moving Average')
ax[1].set_title('Statistical Insights on Technology', fontweight='bold')

# Adding grid and legend
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend(loc='upper left', fontsize=9)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()