import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm as cm

# Define fictional data points for the Andromeda Mission
gravitational_anomalies = np.array([1.2, 1.8, 2.3, 1.7, 2.5, 3.1, 2.8, 3.5, 2.9, 3.8, 4.2, 4.5, 3.0, 4.1])
organic_signature_strengths = np.array([2.1, 2.5, 2.8, 3.2, 2.9, 3.0, 3.3, 3.7, 3.1, 3.5, 3.6, 3.9, 3.2, 3.8])

# Define a size for each data point representing the probe's sensor size
sensor_sizes = np.array([100, 120, 150, 110, 130, 170, 140, 160, 135, 180, 190, 200, 145, 185])

# Define color based on another fictional metric
colors = np.array(['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF4500', 
                   '#8A2BE2', '#20B2AA', '#FF1493', '#7FFF00', '#DC143C', 
                   '#00CED1', '#9400D3', '#F4A460', '#5F9EA0'])

# Create a color map for edge colors
norm = Normalize(vmin=min(gravitational_anomalies), vmax=max(gravitational_anomalies))
cmap = cm.viridis

# Create the scatter plot
plt.figure(figsize=(14, 8))
scatter = plt.scatter(gravitational_anomalies, organic_signature_strengths, s=sensor_sizes, c=colors, 
                      alpha=0.85, edgecolors=cmap(norm(gravitational_anomalies)), linewidth=2, zorder=2)

# Background and grid customization
plt.gca().set_facecolor('#f0f8ff')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Title and labels with new lines and font styles
plt.title("Cosmic Exploration by Humanoid Drones:\nIntergalactic Scatter in the\nAndromeda Mission 2077", fontsize=18, fontweight='bold', y=1.02)
plt.xlabel("Gravitational Anomaly (arbitrary units)", fontsize=14, labelpad=10)
plt.ylabel("Organic Signature Strength (arbitrary units)", fontsize=14, labelpad=10)

# Custom axes styles
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

# Annotate some key points with arrows
for i in range(len(gravitational_anomalies)):
    plt.annotate(f'P{i+1}', 
                 (gravitational_anomalies[i], organic_signature_strengths[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9,
                 arrowprops=dict(arrowstyle='->', lw=0.5, color='gray'))

# Customize ticks for better readability
plt.xticks(np.arange(1, 5.5, 0.5))
plt.yticks(np.arange(2, 4.5, 0.5))

# Add a color legend with mock dynamic elements
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=f'Probe {i+1}',
                              markerfacecolor=colors[i], markersize=10, alpha=0.85) for i in range(len(colors))]
plt.legend(handles=legend_elements, title="Probes", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()