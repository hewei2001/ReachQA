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

# Plot setup
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the line chart for each fruit
ax.plot(months, apples_yield, marker='o', linestyle='-', color='#FF9999', label='Apples', linewidth=2)
ax.plot(months, oranges_yield, marker='o', linestyle='-', color='#FFA500', label='Oranges', linewidth=2)
ax.plot(months, grapes_yield, marker='o', linestyle='-', color='#9932CC', label='Grapes', linewidth=2)

# Title and labels
ax.set_title("Seasonal Trends in Fruit Harvesting", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Yield (tons)', fontsize=14)
ax.set_xticks(months)
ax.set_xticklabels(month_names, rotation=45, ha='right')

# Adding legend
ax.legend(loc='upper right', title="Fruit Type", fontsize=12)

# Grid for better readability
ax.grid(linestyle='--', alpha=0.5)

# Annotating peak yields
ax.annotate('Peak Harvest', xy=(8, 65), xytext=(5, 75),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#FF9999')
ax.annotate('Peak Harvest', xy=(2, 45), xytext=(3, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#FFA500')
ax.annotate('Peak Harvest', xy=(9, 80), xytext=(10, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11, color='#9932CC')

# Highlighting the summer period as crucial for harvest
ax.axvspan(6, 9, color='yellow', alpha=0.1)
ax.text(7.5, 90, 'Summer Harvest Season', fontsize=12, color='darkorange', ha='center')

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()