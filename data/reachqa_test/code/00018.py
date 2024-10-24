import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Data for tech startups
innovation_scores = np.array([15, 20, 35, 45, 55, 60, 70, 75, 85, 90])
market_influence = np.array([5, 25, 15, 40, 20, 50, 30, 60, 55, 80])

# Creating a smooth line using cubic spline interpolation
tck = interpolate.splrep(innovation_scores, market_influence, s=0)
innovation_fine = np.linspace(min(innovation_scores), max(innovation_scores), 300)
market_fine = interpolate.splev(innovation_fine, tck, der=0)

# Categorizing innovation scores into ranges for a bar chart
bins = [10, 30, 50, 70, 90]
labels = ['10-30', '31-50', '51-70', '71-90']
categories = np.digitize(innovation_scores, bins=bins, right=True)
average_market_influence = [market_influence[categories == i].mean() if len(market_influence[categories == i]) > 0 else 0 for i in range(1, len(bins))]

# Plot
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot with spline
axs[0].scatter(innovation_scores, market_influence, color='blue', label='Startups', s=100, alpha=0.7, edgecolors='k')
axs[0].plot(innovation_fine, market_fine, color='green', linestyle='--', linewidth=2, label='Trend Line (Cubic Spline)')
axs[0].set_title("Tech Startups' Growth Trajectory:\nInnovation vs. Market Influence", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Innovation Score", fontsize=12)
axs[0].set_ylabel("Market Influence", fontsize=12)
axs[0].legend(frameon=False, fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.7)

# Bar chart for average market influence
axs[1].bar(labels, average_market_influence, color='orange', alpha=0.7, edgecolor='k')
axs[1].set_title("Average Market Influence\nper Innovation Score Range", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Innovation Score Range", fontsize=12)
axs[1].set_ylabel("Average Market Influence", fontsize=12)
for i, v in enumerate(average_market_influence):
    axs[1].text(i, v + 1, f"{v:.1f}", ha='center', fontsize=10, color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()