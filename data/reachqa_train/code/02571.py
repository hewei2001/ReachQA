import numpy as np
import matplotlib.pyplot as plt

# Define the cities and sustainability dimensions
cities = ['New York', 'Tokyo', 'Paris', 'Sydney']
sustainability_dimensions = ['Carbon Footprint', 'Renewable Energy', 'Waste Management', 
                             'Public Transport', 'Green Space', 'Water Management']

# Define sustainability scores for each city across the dimensions
sustainability_scores = {
    'New York': [75, 60, 65, 80, 55, 70],
    'Tokyo': [65, 85, 60, 75, 70, 80],
    'Paris': [80, 70, 75, 65, 85, 60],
    'Sydney': [70, 65, 80, 85, 75, 90]
}

# Plotting the radar chart
def plot_radar_chart(data, cities, dimensions):
    num_vars = len(dimensions)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Repeat the first value to close the circle
    angles += angles[:1]

    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Colors for each city
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    # Draw one line per city
    for idx, (city, scores) in enumerate(data.items()):
        scores += scores[:1]
        ax.fill(angles, scores, color=colors[idx], alpha=0.25)
        ax.plot(angles, scores, color=colors[idx], linewidth=2, label=city)

    # Add labels for dimensions
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=11)

    # Add title and legend
    ax.set_title("Sustainability Indices of Global Cities\nin 2030", fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Cities', fontsize=10)

    # Automatically adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function to plot the radar chart
plot_radar_chart(sustainability_scores, cities, sustainability_dimensions)