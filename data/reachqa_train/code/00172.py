import matplotlib.pyplot as plt
import numpy as np

# Function to create a radar chart
def create_radar_chart(categories, data, title, colors):
    num_vars = len(categories)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Close the loop
    angles += angles[:1]
    
    # Setup the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot each city's data
    for city_data, color, city_label in zip(data, colors, ['EcoVille', 'Greenburg', 'SustainCity']):
        # Append first value to close the loop
        values = city_data + city_data[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=city_label, color=color)
        ax.fill(angles, values, color=color, alpha=0.25)

    # Add labels for each category
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, color='gray')

    # Add a title
    plt.title(title, size=15, color='darkblue', y=1.1, weight='bold', multialignment='center')

    # Add a legend with proper formatting
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title='Cities', title_fontsize='13')

    # Set range for radial axis
    ax.set_ylim(0, 10)

    # Remove radial labels for a cleaner look
    ax.set_yticklabels([])

    # Adjust layout for optimal display
    plt.tight_layout()

    # Display the radar chart
    plt.show()

# Define the categories
categories = ['Air Quality', 'Green Space', 'Waste Management', 
              'Water Management', 'Renewable Energy', 'Public Transportation']

# Define data for each city
data = [
    [8, 6, 9, 7, 6, 8],   # EcoVille
    [7, 8, 6, 8, 7, 7],   # Greenburg
    [9, 7, 8, 9, 9, 9]    # SustainCity
]

# Define colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create the radar chart
create_radar_chart(categories, data, 
                   'City Green Index:\nUrban Environmental Performance', 
                   colors)