import matplotlib.pyplot as plt
import numpy as np

# Define the years for which data is available
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

# Define the cuisines being analyzed
cuisines = ["Indian", "Mediterranean", "Mexican", "Thai", "Middle Eastern"]

# Spice usage data for each cuisine across the years (in tons)
spice_usage = np.array([
    [50, 55, 60, 65, 70, 80],  # Indian
    [40, 45, 47, 50, 54, 60],  # Mediterranean
    [30, 35, 40, 43, 47, 55],  # Mexican
    [25, 28, 33, 36, 40, 45],  # Thai
    [20, 22, 25, 28, 30, 35]   # Middle Eastern
])

# Calculate average spice usage per year across all cuisines for the line plot
avg_spice_usage = np.mean(spice_usage, axis=0)

# Hypothetical global spice price index data
spice_price_index = [100, 105, 110, 120, 130, 145]

# Setup figure and axes for the stacked bar chart
fig, ax1 = plt.subplots(figsize=(14, 9))

# Define color palette for the bars
colors = ['#E57373', '#FFD54F', '#4DB6AC', '#9575CD', '#F06292']

# Plotting stacked bar chart
bottom_values = np.zeros(len(years))
for idx, cuisine in enumerate(cuisines):
    ax1.bar(years, spice_usage[idx], bottom=bottom_values, color=colors[idx], label=cuisine, alpha=0.85)
    bottom_values += spice_usage[idx]

# Adding title and labels
ax1.set_title('Culinary Adventures: Spice Usage in Global Cuisines\nand Impact of Spice Price Index (2015-2020)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Spice Usage (in tons)', fontsize=12)
ax1.set_xticks(years)

# Adding a secondary y-axis for the spice price index
ax2 = ax1.twinx()
ax2.set_ylabel('Spice Price Index', fontsize=12, color='tab:blue')
ax2.plot(years, spice_price_index, color='tab:blue', marker='o', linestyle='--', linewidth=2.5, label='Spice Price Index')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Adding the average spice usage line plot
ax1.plot(years, avg_spice_usage, color='tab:orange', marker='s', linestyle='-', linewidth=2, label='Avg Spice Usage')

# Adding legends
bar_legend = ax1.legend(title='Cuisines', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))
line_legend = ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.05, 0.95))

# Adding a grid to enhance readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure no overlap of elements
plt.tight_layout()

# Display the plot
plt.show()