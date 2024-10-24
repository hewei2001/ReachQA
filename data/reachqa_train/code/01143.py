import matplotlib.pyplot as plt
import numpy as np

# Categories and number of variables
categories = ['Energy Efficiency', 'Green Spaces', 'Transportation', 'Waste Management', 'Water Usage', 'Air Quality']
num_vars = len(categories)

# Data for EcoVille and SustainCity
ecoville_scores = [8, 9, 7, 6, 8, 9]
sustaincity_scores = [7, 8, 8, 7, 9, 6]

# Function to create a radar chart
def create_radar_chart(ax, data, color, label):
    # Compute angle for each category
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop and append the start to the end
    data += data[:1]
    angles += angles[:1]

    # Plot data
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)

    # Fill area
    ax.fill(angles, data, color=color, alpha=0.25)

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Adjust the chart layout
fig.subplots_adjust(top=0.85, bottom=0.05)

# Create the plots for both cities
create_radar_chart(ax, ecoville_scores[:], 'green', 'EcoVille')
create_radar_chart(ax, sustaincity_scores[:], 'blue', 'SustainCity')

# Labels for each angle
ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
ax.set_xticklabels(categories, fontsize=11)

# Set the range for the radial axis
ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Add title and legend
plt.title("Comparative Analysis of Urban Sustainability Metrics:\nEcoVille vs. SustainCity", size=16, color='darkblue', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()