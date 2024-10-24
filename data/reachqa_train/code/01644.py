import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Centuries from the 1500s to the 2000s
centuries = np.array([15, 16, 17, 18, 19, 20, 21])  # Centuries

# Hypothetical Cultural Impact Score for each painting style
impact_scores = np.array([50, 60, 55, 70, 80, 90, 85])  # Cultural Impact Scores

# Generate smooth lines using B-spline interpolation
X_Y_Spline = make_interp_spline(centuries, impact_scores)
X_ = np.linspace(centuries.min(), centuries.max(), 500)
Y_ = X_Y_Spline(X_)

# Set up the plot
plt.figure(figsize=(12, 7))

# Plot scatter points
plt.scatter(centuries, impact_scores, color='crimson', label='Cultural Impact Score', s=100, zorder=5)

# Plot the smooth fitting line
plt.plot(X_, Y_, label='Smooth Trend', color='dodgerblue', linewidth=2)

# Title and labels
plt.title('Evolution of Painting Styles Over the Centuries\nand Their Cultural Impact', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Century', fontsize=14)
plt.ylabel('Cultural Impact Score', fontsize=14)

# Annotate century labels for scatter points
style_labels = ['Renaissance', 'Baroque', 'Neoclassicism', 'Rococo', 'Impressionism', 'Modernism', 'Contemporary']
for i, label in enumerate(style_labels):
    plt.annotate(label, (centuries[i], impact_scores[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='navy')

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=True)

# Adjust layout to avoid clipping
plt.tight_layout()

# Display the chart
plt.show()