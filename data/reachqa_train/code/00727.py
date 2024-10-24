import matplotlib.pyplot as plt
import numpy as np

# Define the categories and data for each planet
categories = ['Communication', 'Energy', 'Transportation', 'Health', 'Education']
num_vars = len(categories)

# Data for each planet
nova_terra = [8, 9, 7, 8, 7]
zynorra = [6, 7, 6, 8, 9]
kaleron = [9, 6, 8, 7, 8]
pyrros = [7, 8, 9, 6, 6]

# Average data across all planets
average_scores = [
    np.mean([nova_terra[i], zynorra[i], kaleron[i], pyrros[i]]) 
    for i in range(num_vars)
]

# Function to create the radar chart for a given planet
def create_radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, label=label)

# Initialize the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=False))

# Create radar chart on the first subplot
ax1.set_title('Radar Chart: Technological Infrastructure\nAssessment of Planets', fontsize=12, fontweight='bold')
polar_ax = fig.add_subplot(121, polar=True)
create_radar_chart(polar_ax, nova_terra, 'b', 'Nova Terra')
create_radar_chart(polar_ax, zynorra, 'r', 'Zynorra')
create_radar_chart(polar_ax, kaleron, 'g', 'Kaleron')
create_radar_chart(polar_ax, pyrros, 'orange', 'Pyrros')
polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=10)
polar_ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))

# Create bar chart on the second subplot
ax2.bar(categories, average_scores, color=['b', 'r', 'g', 'orange', 'purple'])
ax2.set_ylim(0, 10)
ax2.set_title('Average Scores Across Categories', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Score')
ax2.set_xlabel('Category')
for i, score in enumerate(average_scores):
    ax2.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

# Automatically adjust the layout for optimal spacing
plt.tight_layout()

# Display the charts
plt.show()