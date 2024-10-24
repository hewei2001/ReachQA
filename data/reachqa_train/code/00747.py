import matplotlib.pyplot as plt
import numpy as np

# Data: Age groups and their respective average daily internet usage in hours
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
internet_usage_hours = [7.5, 6.5, 5.5, 4.0, 3.0, 2.0]

# Hypothetical data for percentage change from the previous year
percentage_change = [5, -2, -3, 0, 4, -1]

# Colors for the horizontal bars
colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FFBD', '#3385FF', '#8D33FF']

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot horizontal bars
ax1.barh(age_groups, internet_usage_hours, color=colors, edgecolor='black', height=0.5)
ax1.set_xlabel('Average Usage (Hours)', fontsize=12)
ax1.set_ylabel('Age Groups', fontsize=12)

# Add annotations to each bar
for i, (hours, group) in enumerate(zip(internet_usage_hours, age_groups)):
    ax1.text(hours + 0.1, i, f'{hours:.1f} hrs', va='center', ha='left', fontsize=10, color='black', fontweight='bold')

# Create a second y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(age_groups, percentage_change, color='black', marker='o', linestyle='--', linewidth=2, label='Percentage Change')
ax2.set_ylabel('Percentage Change (%)', fontsize=12)

# Adding a legend for the line plot
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2, fontsize=10)

# Add annotations to line plot points
for i, (change, group) in enumerate(zip(percentage_change, age_groups)):
    ax2.text(i, change + 0.5, f'{change:+}%', fontsize=9, ha='center', va='bottom', color='black')

# Grid and formatting
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Title
plt.title('Average Daily Internet Usage (2023)\nAnd Yearly Change by Age Group', fontsize=16, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()