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

# Setup figure and axes for the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define color palette for the bars
colors = ['#E57373', '#FFD54F', '#4DB6AC', '#9575CD', '#F06292']

# Plotting stacked bar chart
bottom_values = np.zeros(len(years))  # Initialize the base for stacking
for idx, cuisine in enumerate(cuisines):
    ax.bar(years, spice_usage[idx], bottom=bottom_values, color=colors[idx], label=cuisine, alpha=0.85)
    bottom_values += spice_usage[idx]  # Update the base for next stack

# Adding title and labels
ax.set_title('Culinary Adventures: Spice Usage\nin Global Cuisines (2015-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Spice Usage (in tons)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years)
ax.set_xlim(2014.5, 2020.5)  # Adding some buffer on x-axis

# Adding the legend
ax.legend(title='Cuisines', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adding a grid to enhance readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure no overlap of elements
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust space for legend

# Display the plot
plt.show()