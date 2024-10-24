import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define companies and specializations
companies = ['TechNova', 'CodeCraft', 'AlgoSphere']
specializations = [
    'AI Research', 
    'Cybersecurity', 
    'Cloud Computing', 
    'Quantum Computing', 
    'Blockchain Development'
]

# Number of positions open for each specialization at each company
positions = np.array([
    [120, 80, 200, 50, 70],   # TechNova
    [150, 110, 170, 65, 90],  # CodeCraft
    [130, 95, 180, 75, 85]    # AlgoSphere
])

# Set a Seaborn style
sns.set(style="whitegrid")

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot each company's data with advanced visual elements
colors = sns.color_palette("husl", len(companies))
markers = ['o', 's', '^']

# Plot each company's data
for i, company in enumerate(companies):
    x_positions = np.arange(len(specializations)) + i * 0.2
    y_positions = positions[i]
    ax.scatter(x_positions, y_positions, color=colors[i], marker=markers[i],
               s=200, edgecolor='black', alpha=0.8, label=company)

    # Annotate each point with the number of positions
    for (x, y) in zip(x_positions, y_positions):
        ax.text(x, y + 5, str(y), fontsize=9, ha='center')

# Customize x-ticks
ax.set_xticks(np.arange(len(specializations)))
ax.set_xticklabels(specializations, fontsize=11, rotation=15)

# Add a title and labels with line breaks if necessary
ax.set_title('Tech Giants\' Hiring Focus in 2050\nAcross Various Computer Science Specializations', 
             fontsize=18, fontweight='bold', loc='left', ha='left')
ax.set_xlabel('Specializations', fontsize=13)
ax.set_ylabel('Number of Positions Open', fontsize=13)

# Customize the grid
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(title='Companies', fontsize=11, title_fontsize=12, loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()