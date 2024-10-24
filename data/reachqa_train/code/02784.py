import matplotlib.pyplot as plt
import numpy as np

# Define the futuristic elements and number of variables
elements = ['Tech Integration', 'Eco Materials', 'Abstract Concepts', 'Interactive Art', 'Global Narratives']
num_vars = len(elements)

# Data for each artist (explicitly constructed)
data = {
    'Innovator Iris': [8, 6, 9, 7, 5],
    'Visionary Victor': [7, 8, 6, 9, 7],
    'Futurist Fiona': [9, 7, 8, 6, 8],
    'Avant-garde Alex': [6, 9, 5, 8, 9],
    'Creative Chris': [5, 7, 9, 6, 8]
}

# Helper function to calculate the angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

def plot_radar(data, title):
    # Create a polar subplot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Set up the grid and angles
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], elements, fontsize=9)

    # Set y-ticks and limits
    ax.set_rscale('linear')
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
    plt.ylim(0, 10)

    # Define color palette
    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD']
    
    # Plot each artist's data
    for color, (artist, values) in zip(colors, data.items()):
        values += values[:1]  # Complete the loop
        ax.fill(angles, values, color=color, alpha=0.25, label=artist)
        ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')

    # Add a legend and title
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
    plt.title(title, size=14, color='black', y=1.1, weight='bold', ha='center')

    # Adjust layout and display plot
    plt.tight_layout()
    plt.show()

# Plot the radar chart
plot_radar(data, "Exploration of Futuristic Elements\nin Contemporary Art")