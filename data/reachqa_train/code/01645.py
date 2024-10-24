import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Extended centuries including past, present, and future (12th to 22nd century)
centuries = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

# Hypothetical Cultural Impact Score for each painting style
cultural_impact = np.array([30, 40, 45, 50, 60, 55, 70, 80, 90, 85, 95])
historical_significance = np.array([25, 35, 50, 55, 65, 60, 75, 85, 80, 88, 92])
technological_influence = np.array([10, 20, 25, 35, 50, 45, 60, 70, 75, 80, 90])

# Generate smooth lines using B-spline interpolation for each impact type
x_smooth = np.linspace(centuries.min(), centuries.max(), 500)
cultural_smooth = make_interp_spline(centuries, cultural_impact)(x_smooth)
historical_smooth = make_interp_spline(centuries, historical_significance)(x_smooth)
technological_smooth = make_interp_spline(centuries, technological_influence)(x_smooth)

# Set up the plot with subplots for multi-dimensional impact analysis
fig, axs = plt.subplots(2, 1, figsize=(14, 12), constrained_layout=True)

# Upper Plot: Multi-metric trend lines
axs[0].plot(x_smooth, cultural_smooth, label='Cultural Impact', color='dodgerblue', linewidth=2)
axs[0].plot(x_smooth, historical_smooth, label='Historical Significance', color='green', linestyle='--', linewidth=2)
axs[0].plot(x_smooth, technological_smooth, label='Technological Influence', color='purple', linestyle=':', linewidth=2)

# Scatter points for cultural impact
axs[0].scatter(centuries, cultural_impact, color='crimson', s=100, zorder=5)
axs[0].set_title('Evolution of Painting Styles: Multi-dimensional Impact Over the Centuries', fontsize=15, fontweight='bold')
axs[0].set_xlabel('Century', fontsize=13)
axs[0].set_ylabel('Impact Scores', fontsize=13)
axs[0].legend(loc='upper left', fontsize=11)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Annotate styles on the cultural impact line
style_labels = [
    'Romanesque', 'Gothic', 'Proto-Renaissance', 'Renaissance', 
    'Baroque', 'Neoclassicism', 'Rococo', 'Impressionism', 
    'Modernism', 'Contemporary', 'Future Styles'
]
for i, label in enumerate(style_labels):
    axs[0].annotate(label, (centuries[i], cultural_impact[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='navy')

# Lower Plot: Histogram for distribution of impact scores
axs[1].hist([cultural_impact, historical_significance, technological_influence],
            bins=np.arange(0, 101, 10), stacked=True, label=['Cultural', 'Historical', 'Technological'],
            color=['dodgerblue', 'green', 'purple'], alpha=0.7)
axs[1].set_title('Distribution of Impact Scores Across Metrics', fontsize=15, fontweight='bold')
axs[1].set_xlabel('Impact Score', fontsize=13)
axs[1].set_ylabel('Frequency', fontsize=13)
axs[1].legend(loc='upper right', fontsize=11)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Display the enhanced chart
plt.show()