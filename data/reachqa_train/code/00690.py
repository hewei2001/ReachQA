import matplotlib.pyplot as plt
import numpy as np

# Define a broader range of years
years = np.array(range(2000, 2026))

# Internet usage percentages for each age group over a broader period
# Ensure all usage arrays have 26 elements, corresponding to the 26 years (2000-2025)
usage_0_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
usage_5_14 = np.array([5, 7, 10, 13, 15, 18, 21, 24, 28, 32, 35, 39, 43, 47, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94])
usage_15_24 = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86, 88, 90, 91, 92, 93, 94, 95])
usage_25_34 = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 89, 90, 91, 92, 93])
usage_35_44 = np.array([8, 10, 15, 18, 21, 25, 29, 33, 37, 41, 45, 49, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78])
usage_45_54 = np.array([5, 8, 12, 15, 18, 22, 26, 30, 34, 37, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 73, 75, 77, 79, 81])
usage_55_64 = np.array([2, 4, 6, 8, 10, 13, 16, 19, 22, 25, 28, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 59, 61, 63, 65, 67])
usage_65_plus = np.array([1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47])

# Stack the usage data
usage_data = np.vstack([usage_0_4, usage_5_14, usage_15_24, usage_25_34, usage_35_44, usage_45_54, usage_55_64, usage_65_plus])

# Create the area chart
fig, ax = plt.subplots(figsize=(16, 10))

# Plot each age group's internet usage using stackplot
colors = ['#fde0dd', '#fa9fb5', '#f768a1', '#c51b8a', '#7a0177', '#084594', '#2171b5', '#6baed6']
labels = ['Age 0-4', 'Age 5-14', 'Age 15-24', 'Age 25-34', 'Age 35-44', 'Age 45-54', 'Age 55-64', 'Age 65+']
ax.stackplot(years, usage_data, labels=labels, colors=colors, alpha=0.85)

# Add title and labels with proper line breaks
ax.set_title("Internet Usage Trends\nAcross Various Age Groups\nFrom 2000 to 2025", fontsize=18, fontweight='bold', pad=30)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Internet Usage (%)", fontsize=14)

# Add a legend
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1))

# Enhance readability with a grid
ax.grid(True, linestyle='--', alpha=0.6)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()