import matplotlib.pyplot as plt
import numpy as np

# Features in modern architectural designs
features = [
    "Solar Panels", "Green Roofs", "Energy-efficient Windows",
    "Rainwater Harvesting", "Insulation", "Smart HVAC"
]

# Data representing the proportion of features in percentage
data = np.array([20, 15, 25, 10, 18, 12])

# Define the number of categories and calculate angles
num_features = len(features)
angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()

# Complete the circle for rose chart
data = np.concatenate((data, [data[0]]))
angles += angles[:1]

# Create a polar plot
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Plot data as a rose chart
bars = ax.bar(angles[:-1], data[:-1], width=(2 * np.pi) / num_features, 
              color=plt.cm.viridis(np.linspace(0, 1, num_features)), alpha=0.7, edgecolor='black')

# Add labels
ax.set_yticklabels([])  # Hide radial ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(features, fontsize=10, fontweight='bold', color='darkblue')

# Add a title
plt.title("Energy Efficiency Features\nin Modern Architectural Designs", fontsize=15, fontweight='bold', va='bottom', color='darkblue')

# Add value annotations
for bar, value in zip(bars, data):
    angle = bar.get_x() + bar.get_width() / 2
    ax.text(angle, bar.get_height() + 2, f"{int(value)}%", ha='center', va='bottom', fontsize=9, color='black')

# Create a legend
ax.legend(bars, features, loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title="Features", title_fontsize='12')

# Automatically adjust the layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()