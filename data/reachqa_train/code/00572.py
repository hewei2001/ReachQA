import matplotlib.pyplot as plt
import numpy as np

# Data: Number of urban herb gardens established each month in three cities over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a = np.array([10, 15, 18, 22, 28, 35, 40, 42, 45, 50, 55, 60])
city_b = np.array([5, 8, 12, 15, 20, 25, 30, 35, 38, 42, 45, 50])
city_c = np.array([8, 11, 14, 19, 25, 30, 34, 36, 39, 41, 44, 48])

# Create an aggregated dataset for the bar plot
total_gardens = city_a + city_b + city_c

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Line plots for each city
ax1.plot(months, city_a, label='Greenfield City', marker='o', linestyle='-', color='forestgreen', linewidth=2)
ax1.plot(months, city_b, label='Sunnyvale Town', marker='o', linestyle='-', color='goldenrod', linewidth=2)
ax1.plot(months, city_c, label='Bluehills Village', marker='o', linestyle='-', color='steelblue', linewidth=2)

# Bar plot for total gardens
ax2 = ax1.twinx()
ax2.bar(months, total_gardens, alpha=0.3, color='gray', label='Total Gardens', width=0.4)

# Annotate data points with the number of new gardens for key months
highlight_months = [4, 10]  # Highlight May and November for significant growth
for i in highlight_months:
    ax1.annotate(f'{city_a[i]}', xy=(months[i], city_a[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='forestgreen')
    ax1.annotate(f'{city_b[i]}', xy=(months[i], city_b[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='goldenrod')
    ax1.annotate(f'{city_c[i]}', xy=(months[i], city_c[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='steelblue')
    ax2.annotate(f'{total_gardens[i]}', xy=(months[i], total_gardens[i]), xytext=(-5, -20), textcoords='offset points', fontsize=9, color='gray')

# Set chart titles and labels
ax1.set_title('The Rise of Home Gardening:\nMonthly Growth of Urban Herb Gardens', fontsize=16, pad=20, weight='bold')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Number of New Herb Gardens (Cities)', fontsize=12)
ax2.set_ylabel('Total Number of Herb Gardens', fontsize=12, color='gray')

# Add legends
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1), title='Cities')
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1))

# Grid and layout adjustment
ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()