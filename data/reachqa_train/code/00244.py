import matplotlib.pyplot as plt
import numpy as np

# Define categories of renewable energy evaluation
categories = ['Availability', 'Efficiency', 'Cost-effectiveness', 'Public Adoption', 'Environmental Impact']

# Data for each continent
data_Africa = [8, 6, 5, 7, 6]
data_Asia = [7, 8, 6, 6, 7]
data_Europe = [6, 7, 7, 8, 8]
data_North_America = [8, 7, 8, 7, 7]
data_South_America = [7, 6, 8, 6, 6]

# Append the first element to the end for a closed radar chart
data_Africa += data_Africa[:1]
data_Asia += data_Asia[:1]
data_Europe += data_Europe[:1]
data_North_America += data_North_America[:1]
data_South_America += data_South_America[:1]

# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the plot

# Initialize radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one spoke per category and add labels with rotation for better readability
plt.xticks(angles[:-1], categories, color='grey', size=10, rotation=45, ha='right')

# Draw y-labels
plt.yticks([5, 6, 7, 8], ['5', '6', '7', '8'], color='grey', size=8)
plt.ylim(4, 9)  # Adjust ylim for clarity

# Background grid customization
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)

# Plot and fill for each continent with distinctive styles
styles = {
    'Africa': ('skyblue', '-', 'o'),
    'Asia': ('lightgreen', '--', '^'),
    'Europe': ('coral', '-.', 's'),
    'North America': ('orchid', ':', 'd'),
    'South America': ('gold', (0, (3, 1, 1, 1)), 'p')
}

datasets = [data_Africa, data_Asia, data_Europe, data_North_America, data_South_America]
labels = styles.keys()

for data, (label, style) in zip(datasets, styles.items()):
    color, linestyle, marker = style
    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, marker=marker, markersize=5, label=label)
    ax.fill(angles, data, color=color, alpha=0.15)

# Add a multi-line title for better emphasis
plt.title('Renewable Energy Evaluation Across Continents\nEmphasizing Availability, Efficiency, Cost-effectiveness, Public Adoption, and Environmental Impact', 
          size=13, color='darkblue', weight='bold', loc='center', pad=30)

# Add legend outside of the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10, title="Continents")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()