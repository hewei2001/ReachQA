import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2050, 2061)

# Mineral resource extraction data in arbitrary units (e.g., tons)
iron = [50, 55, 62, 70, 78, 87, 97, 108, 120, 133, 147]
magnesium = [30, 35, 40, 46, 52, 59, 67, 75, 84, 94, 105]
silicon = [20, 22, 25, 29, 34, 40, 47, 55, 64, 74, 85]
helium3 = [5, 6, 8, 10, 13, 17, 22, 28, 35, 43, 52]

# Compute cumulative data for annotation purposes
cumulative_minerals = np.array(iron) + np.array(magnesium) + np.array(silicon) + np.array(helium3)

# Set up the plot with a gradient background
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_facecolor('#eafff5')
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.8)

# Create stacked bar chart with a gradient color palette
colors = ['#ff6f69', '#ffcc5c', '#88d8b0', '#6b5b95']
ax.bar(years, iron, label='Iron', color=colors[0], width=0.6)
ax.bar(years, magnesium, bottom=iron, label='Magnesium', color=colors[1], width=0.6)
ax.bar(years, silicon, bottom=np.array(iron) + np.array(magnesium), label='Silicon', color=colors[2], width=0.6)
ax.bar(years, helium3, bottom=np.array(iron) + np.array(magnesium) + np.array(silicon), label='Helium-3', color=colors[3], width=0.6)

# Add annotations for significant data points
for i, (year, cum_value) in enumerate(zip(years, cumulative_minerals)):
    ax.text(year, cum_value + 5, f'{cum_value} tons', ha='center', va='bottom', fontsize=9, color='black')

# Add title and labels
ax.set_title("Mineral Resource Extraction on Mars Colony\nGrowth from 2050 to 2060", fontsize=18)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Resource Extraction (Tons)", fontsize=14)

# Add legend
ax.legend(title='Minerals', loc='upper left', fontsize=11)

# Adjust x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a subplot for cumulative resource extraction
cumulative_plot = ax.twinx()
cumulative_plot.plot(years, cumulative_minerals, color='purple', linestyle='--', marker='o', label='Total Extraction')
cumulative_plot.set_ylabel("Total Resource Extraction (Tons)", fontsize=14, color='purple')
cumulative_plot.legend(loc='upper right', fontsize=11)
cumulative_plot.yaxis.label.set_color('purple')
cumulative_plot.tick_params(axis='y', labelcolor='purple')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()