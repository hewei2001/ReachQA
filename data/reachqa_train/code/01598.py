import matplotlib.pyplot as plt
import numpy as np

# Define gadget categories and years
gadgets = ['Smartphones', 'Laptops', 'Smartwatches', 'Tablets', 'Gaming Consoles']
years = ['2018', '2019', '2020', '2021', '2022', '2023']

# Market share data for each gadget over the years
data = np.array([
    [35, 33, 30, 28, 25, 22],
    [25, 26, 27, 26, 25, 24],
    [10, 12, 15, 18, 20, 22],
    [20, 18, 17, 15, 14, 13],
    [10, 11, 11, 13, 16, 19],
])

# Calculate cumulative market share of Smart Devices (Smartphones, Smartwatches, Tablets)
smart_devices = data[0] + data[2] + data[3]

# Calculate year-over-year growth rate for Gaming Consoles
gaming_growth_rate = np.diff(data[4], prepend=data[4][0]) / data[4][0] * 100

# Create a 1x2 subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# Bar Chart (Original)
bar_width = 0.15
x_positions = np.arange(len(years))
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']

for i, (gadget, color) in enumerate(zip(gadgets, colors)):
    ax1.bar(x_positions + i * bar_width, data[i], width=bar_width, label=gadget, color=color, edgecolor='black')

ax1.set_title('Market Share Distribution of Consumer Tech Gadgets\n(2018-2023)', fontsize=14)
ax1.set_xlabel('Year')
ax1.set_ylabel('Market Share (%)')
ax1.set_xticks(x_positions + bar_width * 2)
ax1.set_xticklabels(years)
ax1.legend(title="Gadget Categories")

for i in range(len(years)):
    for j in range(len(gadgets)):
        ax1.text(x_positions[i] + j * bar_width, data[j, i] + 0.5, f"{data[j, i]}%", ha='center', va='bottom', fontsize=9)

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Line Chart (New)
ax2.plot(years, smart_devices, marker='o', color='#1f77b4', label='Smart Devices (Cumulative)')
ax2.set_title('Cumulative Market Share & Gaming Consoles Growth Rate\n(2018-2023)', fontsize=14)
ax2.set_xlabel('Year')
ax2.set_ylabel('Cumulative Market Share (%)', color='#1f77b4')
ax2.tick_params(axis='y', labelcolor='#1f77b4')

# Secondary y-axis for growth rate
ax3 = ax2.twinx()
ax3.plot(years, gaming_growth_rate, marker='x', color='#ff7f0e', linestyle='--', label='Gaming Consoles Growth Rate')
ax3.set_ylabel('Growth Rate (%)', color='#ff7f0e')
ax3.tick_params(axis='y', labelcolor='#ff7f0e')

# Legends for line chart
lns1, labs1 = ax2.get_legend_handles_labels()
lns2, labs2 = ax3.get_legend_handles_labels()
ax2.legend(lns1 + lns2, labs1 + labs2, loc='upper left')

plt.show()