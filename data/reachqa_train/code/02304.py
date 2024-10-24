import matplotlib.pyplot as plt
import numpy as np

# Transportation Concepts
concepts = [
    "E-Bike", "Autonomous Pod", "Solar Scooter", "Hoverboard", 
    "Urban Jetpack", "Flying Car", "Smart Skateboard", "Personal Drone"
]

# Efficiency Scores (out of 100)
efficiency_scores = [85, 90, 75, 65, 50, 45, 70, 55]

# Adoption Potential (out of 10)
adoption_potentials = [8.5, 7.0, 6.0, 4.5, 3.0, 2.5, 5.5, 2.0]

# Stage of Development: (0: Concept, 1: Prototype, 2: Market Ready)
stages = [2, 1, 1, 0, 0, 0, 1, 0]

# Colors for stages
colors = ['green' if stage == 2 else 'orange' if stage == 1 else 'red' for stage in stages]

# Average Efficiency per Stage
stage_labels = ['Concept', 'Prototype', 'Market Ready']
average_efficiency = [
    np.mean([efficiency_scores[i] for i in range(len(stages)) if stages[i] == j]) 
    for j in range(3)
]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Scatter Plot
scatter = axes[0].scatter(efficiency_scores, adoption_potentials, s=150, c=colors, alpha=0.7, edgecolor='black')
for i, concept in enumerate(concepts):
    axes[0].text(efficiency_scores[i], adoption_potentials[i]+0.2, concept, fontsize=8, ha='center', va='bottom')

axes[0].set_title("Innovation on Wheels:\nThe Evolution of Personal Transportation Technology", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Efficiency Score (out of 100)", fontsize=12)
axes[0].set_ylabel("Adoption Potential (out of 10)", fontsize=12)
axes[0].legend(handles=scatter.legend_elements()[0], labels=stage_labels, title="Stage of Development", loc='upper left', fontsize='small')
axes[0].grid(True, linestyle='--', alpha=0.6)

# Bar Chart
axes[1].bar(stage_labels, average_efficiency, color=['red', 'orange', 'green'])
axes[1].set_title("Average Efficiency by Development Stage", fontsize=14)
axes[1].set_xlabel("Stage of Development", fontsize=12)
axes[1].set_ylabel("Average Efficiency Score", fontsize=12)
axes[1].set_ylim(0, 100)
for i, v in enumerate(average_efficiency):
    axes[1].text(i, v + 2, f"{v:.1f}", ha='center', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()