import matplotlib.pyplot as plt
import squarify
import matplotlib.patches as mpatches

# Domains and their corresponding relative sizes
domains = [
    'Quantum Computing', 'Autonomous Transport', 'Biotechnology', 
    'Cybersecurity', 'Renewable Energy', 'Smart Infrastructure',
    'Artificial Intelligence', 'Space Exploration', 'IoT'
]
sizes = [130, 180, 160, 100, 140, 110, 200, 90, 120]  
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#66FF66', '#FFB366', '#99CCFF', '#CC99FF']

# Additional data for annotations
growth_rates = [8, 10, 9, 5, 7, 6, 11, 4, 7]  # Example projected growth rates in %

# Create the treemap
plt.figure(figsize=(14, 10))
labels = [f'{domain}\n{size} units\nGrowth: {growth}%' for domain, size, growth in zip(domains, sizes, growth_rates)]
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold'})

# Add title
plt.title('Tech Pioneers of 2050:\nNovaTech\'s Innovation Landscape', fontsize=18, pad=20)

# Add a color legend
legend_elements = [mpatches.Patch(color=colors[i], label=f'{domains[i]}') for i in range(len(domains))]
plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), title='Domains')

# Remove axes for clarity
plt.axis('off')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()