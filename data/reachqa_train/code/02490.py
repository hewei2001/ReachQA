import matplotlib.pyplot as plt
import numpy as np

# Define flower types
flower_types = ['Roses', 'Tulips', 'Lilies', 'Sunflowers', 'Orchids']

# Define popularity score for each flower type across the four seasons
# Each score represents an arbitrary measure of popularity
popularity_scores = np.array([
    [80, 30, 20, 50],  # Roses: highly popular in Spring and Summer
    [60, 80, 30, 10],  # Tulips: peak in Spring, drop in Winter
    [40, 50, 80, 30],  # Lilies: peak in Autumn
    [30, 60, 40, 70],  # Sunflowers: highly popular in Summer and Winter
    [50, 40, 30, 80]   # Orchids: peak in Winter
])

# Number of flower types
N = len(flower_types)

# Number of seasons (4 in this example)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
angles = np.linspace(0, 2 * np.pi, len(seasons), endpoint=False).tolist()

# Complete the circle by appending the start to the end
popularity_scores = np.concatenate((popularity_scores, popularity_scores[:,[0]]), axis=1)
angles += angles[:1]

# Create polar plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each flower type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for i in range(N):
    ax.fill(angles, popularity_scores[i], color=colors[i], alpha=0.25)
    ax.plot(angles, popularity_scores[i], label=flower_types[i], linewidth=2, color=colors[i])

# Add titles and labels
ax.set_title("Petal Power: The Popularity of Different Flower Types\nAcross Seasons in Botanical Gardens", size=16, weight='bold', position=(0.5, 1.1))
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(seasons, size=12, weight='bold')

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12, title="Flower Types")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display plot
plt.show()