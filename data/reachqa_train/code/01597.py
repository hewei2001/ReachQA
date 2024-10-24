import matplotlib.pyplot as plt
import numpy as np

# Define categories and years for the analysis
gadgets = ['Smartphones', 'Laptops', 'Smartwatches', 'Tablets', 'Gaming Consoles']
years = ['2018', '2019', '2020', '2021', '2022', '2023']

# Market share data as a percentage for each gadget category over the years
data = np.array([
    [35, 33, 30, 28, 25, 22],  # Smartphones
    [25, 26, 27, 26, 25, 24],  # Laptops
    [10, 12, 15, 18, 20, 22],  # Smartwatches
    [20, 18, 17, 15, 14, 13],  # Tablets
    [10, 11, 11, 13, 16, 19],  # Gaming Consoles
])

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
x_positions = np.arange(len(years))

# Define a distinct color for each gadget category
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']

# Plot each gadget category with its corresponding data
for i, (gadget, color) in enumerate(zip(gadgets, colors)):
    ax.bar(x_positions + i * bar_width, data[i], width=bar_width, label=gadget, color=color, edgecolor='black')

# Set the title, labels, and customize the x-ticks
ax.set_title('Market Share Distribution of Consumer Tech Gadgets\n(2018-2023)', fontsize=16, pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_xticks(x_positions + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title="Gadget Categories", title_fontsize='13', fontsize='11')

# Add percentage labels above each bar
for i in range(len(years)):
    for j in range(len(gadgets)):
        ax.text(x_positions[i] + j * bar_width, data[j, i] + 0.5, f"{data[j, i]}%", ha='center', va='bottom', fontsize=9)

# Improve readability by rotating the x-axis labels if necessary
plt.xticks(rotation=0)

# Enable grid for the y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to ensure elements fit well
plt.tight_layout()

# Display the plot
plt.show()