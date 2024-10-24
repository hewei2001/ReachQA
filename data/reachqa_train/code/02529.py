import matplotlib.pyplot as plt
import numpy as np

# Weekly working hours for different departments (sample data)
development_hours = [38, 40, 42, 45, 50, 48, 60, 55, 58, 40, 43, 47, 49, 45, 44, 46]
marketing_hours = [35, 36, 40, 38, 42, 39, 34, 37, 33, 31, 40, 38, 36, 35, 37, 39]
sales_hours = [30, 32, 35, 40, 38, 45, 50, 60, 55, 41, 42, 44, 46, 35, 37, 31]
support_hours = [25, 30, 35, 40, 45, 50, 55, 60, 32, 34, 36, 38, 33, 31, 29, 28]

# Consolidate the data
data = [development_hours, marketing_hours, sales_hours, support_hours]
departments = ['Development', 'Marketing', 'Sales', 'Customer Support']

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the horizontal box plot
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, 
                boxprops=dict(facecolor='lightblue', color='darkblue'),
                whiskerprops=dict(color='darkblue'),
                capprops=dict(color='darkblue'),
                flierprops=dict(marker='o', color='red', markersize=8, linestyle='none'),
                medianprops=dict(color='orange', linewidth=2))

# Customizing the plot
ax.set_title('Distribution of Weekly Working Hours\nAcross Departments in a Tech Company', fontsize=16, fontweight='bold')
ax.set_xlabel('Hours Worked per Week', fontsize=12)
ax.set_yticklabels(departments)
ax.set_yticks([1, 2, 3, 4])

# Adding grid for improved readability
ax.grid(True, linestyle='--', alpha=0.6, axis='x')

# Adjusting the box colors and setting different colors for each department
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding annotations for median hours
for i, hours in enumerate(data, start=1):
    median = np.median(hours)
    ax.annotate(f'{median} hrs', xy=(median, i), xytext=(median + 2, i + 0.1),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()