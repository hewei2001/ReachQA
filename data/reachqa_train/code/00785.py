import matplotlib.pyplot as plt
import numpy as np

# Define the metrics and the performance scores for two cities
metrics = ['Air Quality', 'Renewable Energy', 'Water Conservation', 
           'Green Spaces', 'Waste Management', 'Public Transport']
green_city_scores = [7, 8, 6, 9, 5, 8]
eco_town_scores = [6, 7, 8, 7, 6, 9]

# Radar chart requires closing the loop
green_city_scores += green_city_scores[:1]
eco_town_scores += eco_town_scores[:1]

# Number of variables
num_vars = len(metrics)

# Compute the angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the plot
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot data for Green City and fill the area
ax.plot(angles, green_city_scores, color='green', linewidth=1.5, linestyle='solid')
ax.fill(angles, green_city_scores, color='green', alpha=0.3)

# Plot data for Eco Town and fill the area
ax.plot(angles, eco_town_scores, color='blue', linewidth=1.5, linestyle='solid')
ax.fill(angles, eco_town_scores, color='blue', alpha=0.3)

# Customize the chart
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])  # Set ticks to match metrics
ax.set_xticklabels(metrics, color='black', fontsize=11)  # Set metric labels

# Add a title
plt.title("2023 City Sustainability Metrics Comparison\nGreen City vs Eco Town",
          size=16, color='darkgreen', y=1.08, fontweight='bold')

# Add a legend
plt.legend(['Green City', 'Eco Town'], loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Ensure the plot layout fits within the figure area
plt.tight_layout(pad=3.0)

# Display the chart
plt.show()