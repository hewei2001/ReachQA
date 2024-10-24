import matplotlib.pyplot as plt
import numpy as np

# Define the years and faculties
years = ['2018', '2019', '2020', '2021', '2022']
faculties = ['Science', 'Arts', 'Engineering']

# Enrollment data (in hundreds)
# Modified data for clarity and diversity
data = np.array([
    [50, 40, 30],  # 2018
    [55, 42, 33],  # 2019
    [58, 38, 36],  # 2020
    [62, 35, 43],  # 2021
    [66, 30, 49],  # 2022
])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each faculty
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot the stacked bar chart
bottoms = np.zeros(len(years))
for i, (faculty, color) in enumerate(zip(faculties, colors)):
    ax.bar(years, data[:, i], bottom=bottoms, label=faculty, color=color, alpha=0.8)
    bottoms += data[:, i]

# Customize the chart
ax.set_title("University Enrollment Trends (2018-2022)\nFaculty Contribution Over the Years", fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Enrollment (Hundreds)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend
ax.legend(title='Faculties', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Annotate values on each bar segment
for i in range(len(years)):
    y = 0
    for j in range(len(faculties)):
        ax.text(i, y + data[i, j] / 2, f"{data[i, j]}", ha='center', va='center', color='white', fontsize=9)
        y += data[i, j]

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()