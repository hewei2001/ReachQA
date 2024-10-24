import matplotlib.pyplot as plt
import numpy as np

# Define months and expanded to include 2 years
months_extended = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
] * 2)

# Simulate average writing hours for two years (2023 and 2024)
average_hours_2023 = np.array([20, 22, 25, 24, 27, 26, 28, 30, 29, 26, 25, 24])
average_hours_2024 = np.array([21, 23, 26, 25, 28, 27, 29, 31, 30, 27, 26, 25])
average_hours = np.concatenate([average_hours_2023, average_hours_2024])

# Standard deviations for error bars
std_devs_2023 = np.array([3, 4, 3.5, 4.5, 4, 3.2, 3.8, 4.1, 3.9, 4.2, 4, 3.5])
std_devs_2024 = np.array([3.5, 4.2, 3.8, 4.4, 4.1, 3.5, 3.9, 4.3, 4, 4.5, 4.1, 3.6])
std_devs = np.concatenate([std_devs_2023, std_devs_2024])

# A secondary dataset for comparison (e.g., number of projects completed)
projects_completed = np.array([2, 3, 5, 4, 6, 5, 7, 8, 7, 5, 6, 5, 3, 4, 6, 5, 7, 6, 8, 9, 8, 6, 7, 6])

x_values = np.arange(len(months_extended))

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot average hours with error bars
color = '#1f77b4'
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Avg Writing Hours Per Week', fontsize=14, color=color)
ax1.errorbar(
    x_values, average_hours, yerr=std_devs, fmt='-o', color=color,
    ecolor='lightcoral', elinewidth=2, capsize=4, alpha=0.8,
    label='Average Weekly Hours'
)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(x_values)
ax1.set_xticklabels(months_extended, rotation=45, ha="right", fontsize=10)
ax1.set_ylim(15, 35)

# Add second y-axis for projects completed
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Projects Completed', fontsize=14, color=color)
ax2.bar(x_values, projects_completed, width=0.4, color=color, alpha=0.5, label='Projects Completed')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 10)

# Add title and grid
plt.title('Writing Habits of Authors (2023 & 2024)\nAvg Weekly Hours & Projects Completed', 
          fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Adjust layout for clear visualization
fig.tight_layout()

# Show plot
plt.show()