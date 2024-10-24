import matplotlib.pyplot as plt
import numpy as np

# Define the months for plotting
months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Yield data in tons for each fruit per month
apples_yield = [10, 12, 15, 18, 22, 30, 50, 65, 55, 40, 25, 15]
oranges_yield = [30, 45, 60, 55, 50, 45, 35, 30, 28, 25, 30, 35]
grapes_yield = [5, 8, 12, 18, 30, 50, 60, 75, 80, 70, 50, 30]

# Additional data for temperature (dummy data)
temperature = [4, 6, 10, 15, 20, 25, 30, 28, 24, 18, 10, 6]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Primary line chart for fruit yields
ax1.plot(months, apples_yield, marker='o', linestyle='-', color='#FF9999', label='Apples', linewidth=2)
ax1.plot(months, oranges_yield, marker='o', linestyle='--', color='#FFA500', label='Oranges', linewidth=2)
ax1.plot(months, grapes_yield, marker='o', linestyle=':', color='#9932CC', label='Grapes', linewidth=2)

# Title and labels
ax1.set_title("Seasonal Trends in Fruit Harvesting\nWith Temperature Correlation", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Yield (tons)', fontsize=14, color='black')
ax1.set_xticks(months)
ax1.set_xticklabels(month_names, rotation=45, ha='right')

# Legend for fruit yields
ax1.legend(loc='upper left', title="Fruit Type", fontsize=12)

# Grid for better readability
ax1.grid(linestyle='--', alpha=0.5)

# Adding temperature line to the plot
ax2 = ax1.twinx()
ax2.plot(months, temperature, color='blue', linewidth=2, linestyle='-', marker='s', label='Temperature (°C)')
ax2.set_ylabel('Temperature (°C)', fontsize=14, color='blue')
ax2.legend(loc='upper right', fontsize=12)

# Annotating peak yields
ax1.annotate('Peak Harvest', xy=(8, 65), xytext=(5, 75),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=11, color='#FF9999')
ax1.annotate('Peak Harvest', xy=(2, 45), xytext=(3, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=11, color='#FFA500')
ax1.annotate('Peak Harvest', xy=(9, 80), xytext=(10, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=11, color='#9932CC')

# Highlighting important periods
ax1.axvspan(3, 5, color='lightgreen', alpha=0.1)
ax1.axvspan(6, 9, color='yellow', alpha=0.1)
ax1.text(4, 90, 'Spring Bloom', fontsize=12, color='green', ha='center')
ax1.text(7.5, 90, 'Summer Harvest Season', fontsize=12, color='darkorange', ha='center')

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()