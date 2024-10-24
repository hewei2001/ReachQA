import matplotlib.pyplot as plt
import numpy as np

# Define competencies and their importance across sectors
labels = np.array(['Digital Literacy', 'Emotional Intelligence', 'Creativity', 'Leadership', 'Critical Thinking'])
sectors = ['Technology', 'Healthcare', 'Education']
values = {
    'Technology': [9, 7, 8, 9, 9],
    'Healthcare': [8, 9, 7, 8, 8],
    'Education': [7, 8, 9, 7, 10]
}

# Benchmark data for the overlay plot
benchmark = [8, 8, 8, 8, 8]

# Number of competencies
num_vars = len(labels)

# Function to create a radar chart
def create_radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]  # Close the plot
    angles += angles[:1]

    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.2)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Colors for each sector
colors = ['#ff6f61', '#6b5b95', '#88b04b']

# Create a radar chart for each sector
for i, sector in enumerate(sectors):
    create_radar_chart(ax, values[sector], colors[i], sector)

# Plot benchmark overlay
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
benchmark += benchmark[:1]  # Close the plot
angles += angles[:1]
ax.plot(angles, benchmark, color='black', linewidth=2, linestyle='dashed', label='Benchmark')
ax.fill(angles, benchmark, color='grey', alpha=0.1)

# Add labels and adjust tick positions
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(labels, fontsize=11)
ax.set_yticklabels([])

# Add a chart title
plt.title('Key Competencies in Future Workplaces\nComparative Analysis Across Sectors & Benchmarking', size=16, color='darkblue', pad=30)

# Add legend to differentiate sectors and benchmark
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title="Sectors & Benchmark", title_fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Display the radar chart
plt.show()