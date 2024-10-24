import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Define vehicle types and their performance metrics
vehicles = ['Electric Glider', 'Solar Rover', 'Hydrogen Cruiser', 'Biofuel Flyer']

# Radar chart data
efficiency_data = {
    'Electric Glider': [8, 5, 9, 6, 10],
    'Solar Rover': [7, 7, 8, 5, 9],
    'Hydrogen Cruiser': [6, 9, 7, 8, 6],
    'Biofuel Flyer': [5, 8, 6, 9, 7]
}

# Labels for the performance metrics
labels = ['Fuel Efficiency', 'Speed', 'Safety', 'Cargo Capacity', 'Environmental Impact']
num_vars = len(labels)

def plot_radar_chart(efficiency_data, vehicles, labels):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the loop

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

    # Define a color palette with distinct, contrasting colors
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

    # Plot data for each vehicle
    for idx, vehicle in enumerate(vehicles):
        values = efficiency_data[vehicle] + efficiency_data[vehicle][:1]
        ax.plot(angles, values, linewidth=2, linestyle='-', marker='o', label=vehicle, color=colors[idx])
        ax.fill(angles, values, color=colors[idx], alpha=0.2)

    # Customize ticks and labels
    ax.set_yticks(range(1, 11))
    ax.set_yticklabels([str(i) for i in range(1, 11)], color='grey', size=8)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9, color='navy', fontweight='bold')
    
    # Improved title with subtitle
    ax.set_title('Futuristic Vehicle Efficiency Analysis (2050)\nComparative Performance Across Key Metrics', 
                 size=14, color='darkgreen', ha='center', va='top', pad=20)

    ax.grid(color='grey', linestyle='--', linewidth=0.5)

    # Improved legend, moved outside plot area
    legend_elements = [Line2D([0], [0], color=colors[i], lw=2, marker='o', label=vehicles[i]) for i in range(len(vehicles))]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, title="Vehicles")

    # Enhance layout
    plt.tight_layout()
    
    plt.show()

# Plot the radar chart
plot_radar_chart(efficiency_data, vehicles, labels)