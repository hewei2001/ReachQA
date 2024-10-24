import matplotlib.pyplot as plt
import numpy as np

# Define decades and art styles
decades = ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
styles = ['Abstract Expressionism', 'Pop Art', 'Minimalism', 'Conceptual Art', 'Digital Art']

# Representation data (as a percentage of total exhibitions)
style_representation = {
    'Abstract Expressionism': [40, 30, 20, 15, 10, 5],
    'Pop Art': [20, 25, 20, 15, 10, 5],
    'Minimalism': [10, 15, 20, 25, 20, 15],
    'Conceptual Art': [15, 20, 25, 30, 30, 25],
    'Digital Art': [5, 10, 15, 15, 30, 50]
}

# Colors for each style
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create figure and axes
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Evolution of Art Styles\nin Modern Art Exhibitions', fontsize=16, fontweight='bold')

# Calculate total representation percentage for line plot
total_representation = np.sum(list(style_representation.values()), axis=0)

for i, (ax, decade) in enumerate(zip(axes.flatten(), decades)):
    # Gather data for the current decade
    data = [style_representation[style][i] for style in styles]
    
    # Create a donut pie chart
    wedges, texts, autotexts = ax.pie(
        data, colors=colors, labels=None, autopct='%1.1f%%', startangle=140,
        wedgeprops=dict(width=0.3), pctdistance=0.85
    )
    
    # Add a circle in the center to make it a donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Set aspect ratio to be equal and title for each subplot
    ax.set_aspect('equal')
    ax.set_title(decade, fontsize=12, fontweight='bold')

    # Overlay line plot for total representation
    ax2 = ax.twinx()
    ax2.plot(range(len(decades)), total_representation, marker='o', color='black', linewidth=2, markersize=6, label='Total Representation (%)')
    ax2.set_ylim(0, 150)  # Setting y-limits to allow better view of trend

# Create a unified legend for styles and line plot
lines_labels = [ax2.get_legend_handles_labels() for ax2 in axes.flatten()]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]

fig.legend(wedges + lines, styles + ['Total Representation'], loc='center right', fontsize=10, title='Art Styles', title_fontsize='12')

# Adjust layout
plt.subplots_adjust(right=0.85)
plt.tight_layout(rect=[0, 0, 0.85, 0.95])

# Show plot
plt.show()