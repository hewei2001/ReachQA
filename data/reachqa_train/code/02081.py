import matplotlib.pyplot as plt

# Define the data for conservation actions
projects = [
    'Amazon Rainforest Preservation',
    'Great Barrier Reef Protection',
    'Arctic Wildlife Initiative',
    'African Savannah Safeguard',
    'Himalayan Sanctuaries Project',
    'Borneo Rescue Mission'
]

# Number of successful conservation actions for each project
actions = [230, 180, 120, 300, 150, 210]

# Colors for each project
colors = ['#556B2F', '#FF6347', '#4682B4', '#FFD700', '#8B4513', '#3CB371']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(projects, actions, color=colors, edgecolor='black', height=0.7)

# Title and axis labels
ax.set_title('Wildlife Conservation Efforts:\nSuccessful Actions in Key Regions', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Successful Conservation Actions', fontsize=12)
ax.set_ylabel('Conservation Projects', fontsize=12)

# Annotate bars with the respective values
for bar, action in zip(bars, actions):
    ax.text(action + 5, bar.get_y() + bar.get_height() / 2, f'{action}', va='center', ha='left', fontsize=10, color='black')

# Add vertical grid lines to enhance readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Ensure layout fits all text and visual elements
plt.tight_layout()

# Show the chart
plt.show()