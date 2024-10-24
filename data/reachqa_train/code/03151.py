import matplotlib.pyplot as plt
import numpy as np

# Function to calculate angles for radar chart
def radar_chart_angles(n):
    return np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()

# Function to create data for radar chart
def create_radar_data(values, angles):
    return values + values[:1], angles + angles[:1]

# Define expanded categories
categories = ['Memory', 'Attention', 'Problem Solving', 'Creativity', 'Verbal Skills',
              'Logical Reasoning', 'Processing Speed', 'Emotional Intelligence']

# Data for each blend
alpha_mix = [8, 7, 6, 5, 9, 8, 6, 7]
beta_boost = [6, 8, 7, 4, 6, 9, 5, 8]
gamma_grow = [7, 6, 8, 9, 5, 7, 8, 6]
delta_develop = [5, 6, 7, 8, 9, 6, 7, 5]
epsilon_enhance = [9, 5, 6, 7, 8, 9, 6, 8]

# Creating radar chart
angles = radar_chart_angles(len(categories))

# Plot setup
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.suptitle("Enhanced Cognitive Abilities Through Nutrient Blends",
             fontsize=14, fontweight='bold', va='bottom')

# Create data lines and fill
blends_data = {'AlphaMix': alpha_mix, 'BetaBoost': beta_boost, 'GammaGrow': gamma_grow,
               'DeltaDevelop': delta_develop, 'EpsilonEnhance': epsilon_enhance}
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#EE82EE']

for idx, (blend, color) in enumerate(zip(blends_data.values(), colors)):
    values, angles_filled = create_radar_data(blend, angles)
    ax.fill(angles_filled, values, color=color, alpha=0.25, label=list(blends_data.keys())[idx])
    ax.plot(angles_filled, values, color=color, linewidth=2)

# Adding labels to the chart
ax.set_yticks(range(1, 11))
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=10)

# Customizing grid and axes
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_ylim(0, 10)

# Add legend with adjusted location
plt.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), title="Nutrient Blends", fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Display the chart
plt.show()