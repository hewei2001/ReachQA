import matplotlib.pyplot as plt
import numpy as np

# Define the categories and the number of variables (indices)
categories = ['Renewable Energy\nUsage', 'Carbon Emission\nReduction', 
              'Water Conservation', 'Waste Management', 'Biodiversity\nPreservation']
num_vars = len(categories)

# Function to create a radar chart
def create_radar_chart(ax, data, color, label):
    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]  # Repeat the first value to close the circle
    angles += angles[:1]
    
    # Plot data and fill area
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, label=label)

    # Set the labels for each axis
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, color='navy')

# Data for each country
data_Germany = [80, 75, 70, 85, 65]
data_Japan = [70, 60, 80, 75, 55]
data_Brazil = [60, 50, 65, 55, 90]
data_SouthAfrica = [50, 55, 60, 70, 80]

# Plot setup
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create radar charts for each country
create_radar_chart(ax, data_Germany, colors[0], 'Germany')
create_radar_chart(ax, data_Japan, colors[1], 'Japan')
create_radar_chart(ax, data_Brazil, colors[2], 'Brazil')
create_radar_chart(ax, data_SouthAfrica, colors[3], 'South Africa')

# Add a legend and set the title
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)
plt.title('Global Sustainability Indices\nComparison Among Countries', size=15, color='darkslategray', y=1.15)

# Adjust layout to prevent overlap and improve appearance
plt.tight_layout()
plt.show()