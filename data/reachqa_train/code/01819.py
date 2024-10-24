import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Connectivity', 'Sustainability', 'Security', 'Mobility', 'Energy Efficiency']

# Create data for five fictional smart cities
city1 = np.array([8, 7, 9, 6, 8])  # City A: Technopolis
city2 = np.array([7, 8, 8, 5, 7])  # City B: Futurama
city3 = np.array([6, 6, 7, 7, 9])  # City C: Innovatown
city4 = np.array([9, 5, 6, 8, 6])  # City D: Cyber City
city5 = np.array([5, 9, 8, 7, 8])  # City E: Sustainaville

# Combine all city data
city_data = np.vstack([city1, city2, city3, city4, city5])

# City names for the legend
city_names = ['Technopolis', 'Futurama', 'Innovatown', 'Cyber City', 'Sustainaville']

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Function to create radar chart
def create_radar_chart(data, categories, city_names):
    angles_with_closure = angles + angles[:1]
    
    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

    # Draw one line per city
    for i, city in enumerate(data):
        values = np.append(city, city[0])  # Closing the loop
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='solid', label=city_names[i])
        ax.fill(angles_with_closure, values, alpha=0.1)

    # Add labels for each category
    plt.xticks(angles, categories, color='black', size=12)

    # Add labels for the axes
    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    # Title and legend
    plt.title("Cities of Tomorrow:\nComparative Analysis of Smart City Features", size=15, color='navy', y=1.1, fontweight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Automatically adjust layout
    plt.tight_layout()
    
    # Show the radar chart
    plt.show()

# Call the function with our data
create_radar_chart(city_data, categories, city_names)