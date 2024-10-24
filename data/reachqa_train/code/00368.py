import matplotlib.pyplot as plt
import numpy as np

# Define the browsers and age groups
browsers = ["Chrome", "Firefox", "Edge"]
age_groups = ["Teens (13-19)", "Adults (20-39)", "Seniors (40+)"]

# Fictional data representing browser usage percentage by age group
usage_data = np.array([
    [60, 25, 15],  # Teens
    [50, 30, 20],  # Adults
    [45, 35, 20]   # Seniors
])

# Fictional data representing user satisfaction scores (out of 100)
satisfaction_data = np.array([
    [80, 75, 70],  # Teens
    [85, 70, 65],  # Adults
    [78, 68, 60]   # Seniors
])

# Colors for each browser
browser_colors = ['#FF5733', '#4285F4', '#34A853']
line_colors = ['#C70039', '#900C3F', '#581845']

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the stacked bars
cumulative_usage = np.zeros(len(age_groups))
for idx, browser in enumerate(browsers):
    bars = ax1.bar(age_groups, usage_data[:, idx], bottom=cumulative_usage, 
                   label=f'{browser} Usage', color=browser_colors[idx])
    cumulative_usage += usage_data[:, idx]

# Add the line plot for satisfaction scores
ax2 = ax1.twinx()  # Create a secondary y-axis for the line plot
for idx, browser in enumerate(browsers):
    ax2.plot(age_groups, satisfaction_data[:, idx], marker='o', linestyle='--', 
             label=f'{browser} Satisfaction', color=line_colors[idx])

# Annotate satisfaction scores
for i, age_group in enumerate(age_groups):
    for j, (score, color) in enumerate(zip(satisfaction_data[i], line_colors)):
        ax2.annotate(f'{score}', 
                     xy=(age_group, score), 
                     xytext=(-5, 5), 
                     textcoords='offset points', 
                     ha='center', va='bottom', color=color)

# Configure primary y-axis for usage percentages
ax1.set_ylabel('Usage Percentage (%)', fontsize=12)
ax1.set_ylim(0, 100)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Configure secondary y-axis for satisfaction scores
ax2.set_ylabel('Satisfaction Score (out of 100)', fontsize=12)
ax2.set_ylim(50, 100)

# Add title and legends
ax1.set_title('Web Browsing Habits and Satisfaction in 2023:\nComparison Across Age Groups', fontsize=16, weight='bold', pad=20)
ax1.legend(loc='upper left', fontsize=9)
ax2.legend(loc='upper right', fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()