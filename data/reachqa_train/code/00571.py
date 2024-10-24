import matplotlib.pyplot as plt
import numpy as np

# Data: Number of urban herb gardens established each month in three cities over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a = np.array([10, 15, 18, 22, 28, 35, 40, 42, 45, 50, 55, 60])
city_b = np.array([5, 8, 12, 15, 20, 25, 30, 35, 38, 42, 45, 50])
city_c = np.array([8, 11, 14, 19, 25, 30, 34, 36, 39, 41, 44, 48])

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines for each city
ax.plot(months, city_a, label='Greenfield City', marker='o', linestyle='-', color='forestgreen', linewidth=2)
ax.plot(months, city_b, label='Sunnyvale Town', marker='o', linestyle='-', color='goldenrod', linewidth=2)
ax.plot(months, city_c, label='Bluehills Village', marker='o', linestyle='-', color='steelblue', linewidth=2)

# Annotate data points with the number of new gardens for key months
highlight_months = [4, 10]  # Highlight May and November for significant growth
for i in highlight_months:
    ax.annotate(f'{city_a[i]}', xy=(months[i], city_a[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=9, color='forestgreen')
    ax.annotate(f'{city_b[i]}', xy=(months[i], city_b[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=9, color='goldenrod')
    ax.annotate(f'{city_c[i]}', xy=(months[i], city_c[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=9, color='steelblue')

# Set chart title and labels
ax.set_title('The Rise of Home Gardening:\nMonthly Growth of Urban Herb Gardens', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of New Herb Gardens', fontsize=12)

# Add a legend to distinguish between cities
ax.legend(title='Cities', loc='upper left')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to ensure nothing overlaps
plt.tight_layout()

# Display the plot
plt.show()