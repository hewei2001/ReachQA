import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and data for each city
categories = ['Renewable Energy Use', 'Waste Management', 
              'Public Transport', 'Green Spaces', 'Water Conservation']
data = {
    'GreenVille': [8, 7, 6, 9, 8],
    'EcoTown': [7, 8, 7, 7, 6],
    'CleanCity': [6, 6, 8, 5, 7],
    'RenewVille': [9, 6, 7, 8, 9],
    'Sustainopolis': [8, 9, 9, 8, 9]
}

# Number of categories
N = len(categories)

# Function to plot radar chart
def plot_radar(data, categories):
    # Color palette and line styles
    colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
    line_styles = ['-', '--', '-.', ':', '-']

    # Create the figure
    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#f7f7f7')
    
    # Generate angles for each category
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle
    
    # Draw each city's data
    for idx, (city, values) in enumerate(data.items()):
        values += values[:1]  # Complete the loop
        ax.plot(angles, values, linewidth=2, linestyle=line_styles[idx], label=city, color=colors[idx])
        ax.fill(angles, values, alpha=0.25, color=colors[idx])

    # Add category labels with slight rotation for better readability
    plt.xticks(angles[:-1], categories, color='black', size=10, rotation=45)

    # Add y-ticks and labels
    ax.yaxis.set_ticks([2, 4, 6, 8, 10])
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
    plt.ylim(0, 10)

    # Add data point markers
    for values in data.values():
        for angle, value in zip(angles, values):
            ax.plot(angle, value, 'o', color='black')

    # Title and legend
    plt.title("Sustainability Adoption Index:\nEvaluating Urban Environmental Initiatives", 
              size=15, color='darkgreen', weight='bold', pad=30)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), frameon=False)

    # Add gridlines
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Adjust layout
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Call the plotting function
plot_radar(data, categories)