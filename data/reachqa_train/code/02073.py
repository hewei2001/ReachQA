import matplotlib.pyplot as plt
import numpy as np

# Define the data for conservation actions
projects = [
    'Amazon Rainforest Preservation',
    'Great Barrier Reef Protection',
    'Arctic Wildlife Initiative',
    'African Savannah Safeguard',
    'Himalayan Sanctuaries Project',
    'Borneo Rescue Mission',
    'Galapagos Marine Reserve',
    'Madagascar Biodiversity Conservation',
    'Coral Triangle Protection',
    'Patagonia Eco-safeguard'
]

# Number of successful conservation actions for each category in each project
actions_data = {
    'Legal Protections': [80, 60, 40, 90, 50, 70, 65, 55, 60, 75],
    'Habitat Restoration': [90, 70, 50, 100, 60, 80, 70, 65, 75, 85],
    'Species Reintroduction': [60, 50, 30, 110, 40, 60, 55, 45, 65, 70]
}

categories = list(actions_data.keys())
colors = ['#556B2F', '#FF6347', '#4682B4']
project_indices = np.arange(len(projects))

# Calculate totals for each project to display on the chart
total_actions = np.sum(list(actions_data.values()), axis=0)
average_line = np.mean(total_actions)

# Create the figure and stacked bar chart
fig, ax = plt.subplots(figsize=(16, 10))
bottom = np.zeros(len(projects))

# Plotting stacked bars
for idx, category in enumerate(categories):
    ax.barh(project_indices, actions_data[category], left=bottom, color=colors[idx], edgecolor='black', label=category)
    bottom += actions_data[category]

# Add annotations for totals
for i, total in enumerate(total_actions):
    ax.text(total + 5, i, f'{total}', va='center', ha='left', fontsize=10, color='black', fontweight='bold')

# Adding an average line
ax.axvline(average_line, color='purple', linestyle='--', label='Average Actions')

# Title and axis labels
plt.title('Wildlife Conservation Efforts:\nAnalysis of Actions by Project and Category', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Successful Conservation Actions', fontsize=12)
plt.ylabel('Conservation Projects', fontsize=12)

# Customize y-axis ticks for clarity
ax.set_yticks(project_indices)
ax.set_yticklabels(projects, ha='right', fontsize=11)

# Add grid for x-axis
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(title='Action Categories', fontsize=10, title_fontsize=12, loc='upper right', bbox_to_anchor=(1.15, 1))

# Ensure the layout is properly adjusted
plt.tight_layout()

# Show the chart
plt.show()