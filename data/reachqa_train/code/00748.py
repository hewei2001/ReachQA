import matplotlib.pyplot as plt
import numpy as np

# Define smart cities and technologies
cities = ['EcoVille', 'GreenMetropolis', 'SunCity', 'WindHaven', 'FutureTown']
technologies = ['Renewable Integration', 'Smart Grids', 'Efficient Buildings', 'AI Monitoring', 'Transport Electrification']

# Energy efficiency scores for each city based on the technologies
ecoville_scores = [85, 90, 78, 88, 80]
greenmetropolis_scores = [90, 88, 85, 75, 83]
suncity_scores = [78, 85, 80, 82, 88]
windhaven_scores = [80, 83, 90, 85, 82]
futuretown_scores = [82, 88, 75, 90, 89]

# Compile data
scores = [ecoville_scores, greenmetropolis_scores, suncity_scores, windhaven_scores, futuretown_scores]

# Set colors for each technology type
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

# Setup a figure for horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Calculate the bottom positions for stacking bars
bottoms = np.zeros(len(cities))

# Plot each technology's score as stacked bars
for idx, tech in enumerate(technologies):
    ax.barh(cities, [score[idx] for score in scores], label=tech, left=bottoms, color=colors[idx], edgecolor='black', alpha=0.7)
    bottoms += [score[idx] for score in scores]

# Add value labels on the bars
for city_idx, city_scores in enumerate(scores):
    left = 0
    for score_idx, score in enumerate(city_scores):
        ax.text(left + score / 2, city_idx, str(score), va='center', ha='center', color='white', fontsize=9, fontweight='bold')
        left += score

# Add chart title and labels
ax.set_title("Energy Usage Efficiency in Smart Cities:\nAnalyzing 2023's Leading Implementations", fontsize=14, fontweight='bold')
ax.set_xlabel("Energy Efficiency Score", fontsize=12)
ax.set_xlim(0, 500)
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add legend with title
ax.legend(title='Technologies', loc='lower right')

# Ensure that layout is optimal and readable
fig.tight_layout()

# Display the plot
plt.show()