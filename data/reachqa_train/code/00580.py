import matplotlib.pyplot as plt
import numpy as np

# Define disciplines and expanded skill sets with weights for complexity
disciplines = ['Humanities', 'Engineering', 'Business', 'Sciences', 'Arts', 'Medicine']
skills = ['Critical Thinking', 'Communication', 'Technical Skills', 'Teamwork', 
          'Problem Solving', 'Analytical Skills', 'Creativity', 'Leadership']
weights = [1.2, 1.0, 1.5, 1.1, 1.3, 1.4, 1.2, 1.0]

# Expanded skill scores for each discipline
scores = {
    'Humanities': [9, 8, 4, 7, 7, 9, 10, 8],
    'Engineering': [7, 6, 10, 5, 9, 8, 6, 7],
    'Business': [6, 9, 7, 8, 8, 7, 7, 9],
    'Sciences': [8, 7, 9, 6, 9, 8, 5, 7],
    'Arts': [9, 9, 5, 8, 8, 6, 9, 7],
    'Medicine': [8, 7, 9, 8, 7, 8, 7, 6]
}

# Function to create radar charts with weighted scores
def create_radar_chart(labels, values, title, color, weights):
    num_vars = len(labels)
    
    # Compute weighted scores
    weighted_values = [v * w for v, w in zip(values, weights)]
    
    # Compute angles for plotting
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop by repeating the first value and angle
    values += values[:1]
    weighted_values += weighted_values[:1]
    angles += angles[:1]
    
    # Create radar plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Plot data
    ax.fill(angles, weighted_values, color=color, alpha=0.25)
    ax.plot(angles, weighted_values, color=color, linewidth=2)
    
    # Hide y-axis labels, but show grid
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', fontsize=9, weight='bold')
    
    # Annotate with the values
    for angle, value in zip(angles, weighted_values):
        ax.text(angle, value + 0.2, f'{value:.1f}', size=9, color=color, ha='center', va='center')
    
    # Customize the title
    ax.set_title(title, size=12, color=color, y=1.1, weight='bold')
    ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.7)

    return fig, ax

# Create a single figure with subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 12), subplot_kw=dict(polar=True))
colors = plt.cm.viridis(np.linspace(0, 1, len(disciplines)))

# Generate radar charts for each discipline
for i, (discipline, ax) in enumerate(zip(disciplines, axs.flatten())):
    create_radar_chart(skills, scores[discipline], discipline, colors[i], weights)

# Super title for the entire figure
plt.suptitle("Comprehensive Academic Skills Assessment:\nWeighted Core Competencies Across Disciplines",
             fontsize=20, fontweight='bold', y=1.02)

# Adjust the layout for better readability
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()