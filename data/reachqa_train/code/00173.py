import matplotlib.pyplot as plt
import numpy as np

# Function to create a radar chart
def create_radar_chart(categories, data, title, colors):
    num_vars = len(categories)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the loop
    
    # Setup the radar chart
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Plot each city's data
    city_labels = ['EcoVille', 'Greenburg', 'SustainCity', 'RenewTown']
    for city_data, color, city_label in zip(data, colors, city_labels):
        values = city_data + city_data[:1]
        ax.plot(angles, values, linewidth=1.5, linestyle='solid', label=city_label, color=color)
        ax.fill(angles, values, color=color, alpha=0.1)

    # Add labels for each category
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9, color='gray', wrap=True)
    
    # Allow for variable radial limits
    ax.set_ylim(0, 12)

    # Title, legend, and layout adjustments
    plt.title(title, size=13, color='darkblue', weight='bold', y=1.1, multialignment='center')
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Cities', title_fontsize='12')
    plt.tight_layout()

    # Display the radar chart
    plt.show()

# Define the categories
categories = [
    'Air Quality', 'Green Space', 'Waste Management', 
    'Water Management', 'Renewable Energy', 'Public Transportation', 
    'Carbon Emission Reduction', 'Water Quality'
]

# Define data for each city
data = [
    [8.1, 6.5, 9.2, 7.8, 6.7, 8.3, 5.5, 8.1],  # EcoVille
    [7.0, 8.3, 6.6, 8.1, 7.4, 7.9, 6.2, 7.5],  # Greenburg
    [9.3, 7.2, 8.1, 9.0, 9.1, 9.5, 7.0, 9.2],  # SustainCity
    [6.8, 7.5, 7.0, 7.2, 6.9, 8.0, 6.8, 7.3]   # RenewTown
]

# Define colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the radar chart
create_radar_chart(categories, data, 
                   'City Green Index:\nUrban Environmental Performance', 
                   colors)