import matplotlib.pyplot as plt
import numpy as np

# Data Setup for the Original Plot
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
rentals = np.array([12, 15, 18, 22, 25, 30, 35, 33, 28, 24, 20, 18])

# Additional Data Setup for the New Plot
avg_temp = np.array([3, 4, 7, 11, 16, 19, 22, 21, 18, 13, 8, 4])  # Average monthly temperatures

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the line chart for bike rentals
ax1.plot(months, rentals, marker='o', linestyle='-', color='darkblue', linewidth=2, label='Bike Rentals')
annotations = {
    'Mar': ('Spring Promo', 18),
    'Jun': ('Bike Fest', 30),
    'Sep': ('Back to School', 28),
}
for month, (text, value) in annotations.items():
    ax1.annotate(
        text,
        xy=(month, value),
        xytext=(0, 10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='orange'),
        fontsize=10,
        color='red'
    )

ax1.set_title('Cycle City: Urban Bicycle Sharing Trends\nin Greenford - 2022', fontsize=16, fontweight='bold', pad=10)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Bike Rentals (in thousands)', fontsize=12)
ax1.set_ylim(0, 40)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, rotation=45, fontsize=10)
ax1.legend(loc='upper left', fontsize=10)

# Plot the bar chart for average temperatures
ax2.bar(months, avg_temp, color='coral', alpha=0.7)
ax2.set_title('Average Monthly Temperatures\nin Greenford - 2022', fontsize=16, fontweight='bold', pad=10)
ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Temperature (°C)', fontsize=12)
ax2.set_ylim(0, 25)
ax2.grid(True, linestyle='--', alpha=0.5, axis='y')
ax2.set_xticks(np.arange(len(months)))
ax2.set_xticklabels(months, rotation=45, fontsize=10)

# Adjust the layout for clarity
plt.tight_layout()

# Show the plots
plt.show()