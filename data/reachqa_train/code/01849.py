import matplotlib.pyplot as plt
import numpy as np

# Define the years and faculties
years = [str(year) for year in range(2015, 2023)]
faculties = ['Science', 'Arts', 'Engineering', 'Medicine', 'Business']

# Enrollment data (in hundreds), explicitly constructed
data = np.array([
    [45, 35, 25, 15, 20],  # 2015
    [48, 36, 28, 18, 22],  # 2016
    [50, 34, 32, 20, 24],  # 2017
    [53, 32, 35, 22, 27],  # 2018
    [55, 30, 38, 25, 30],  # 2019
    [58, 28, 40, 28, 34],  # 2020
    [62, 26, 43, 32, 37],  # 2021
    [67, 25, 46, 36, 40],  # 2022
])

# Calculate cumulative enrollment
cumulative_enrollment = np.sum(data, axis=1)

# Create the figure and axis with subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Colors for each faculty
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the stacked bar chart
bottoms = np.zeros(len(years))
for i, (faculty, color) in enumerate(zip(faculties, colors)):
    ax[0].bar(years, data[:, i], bottom=bottoms, label=faculty, color=color, alpha=0.8)
    bottoms += data[:, i]

# Customize the stacked bar chart
ax[0].set_title("University Enrollment Trends (2015-2022)\nDetailed Faculty Contribution Over the Years", fontsize=14, fontweight='bold', pad=20)
ax[0].set_ylabel('Enrollment (Hundreds)', fontsize=12)
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend to the top plot
ax[0].legend(title='Faculties', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Annotate values on each bar segment
for i in range(len(years)):
    y = 0
    for j in range(len(faculties)):
        ax[0].text(i, y + data[i, j] / 2, f"{data[i, j]} ({data[i, j] / cumulative_enrollment[i] * 100:.1f}%)",
                   ha='center', va='center', color='white', fontsize=9)
        y += data[i, j]

# Plot the cumulative enrollment line chart
ax[1].plot(years, cumulative_enrollment, marker='o', color='black', linestyle='-', linewidth=2, label='Total Enrollment')
ax[1].set_title("Cumulative Enrollment Over the Years", fontsize=14, fontweight='bold', pad=10)
ax[1].set_ylabel('Total Enrollment (Hundreds)', fontsize=12)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].grid(axis='both', linestyle='--', alpha=0.7)

# Add a legend to the bottom plot
ax[1].legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()