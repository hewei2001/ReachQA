import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define decades and their influence scores on modern fashion trends with additional data
decades = np.array([1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
influence_scores_culture = np.array([15, 20, 35, 50, 70, 65, 55, 45, 40])
influence_scores_tech = np.array([10, 15, 25, 40, 55, 60, 60, 70, 75])
influence_scores_economy = np.array([30, 25, 40, 55, 70, 80, 75, 60, 50])

# Generate smooth curves using spline interpolation for each factor
decades_smooth = np.linspace(decades.min(), decades.max(), 500)
spline_culture = make_interp_spline(decades, influence_scores_culture, k=3)
spline_tech = make_interp_spline(decades, influence_scores_tech, k=3)
spline_economy = make_interp_spline(decades, influence_scores_economy, k=3)

influence_culture_smooth = spline_culture(decades_smooth)
influence_tech_smooth = spline_tech(decades_smooth)
influence_economy_smooth = spline_economy(decades_smooth)

# Plot setup with subplots
fig, ax = plt.subplots(2, 1, figsize=(12, 10), constrained_layout=True)

# Main plot for cultural influence
ax[0].scatter(decades, influence_scores_culture, color='deeppink', label='Cultural Influence', s=100, edgecolor='black')
ax[0].plot(decades_smooth, influence_culture_smooth, color='purple', linewidth=2, label='Cultural Smooth Line')
ax[0].set_title('Influence of Various Factors on Modern Fashion Trends', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Decade', fontsize=12)
ax[0].set_ylabel('Cultural Influence Score', fontsize=12)
ax[0].set_xticks(decades)
ax[0].set_yticks(range(0, 101, 10))
ax[0].legend(loc='upper left')
ax[0].grid(alpha=0.3)
ax[0].axhline(y=50, color='gray', linestyle='--', linewidth=1, alpha=0.7)

# Additional subplot for technical and economic influences
ax[1].plot(decades_smooth, influence_tech_smooth, color='blue', linestyle='-', linewidth=2, label='Tech Influence')
ax[1].plot(decades_smooth, influence_economy_smooth, color='green', linestyle='-', linewidth=2, label='Economic Influence')
ax[1].scatter(decades, influence_scores_tech, color='blue', s=100, edgecolor='black')
ax[1].scatter(decades, influence_scores_economy, color='green', s=100, edgecolor='black')
ax[1].set_title('Tech and Economic Influence Trends', fontsize=14)
ax[1].set_xlabel('Decade', fontsize=12)
ax[1].set_ylabel('Influence Score', fontsize=12)
ax[1].set_xticks(decades)
ax[1].set_yticks(range(0, 101, 10))
ax[1].legend(loc='upper left')
ax[1].grid(alpha=0.3)

# Show plot
plt.show()