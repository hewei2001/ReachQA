import matplotlib.pyplot as plt
import numpy as np

# Define the categories and writers
categories = ['Creativity', 'Emotional Depth', 'Social Commentary', 'Humor', 'Style']
writers = ['Shakespeare', 'Austen', 'Hemingway', 'Poe', 'Orwell']

# Define scores for each writer
data = {
    'Shakespeare': [9, 8, 7, 7, 10],
    'Austen': [7, 9, 8, 6, 9],
    'Hemingway': [8, 8, 6, 4, 9],
    'Poe': [9, 7, 5, 5, 8],
    'Orwell': [7, 6, 9, 3, 7]
}

# Extended data for a heatmap subplot (using different aspects or metrics for demonstration)
modern_writers = ['Morrison', 'Atwood', 'Toni', 'Murakami', 'Rushdie']
modern_data = {
    'Morrison': [8, 9, 8, 5, 7],
    'Atwood': [7, 8, 7, 6, 8],
    'Toni': [6, 7, 9, 6, 7],
    'Murakami': [7, 7, 6, 8, 8],
    'Rushdie': [8, 8, 9, 4, 6]
}

# Number of variables/categories
num_vars = len(categories)

# Function to create a radar chart
def create_radar_chart(ax, data, label, color='blue'):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)

# Initialize subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=True))
ax_radar, ax_heatmap = axs

# Assign colors to each writer
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each writer's data on the radar chart
for writer, color in zip(writers, colors):
    create_radar_chart(ax_radar, data[writer], writer, color)

ax_radar.set_title('The Literary Prowess\nof Historical Writers', size=16, weight='bold', position=(0.5, 1.1))
ax_radar.legend(writers, loc='upper right', bbox_to_anchor=(1.2, 1.15), fontsize=10)

# Data matrix for heatmap (the rows are writers, the columns are categories)
heatmap_data = np.array([modern_data[writer] for writer in modern_writers])

# Add heatmap
ax_heatmap.remove()  # Change from polar to rectangular plot for heatmap
ax_heatmap = fig.add_subplot(122)
cax = ax_heatmap.matshow(heatmap_data, cmap='Blues', aspect='auto')

# Set the heatmap's ticks and labels
ax_heatmap.set_xticks(np.arange(len(categories)))
ax_heatmap.set_yticks(np.arange(len(modern_writers)))
ax_heatmap.set_xticklabels(categories, rotation=45, ha='left')
ax_heatmap.set_yticklabels(modern_writers)

# Annotate each cell with the numeric value
for i in range(heatmap_data.shape[0]):
    for j in range(heatmap_data.shape[1]):
        ax_heatmap.text(j, i, f"{heatmap_data[i, j]:.1f}", ha='center', va='center', color='black')

ax_heatmap.set_title('Literary Scores of Modern Writers', size=16, weight='bold', pad=20)

# Add colorbar for the heatmap
fig.colorbar(cax, ax=ax_heatmap, orientation='vertical', fraction=0.046, pad=0.04)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()