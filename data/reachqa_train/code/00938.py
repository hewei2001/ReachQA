import numpy as np
import matplotlib.pyplot as plt

# Define the environmental factors
factors = ['Air Quality', 'Noise Levels', 'Biodiversity', 
           'Public Space', 'Green Policy', 'Community Engagement']

# Scores for each city across the factors
cities_scores = {
    'New York': [7, 5, 6, 8, 7, 5],
    'London': [6, 6, 7, 7, 8, 6],
    'Tokyo': [8, 7, 5, 6, 6, 7],
    'Berlin': [7, 6, 8, 9, 7, 8],
    'Sydney': [9, 8, 9, 8, 9, 9]
}

# Calculate the number of variables
num_vars = len(factors)

# Compute angle for each axis, ensuring the plot is circular
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Extend the angles by adding the first angle again to close the circle
angles += angles[:1]

# Function to create radar chart for a city
def create_radar_chart(data, label, color):
    # Append the first data point again to close the circle
    data = np.concatenate((data, [data[0]]))
    
    # Plot the data
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

# Set up the figure
fig, axs = plt.subplots(3, 2, figsize=(10, 10), subplot_kw=dict(polar=True))
axs = axs.flatten()  # Flatten the 2D array of axes for easy iteration

# Define a color palette
colors = plt.cm.viridis(np.linspace(0, 1, len(cities_scores)))

# Plot each city
for idx, (city, scores) in enumerate(cities_scores.items()):
    ax = axs[idx]
    create_radar_chart(scores, city, colors[idx])
    ax.set_yticklabels([])  # Remove y-tick labels for clarity
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(factors, fontsize=10)
    ax.set_title(city, size=12, color=colors[idx], pad=20)

# Set the main title
plt.suptitle("The Future of Urban Green Spaces:\nComparative Analysis of Metropolitan Environmental Factors",
             fontsize=14, fontweight='bold', y=1.02)

# Adjust the layout to ensure all elements are well-spaced
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Hide any unused subplots (there are 6 subplots for 5 cities)
for i in range(len(cities_scores), len(axs)):
    fig.delaxes(axs[i])

# Show the plot
plt.show()