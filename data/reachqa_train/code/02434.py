import matplotlib.pyplot as plt
import numpy as np

# Define the age groups and their corresponding internet usage percentage
age_groups = ['0-17 years', '18-24 years', '25-34 years', '35-54 years', '55+ years']
usage_percentage = np.array([20, 30, 25, 15, 10])

# Define colors for the bars
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Create a horizontal bar chart
bars = plt.barh(age_groups, usage_percentage, color=colors, alpha=0.85)

# Title and axis labels
plt.title('Internet Usage Distribution by Age Group\nin Techville, 2023', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Percentage of Total Internet Usage', fontsize=14)
plt.xlim(0, 100)

# Annotate each bar with percentage values
for bar, percentage in zip(bars, usage_percentage):
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
             f'{percentage}%', va='center', fontsize=12)

# Remove the frame to enhance focus on data
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Add a grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()