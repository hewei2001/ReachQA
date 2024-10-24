import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define departments and the number of professional development programs
departments = ['Engineering', 'Marketing', 'Sales', 'Human Resources', 'Customer Support']
num_programs = [15, 8, 12, 10, 6]
total_programs = sum(num_programs)

# Define colors for each department
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure and axis for the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bar chart
bars = ax.bar(departments, num_programs, color=colors, width=0.6, edgecolor='black', linewidth=1.2, hatch='/')

# Annotate each bar with the number and percentage of programs
for bar, color in zip(bars, colors):
    yval = bar.get_height()
    percentage = (yval / total_programs) * 100
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval} ({percentage:.1f}%)', ha='center', va='bottom', 
            fontsize=10, fontweight='bold', color=color)

# Set title and labels
ax.set_title('Professional Development Programs\nin InnovateTech Departments (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Number of Programs', fontsize=12)

# Customize the grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

# Adjust the x-tick labels for clarity
plt.xticks(rotation=15, fontsize=11)

# Set the y-limit slightly higher for better annotation spacing
ax.set_ylim(0, max(num_programs) + 6)

# Add a legend
legend_elements = [Patch(facecolor=color, edgecolor='black', label=f'{dept} ({n} Programs)') 
                   for dept, n, color in zip(departments, num_programs, colors)]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10, title='Departments')

# Add an overall trend line (average)
average_programs = np.mean(num_programs)
ax.axhline(average_programs, color='gray', linestyle='--', linewidth=1.5, label=f'Average: {average_programs:.2f}')
ax.text(len(departments) - 0.5, average_programs + 0.5, f'Avg: {average_programs:.1f}', 
        color='gray', fontsize=10, ha='right', va='bottom')

# Automatically adjust layout to prevent overlapping of elements
plt.tight_layout()

# Display the plot
plt.show()