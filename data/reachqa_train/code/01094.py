import matplotlib.pyplot as plt
import numpy as np

# Define data for quantum computing projects
complexity_levels = [3, 5, 7, 9, 4, 6, 8, 2, 10, 5, 7]
investment_millions = [5, 10, 20, 30, 8, 15, 25, 3, 35, 12, 22]
research_focus = [
    'Quantum Cryptography', 'Quantum Cryptography', 'Quantum Machine Learning',
    'Quantum Networking', 'Quantum Machine Learning', 'Quantum Cryptography',
    'Quantum Networking', 'Quantum Simulations', 'Quantum Simulations',
    'Quantum Machine Learning', 'Quantum Networking'
]

# Unique focus areas for color mapping
unique_focus_areas = list(set(research_focus))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Map each research focus to a color
color_mapping = {focus: colors[i] for i, focus in enumerate(unique_focus_areas)}
project_colors = [color_mapping[focus] for focus in research_focus]

# Create scatter plot
plt.figure(figsize=(10, 8))
scatter = plt.scatter(complexity_levels, investment_millions, 
                      c=project_colors, s=100, edgecolor='k', alpha=0.7)

# Add title and labels
plt.title('Quantum Computing R&D Landscape\n(Complexity vs. Investment in 2025)', fontsize=14, fontweight='bold')
plt.xlabel('Complexity Level', fontsize=12)
plt.ylabel('Investment (Millions USD)', fontsize=12)

# Create a legend
legend_labels = {focus: plt.Line2D([0], [0], marker='o', color='w', 
                                   markerfacecolor=color_mapping[focus], markersize=10) 
                 for focus in unique_focus_areas}
plt.legend(legend_labels.values(), legend_labels.keys(), title="Research Focus Area", loc='upper left', fontsize=10)

# Customize gridlines for better readability
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()