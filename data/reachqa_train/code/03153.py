import matplotlib.pyplot as plt
import numpy as np

# Function to calculate angle for radar chart
def radar_chart_angles(categories):
    n = len(categories)
    return np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()

# Function to create data for radar chart
def create_radar_data(values, angles):
    values += values[:1]
    angles = angles + angles[:1]
    return values, angles

# Define categories and data
categories = ['Memory', 'Attention', 'Problem Solving', 'Creativity', 'Verbal Skills']

# Data for each blend
alpha_mix = [8, 7, 6, 5, 9]
beta_boost = [6, 8, 7, 4, 6]
gamma_grow = [7, 6, 8, 9, 5]
delta_develop = [5, 6, 7, 8, 9]

# Creating radar chart
angles = radar_chart_angles(categories)

# Plot setup
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.suptitle("Optimized Cognitive Abilities\nThrough Nutrient Blends", fontsize=14, fontweight='bold')

# Create data lines and fill
blends_data = {'AlphaMix': alpha_mix, 'BetaBoost': beta_boost, 'GammaGrow': gamma_grow, 'DeltaDevelop': delta_develop}
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

for idx, (blend, color) in enumerate(zip(blends_data.values(), colors)):
    values, angles_filled = create_radar_data(blend.copy(), angles.copy())
    ax.fill(angles_filled, values, color=color, alpha=0.25, label=list(blends_data.keys())[idx])
    ax.plot(angles_filled, values, color=color, linewidth=2)

# Adding labels to the chart
ax.set_yticks(range(1, 11))
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=12)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Nutrient Blends")

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()