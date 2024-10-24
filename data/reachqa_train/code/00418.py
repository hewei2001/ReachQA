import matplotlib.pyplot as plt
import numpy as np

# Define fashion capitals, patterns, and seasons
capitals = ['Paris', 'Milan', 'New York', 'Tokyo']
patterns = ['Roses', 'Lilies', 'Daisies', 'Tulips']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Data representing the percentage of floral patterns for each city and season
data = {
    'Paris': {'Spring': [40, 30, 20, 10], 'Summer': [35, 25, 20, 20], 
              'Autumn': [30, 20, 30, 20], 'Winter': [25, 25, 30, 20]},
    'Milan': {'Spring': [30, 35, 20, 15], 'Summer': [25, 30, 25, 20], 
              'Autumn': [20, 25, 35, 20], 'Winter': [15, 20, 40, 25]},
    'New York': {'Spring': [35, 25, 25, 15], 'Summer': [30, 20, 30, 20], 
                 'Autumn': [25, 15, 40, 20], 'Winter': [20, 10, 50, 20]},
    'Tokyo': {'Spring': [25, 20, 35, 20], 'Summer': [20, 15, 40, 25], 
              'Autumn': [15, 10, 45, 30], 'Winter': [10, 5, 50, 35]}
}

# Define colors for patterns
colors = ['#FF6347', '#FFD700', '#7FFFD4', '#FF69B4']

# Create a rose plot (polar plot) for each fashion capital
fig, axs = plt.subplots(2, 2, figsize=(12, 12), subplot_kw=dict(polar=True))
axs = axs.flatten()

sector_angle = (2 * np.pi) / len(seasons)

for idx, capital in enumerate(capitals):
    ax = axs[idx]
    
    # Accumulate and plot data for each floral pattern
    for pattern_idx, pattern in enumerate(patterns):
        values = [data[capital][season][pattern_idx] for season in seasons]
        values += values[:1]  # Close the circle

        angles = np.linspace(0, 2 * np.pi, len(seasons), endpoint=False).tolist()
        angles += angles[:1]

        ax.fill(angles, values, color=colors[pattern_idx], alpha=0.3, label=pattern)
        ax.plot(angles, values, color=colors[pattern_idx], linewidth=2)

    # Customize the plot
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(seasons, fontsize=10, fontweight='bold')
    ax.set_title(capital, size=14, fontweight='bold', pad=10)
    ax.set_theta_offset(np.pi / 2)  # Start from the top
    ax.set_theta_direction(-1)  # Clockwise

    # Add legend outside the plot
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize='small')

# Main title
fig.suptitle("Floral Trends Over the Seasons\nA Rose Chart Analysis", 
             size=16, fontweight='bold', y=1.02)

# Adjust layout to prevent text cutoff
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Show the plot
plt.show()