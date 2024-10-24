import matplotlib.pyplot as plt
import numpy as np

# Define planets and their suitability scores
planets = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Mercury']

# Radar chart data: [Gravity, Atmosphere, Temperature, Radiation, Surface Conditions]
suitability_data = {
    'Mars': [7, 5, 6, 4, 8],
    'Venus': [3, 2, 4, 6, 5],
    'Jupiter': [5, 6, 3, 5, 7],
    'Saturn': [4, 4, 5, 3, 6],
    'Mercury': [6, 3, 4, 7, 4]
}

# Additional line plot data: Historical Space Missions Success Rate (in percentage)
mission_success_data = {
    'Mars': 65,
    'Venus': 55,
    'Jupiter': 45,
    'Saturn': 50,
    'Mercury': 70
}

labels = ['Gravity', 'Atmosphere', 'Temperature', 'Radiation', 'Surface Conditions']
num_vars = len(labels)

def plot_radar_chart(suitability_data, mission_success_data, planets, labels):
    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Close the loop

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Plot radar chart
    for planet in planets:
        values = suitability_data[planet] + suitability_data[planet][:1]
        ax.plot(angles, values, label=planet, linewidth=2)
        ax.fill(angles, values, alpha=0.15)

    # Overlay mission success data directly on the same polar plot
    # Normalize the success data to fit the radar chart scale
    max_suitability_value = max(max(values) for values in suitability_data.values())
    normalized_success_data = [mission_success_data[planet] / 100 * max_suitability_value for planet in planets]
    normalized_success_data += normalized_success_data[:1]

    ax.plot(angles, normalized_success_data, color='red', linewidth=2, marker='o', label='Mission Success Rate')
    ax.fill(angles, normalized_success_data, color='red', alpha=0.1)

    # Configure radar chart
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10, fontweight='bold')
    ax.set_title('Space Exploration Suitability and Mission Success Rates\nfor Various Planets',
                 size=14, color='navy', va='bottom', ha='center')
    
    # Legend and formatting
    ax.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), fontsize=10)
    
    plt.tight_layout()
    plt.show()

# Plot the optimized radar chart
plot_radar_chart(suitability_data, mission_success_data, planets, labels)