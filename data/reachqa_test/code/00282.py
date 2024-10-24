import matplotlib.pyplot as plt
import numpy as np

# Define the mission aspects and their current resource allocations
aspects = [
    'Propulsion Technology',
    'Life Support Systems',
    'Scientific Research Equipment',
    'Communication Systems',
    'Crew Accommodations'
]
current_allocations = [30, 25, 20, 15, 10]

# Historical and projected data
# The bar chart will show historical, current, and projected allocation for each aspect
years = ['2015', '2023', '2030']
historical_allocations = [25, 20, 15, 10, 5]
projected_allocations = [35, 30, 25, 20, 15]

# Define colors consistent with aspects for visual harmony
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFC133']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Plot the donut chart
wedges, texts, autotexts = axs[0].pie(
    current_allocations,
    labels=aspects,
    colors=colors,
    startangle=140,
    autopct='%1.1f%%',
    explode=(0.1, 0, 0, 0, 0),
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color="black", fontsize=10)
)
axs[0].text(0, 0, 'Project StarTrail\nResource Allocation', ha='center', va='center', fontsize=12, fontweight='bold')
axs[0].set_title('Current Allocation\nof Resources', fontsize=14, weight='bold', pad=20)
axs[0].axis('equal')  # Equal aspect ratio for the donut shape

# Plot the bar chart for comparison
bar_width = 0.2
index = np.arange(len(aspects))

# Historical allocations
axs[1].bar(index - bar_width, historical_allocations, bar_width, label='2015', color='#E9967A')

# Current allocations
axs[1].bar(index, current_allocations, bar_width, label='2023', color='#20B2AA')

# Projected allocations
axs[1].bar(index + bar_width, projected_allocations, bar_width, label='2030', color='#4682B4')

# Add labels, title, and legend
axs[1].set_xlabel('Mission Aspects')
axs[1].set_ylabel('Resource Allocation (%)')
axs[1].set_title('Allocation Comparison\n2015, 2023, and 2030', fontsize=14, weight='bold', pad=20)
axs[1].set_xticks(index)
axs[1].set_xticklabels(aspects, rotation=15, ha='right')
axs[1].legend()

# Adjust layout to avoid overlapping elements
plt.tight_layout()

# Display the plots
plt.show()