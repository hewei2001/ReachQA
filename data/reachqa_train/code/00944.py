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

# Historical trend data for each city (e.g., year-on-year improvement)
historical_trends = {
    'New York': [0.2, 0.1, -0.1, 0.3, 0.2, -0.2],
    'London': [0.1, 0.1, 0.2, 0.0, -0.1, 0.1],
    'Tokyo': [-0.1, 0.0, 0.1, 0.1, 0.0, 0.2],
    'Berlin': [0.3, 0.2, 0.1, 0.0, 0.1, 0.2],
    'Sydney': [0.0, 0.1, 0.0, 0.0, 0.1, 0.0]
}

# Number of variables and angles for radar chart
num_vars = len(factors)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]

def create_radar_chart(ax, scores, trends, color):
    # Complete the loop for both scores and trends
    scores = np.concatenate((scores, [scores[0]]))
    trends = np.concatenate((trends, [trends[0]]))
    
    # Plot scores
    ax.plot(angles, scores, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, scores, color=color, alpha=0.25)
    
    # Plot trend data as another series within the same axis
    ax.plot(angles, trends, color='black', linestyle='dashed', linewidth=1.5, label='Trend')
    
    # Set labels
    ax.set_yticklabels([])  # Remove y-tick labels for clarity
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(factors, fontsize=9)
    
# Figure setup
fig, axs = plt.subplots(3, 2, figsize=(12, 12), subplot_kw=dict(polar=True))
axs = axs.flatten()

# Define a color palette
colors = plt.cm.viridis(np.linspace(0, 1, len(cities_scores)))

# Plot radar charts and overlay line plots
for idx, (city, scores) in enumerate(cities_scores.items()):
    ax = axs[idx]
    trend_data = historical_trends[city]
    create_radar_chart(ax, scores, trend_data, colors[idx])
    ax.set_title(city, size=12, color=colors[idx], pad=10)

# Add overall title
plt.suptitle("Comparative Analysis of Metropolitan Environmental Factors and Historical Trends",
             fontsize=16, fontweight='bold', y=1.03)

# Adjust layout to ensure visibility of all elements
plt.tight_layout(rect=[0, 0, 1, 0.98])

# Hide unused subplot
if len(cities_scores) < len(axs):
    for i in range(len(cities_scores), len(axs)):
        fig.delaxes(axs[i])

plt.show()