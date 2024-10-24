import matplotlib.pyplot as plt
import numpy as np

# Data: Age groups and their respective average daily internet usage in hours
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
internet_usage_hours = [7.5, 6.5, 5.5, 4.0, 3.0, 2.0]

# Define distinct colors for each bar
colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FFBD', '#3385FF', '#8D33FF']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot horizontal bars with edges
ax.barh(age_groups, internet_usage_hours, color=colors, edgecolor='black', height=0.5)

# Title and labels
ax.set_title('Average Daily Internet Usage\nAcross Different Age Groups (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Average Usage (Hours)', fontsize=12)
ax.set_ylabel('Age Groups', fontsize=12)

# Add value annotations to each bar
for i, (hours, group) in enumerate(zip(internet_usage_hours, age_groups)):
    ax.text(hours + 0.1, i, f'{hours:.1f} hours', va='center', ha='left', fontsize=10, color='black', fontweight='bold')

# Grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure labels and title do not overlap
plt.tight_layout()

# Display the plot
plt.show()