import matplotlib.pyplot as plt
import numpy as np

# Screen time data in hours for different age groups
screen_time_data = {
    'Children (6-12)': [2, 3, 1.5, 4, 2.5, 3.5, 2.5, 4.5, 3],
    'Teenagers (13-19)': [5, 6.5, 7, 5.5, 6, 5.5, 6.5, 7.5, 6.5],
    'Young Adults (20-35)': [4, 5, 6, 4.5, 5, 4.5, 5.5, 6, 5],
    'Adults (36-60)': [3, 2.5, 2, 3.5, 4, 3, 2.5, 2, 3],
    'Seniors (60+)': [1.5, 2, 1, 2.5, 1.5, 2, 1.5, 1, 1.8]
}

# List of age groups and corresponding screen time data
age_groups = list(screen_time_data.keys())
data_values = list(screen_time_data.values())

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal box chart
boxprops = dict(facecolor='skyblue', color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='--')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='black', linewidth=2)

ax.boxplot(data_values, vert=False, patch_artist=True, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops,
           capprops=capprops, flierprops=flierprops,
           medianprops=medianprops)

# Set labels and title
ax.set_yticklabels(age_groups)
ax.set_xlabel('Daily Screen Time (hours)', fontsize=12)
ax.set_title('Annual Screen Time Usage Across Different Age Groups\nin 2030', fontsize=16, fontweight='bold', pad=20)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend explaining outliers
plt.scatter([], [], color='red', label='Outlier', marker='o', s=50)
ax.legend(loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()