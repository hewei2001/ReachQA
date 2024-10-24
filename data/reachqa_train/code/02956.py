import matplotlib.pyplot as plt

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

# Create donut pie charts for each decade
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle('Evolution of Art Styles\nin Modern Art Exhibitions', fontsize=18, fontweight='bold')

for i, (ax, decade) in enumerate(zip(axes.flatten(), decades)):
    # Gather data for the current decade
    data = [style_representation[style][i] for style in styles]
    
    # Create a donut pie chart
    wedges, texts, autotexts = ax.pie(
        data, colors=colors, labels=styles, autopct='%1.1f%%',
        startangle=140, wedgeprops=dict(width=0.3), pctdistance=0.85
    )
    
    # Add a circle in the center to make it a donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Set aspect ratio to be equal for a perfect circle and title for each subplot
    ax.set_aspect('equal')
    ax.set_title(decade, fontsize=14, fontweight='bold')

    # Adjust label positions
    for text in texts + autotexts:
        text.set_fontsize(8)

# Create a legend outside the plot
fig.legend(wedges, styles, loc='center right', fontsize=10, title='Art Styles', title_fontsize='12')

# Adjust layout to make space for the legend
plt.subplots_adjust(right=0.85)
plt.tight_layout(rect=[0, 0, 0.85, 0.95])

# Show the plot
plt.show()