import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the decades and fruit consumption data in millions
decades = np.array([1980, 1990, 2000, 2010, 2020])
apples = np.array([30, 28, 35, 40, 45])
bananas = np.array([25, 30, 28, 26, 30])
cherries = np.array([10, 15, 20, 25, 30])
dates = np.array([5, 8, 10, 12, 15])
elderberries = np.array([3, 5, 7, 10, 12])

# Additional data for population growth (in billions) to showcase on a secondary axis
population_growth = np.array([4.4, 5.3, 6.1, 6.9, 7.8])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Stackplot for fruit consumption
colors = ['#ff9999', '#ffcc66', '#66c2a5', '#8da0cb', '#e78ac3']
ax1.stackplot(decades, apples, bananas, cherries, dates, elderberries,
             labels=['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries'],
             colors=colors, alpha=0.8)

# Overlay line plots for detailed trends
markers = ['o', 's', '^', 'D', 'p']
for fruit_data, color, marker in zip([apples, bananas, cherries, dates, elderberries], colors, markers):
    ax1.plot(decades, fruit_data, marker=marker, color=color, alpha=0.8, linewidth=1.5)

# Population growth secondary axis
ax2 = ax1.twinx()
ax2.plot(decades, population_growth, 'k--', marker='x', linewidth=1.5, label='World Population (Billions)')
ax2.set_ylabel('World Population (Billions)', fontsize=12)

# Title and labels
ax1.set_title('Fruitopolis: A Five-Decade Journey\nThrough Fruity Delights & Population Trends', 
              fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Fruit Consumption (Millions)', fontsize=12)

# Add legends
legend_fruits = mpatches.Patch(color='grey', label='Fruit Consumption')
ax1.legend(loc='upper left', fontsize=10, handles=ax1.get_legend_handles_labels()[0] + [legend_fruits])
ax2.legend(loc='upper right', fontsize=10)

# Format the x-axis to display decades nicely
ax1.set_xticks(decades)
ax1.set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)

# Highlighting the peak year for apples
peak_year = decades[np.argmax(apples)]
peak_value = np.max(apples)
ax1.annotate(f'Peak Apples: {peak_value}M',
             xy=(peak_year, peak_value), 
             xytext=(peak_year - 5, peak_value + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, fontweight='bold')

# Grid lines for readability
ax1.grid(True, linestyle='--', alpha=0.5)

# Ensure labels are not cut off and fit the figure nicely
plt.tight_layout()

# Display the plot
plt.show()